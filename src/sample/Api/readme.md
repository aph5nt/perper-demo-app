### before we start
- sync perper submodule

### how to start perper fabric ?
- run docker-compose.yml

#### Agent
- Initializer
  - Init - acts like a deployment method 
- GameAgent
  - Startup - method run only once, after agent deployment (init) but before starting work. We start and combine stream processing there.
  - EnqueueCommand - agent call
  - GetGameBoard - agent call
  - MessageProcessor - agent stream
  - UserWebSocketNotifier - agent stream
  - UserEmailNotifier - agent stream

### Important notes
- agents are not actors
  - agent call(method) use multithreading
  - agent once deployed (by Initializer/Init) lives until will be destroyed. (Event after application restart). In order to clean up deployed agents, restart perper fabric.