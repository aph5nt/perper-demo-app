using Perper.Extensions;

namespace Api.Agents;

public class Initializer
{
    private readonly AgentRegistryRepository _agentRegistryRepository;

    public Initializer(AgentRegistryRepository agentRegistryRepository)
    {
        _agentRegistryRepository = agentRegistryRepository;
    }
    
    public async Task Init()
    {
        await _agentRegistryRepository.ExecuteIfAgentNotFound("GameAgent", async () =>
        {
            var gameAgent = await PerperContext.StartAgentAsync("GameAgent");
            await _agentRegistryRepository.AddAgent(gameAgent);
        });
    }
}