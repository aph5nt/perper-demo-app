namespace Api.Agents;

public record GameBoard(string UserName, ushort[,] Fields);

public static class GameBoardHelper
{
    public static ushort[,] Generate()
    {
        var rnd = new Random();
        
        return new ushort[3,3] { 
            {(ushort)rnd.Next(0, 2), (ushort)rnd.Next(0, 2), (ushort)rnd.Next(0, 2)}, 
            {(ushort)rnd.Next(0, 2), (ushort)rnd.Next(0, 2), (ushort)rnd.Next(0, 2)}, 
            {(ushort)rnd.Next(0, 2), (ushort)rnd.Next(0, 2), (ushort)rnd.Next(0, 2)} 
        };
    }
}