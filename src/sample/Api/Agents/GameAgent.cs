using Perper.Extensions;
using Perper.Model;
using Serilog;

namespace Api.Agents;
 
public class GameAgent
{
    private readonly IPerperContext _context;

    private PerperStream UserMessageStream
    {
        get =>
            _context.CurrentState
                .GetOrDefaultAsync<PerperStream>("UserMessageStream")
                .GetAwaiter()
                .GetResult();
        
        set => _context.CurrentState.SetAsync("UserMessageStream", value)
            .ConfigureAwait(false)
            .GetAwaiter()
            .GetResult();
    }
    
    public GameAgent(IPerperContext context)
    {
        _context = context;
    }
 
    public async Task Startup()
    {
        var userMessageStream = UserMessageStream =  await PerperContext.BlankStream().StartAsync().ConfigureAwait(false);
        var messageProcessorStream = await PerperContext.Stream("MessageProcessor").StartAsync(userMessageStream, 10).ConfigureAwait(false);
        await PerperContext.Stream("UserWebSocketNotifier").Action().StartAsync(messageProcessorStream).ConfigureAwait(false);
        await PerperContext.Stream("UserEmailNotifier").Action().StartAsync(messageProcessorStream).ConfigureAwait(false);
    }
    
    public async Task EnqueueCommand(object command)
    {
        await UserMessageStream.WriteItemAsync(command);
    }

    public async Task<GameBoard> GetGameBoard(string userName)
    {
        var key = $"GameBoard-{userName}";
        var result = await _context.CurrentState.GetOrDefaultAsync<GameBoard>(key);
        return result;
    }
  
    public async IAsyncEnumerable<object> MessageProcessor(PerperStream userMessageStream)
    {
        await foreach (var message in userMessageStream.EnumerateAsync<object>())
        {
            if (message is StartGame startGame)
            {
                await _context.CurrentState.SetAsync(
                    $"GameBoard-{startGame.UserName}",
                    new GameBoard(startGame.UserName, GameBoardHelper.Generate()));

                Log.Information("Started new game for user {UserName}", startGame.UserName);
                
                yield return new GameStarted(startGame.UserName);
            }

            if (message is Move move)
            {
                var key = $"GameBoard-{move.UserName}";
                
                var gameBoardResult = await _context.CurrentState.TryGetAsync<GameBoard>(key);

                if (gameBoardResult.Exists)
                {
                    var gameBoard = gameBoardResult.Value;
                    
                    var x = gameBoard.Fields.GetLength(0) - 1;
                    var y = gameBoard.Fields.GetLength(1) - 1;

                    if (move.PositionX > x || move.PositionY > y)
                    {
                        continue;
                    }
                
                    Log.Information("Executed move for user {UserName} x:{PositionX} y:{PositionY}", move.UserName, move.PositionX, move.PositionY);
                    
                    var result = gameBoard.Fields[move.PositionX, move.PositionY];
                    if (result == 1)
                    {
                        Log.Information("Yield UserDied event for user {UserName}", move.UserName);
                        
                        yield return new UserDied(move.UserName);
                    }
                    else
                    {
                        Log.Information("Yield UserSurvived event for user {UserName}", move.UserName);
                        
                        yield return new UserSurvived(move.UserName);
                    }
                }
            }
        }
    }
    
    public async Task UserWebSocketNotifier(PerperStream input)
    {
        await foreach (var message in input.EnumerateAsync<object>())
        {
            switch (message)
            {
                case UserDied userDied:
                    Log.Information("Websocket message UserDied for user {UserName}", userDied.UserName);
                    break;
                case UserSurvived userSurvived:
                    Log.Information("Websocket message UserSurvived for user {UserName}", userSurvived.UserName);
                    break;
            }
        }
    }
    
    public async Task UserEmailNotifier(PerperStream input)
    {
        await foreach (var message in input.EnumerateAsync<object>())
        {
            switch (message)
            {
                case UserDied userDied:
                    Log.Information("Sending email message UserDied for user {UserName}", userDied.UserName);
                    break;
                case UserSurvived userSurvived:
                    Log.Information("Sending email UserSurvived for user {UserName}", userSurvived.UserName);
                    break;
            }
        }
    }
}
 