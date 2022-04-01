using Api.Agents;
using Microsoft.AspNetCore.Mvc;
using Perper.Model;

namespace Api.Controllers;

[ApiController]
[Route("[controller]")]
public class AgentController : ControllerBase
{
    private readonly AgentRegistryRepository _agentRegistryRepository;
    private readonly IPerper _perper;

    public AgentController(AgentRegistryRepository agentRegistryRepository, IPerper perper)
    {
        _agentRegistryRepository = agentRegistryRepository;
        _perper = perper;
    }

    [HttpPost("start-game")]
    public async Task<ActionResult> StartGame([FromBody] StartGame startGame)
    {
        var agent =  await _agentRegistryRepository.GetAgentInstance("GameAgent");
        await _perper.CallAsync(agent, "EnqueueCommand", startGame);
        return Accepted();
    }
    
    [HttpPost("move")]
    public async Task<ActionResult> Move([FromBody] Move move)
    {
        var agent =  await _agentRegistryRepository.GetAgentInstance("GameAgent");
        await _perper.CallAsync(agent, "EnqueueCommand", move);
        return Accepted();
    }
 
    
    [HttpGet("get-game-board")]
    public async Task<ActionResult> GetGameBoard(string userName)
    {
        var agent =  await _agentRegistryRepository.GetAgentInstance("GameAgent");
        var result = await _perper.CallAsync<GameBoard>(agent, "GetGameBoard", userName);

        return Ok(new
        {
            result
        });
    }
}