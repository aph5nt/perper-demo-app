using Perper.Model;

namespace Api.Agents;

public class AgentRegistryRepository
{
    private readonly IPerper _perper;
    private readonly PerperState _internalState = new (nameof(AgentRegistryRepository));

    public AgentRegistryRepository(IPerper perper)
    {
        _perper = perper;
    }

    public async Task AddAgent(PerperAgent agent)
    {
        await _perper.States.SetAsync(_internalState, agent.Agent, agent);
    }

    public async Task<PerperAgent> GetAgentInstance(string agentName)
    {
        var result = await _perper.States.TryGetAsync<PerperAgent>(_internalState, agentName);
        return result.Exists ? result.Value : null;
    }

    public async Task ExecuteIfAgentNotFound(string agentName, Func<Task> action)
    {
        var result = await _perper.States.TryGetAsync<PerperAgent>(_internalState, agentName);
        if (!result.Exists)
        {
            try
            {
                await action.Invoke();
            }
            catch (Exception ex)
            {
                // log
            }
        }
    }
}