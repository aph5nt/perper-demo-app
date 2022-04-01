namespace Api.Agents;

public record GameStarted(string UserName);
public record UserSurvived(string UserName);
public record UserDied(string UserName);