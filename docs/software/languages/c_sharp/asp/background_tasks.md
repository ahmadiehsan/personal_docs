# Background Tasks

## Sample Generator

```shell
dotnet new worker -o ContosoWorker
```

## Example

Service:

```csharp
public class Worker : BackgroundService {
    private readonly ILogger<Worker> _logger;

    public Worker(ILogger<Worker> logger)
    {
        _logger = logger;
    }

    protected override async Task ExecuteAsync(CancellationToken stoppingToken)
    {
        while (!stoppingToken.IsCancellationRequested)
        {
            _logger.LogInformation("Worker running at: {time}", DateTimeOffset.Now);
            await Task.Delay(1000, stoppingToken);
        }
    }
}
```

DI:

```csharp
services.AddHostedService<Worker>();
```
