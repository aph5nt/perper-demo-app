namespace Api.Agents;

public record StartGame(string UserName);
public record Move(string UserName, ushort PositionX, ushort PositionY);