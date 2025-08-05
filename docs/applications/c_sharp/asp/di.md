# DI

## Description

First we should create a builder with the below code inside of the Program.cs file

```csharp
var builder = WebApplication.CreateBuilder(args);
```

Then with one of the below approaches we can inject our class into the application

## Injection Approaches

### AddSingleton

Will create once per process

### AddScoped

Will create once per request

```csharp
builder.Services.AddScoped<ICategoryRepository, CategoryRepository>();
```

### AddTransient

Will create once per reference

### AddHostedService

A hosted service is more than just a singleton service.

The runtime "knows" about it, can tell it to start by calling StartAsync or stop by calling StopAsync() whenever eg the application pool is recycled. The runtime can wait for the hosted service to finish before the web application itself terminates.

- One huge difference is that AddSingleton() is lazy while AddHostedService() is eager.
- A service added with AddSingleton() will be instantiated the first time it is injected into a class constructor. This is fine for most services, but if it really is a background service you want, you probably want it to start right away.
- A service added with AddHostedService() will be instantiated immediately, even if no other class will ever want it injected into its constructor. This is typical for background services, that run all the time.
- Also, it seems that you cannot inject a service added with AddHostedService() into another class.

### AddDbContext

```csharp
builder.Services.AddDbContext<ApplicationDbContext>(options =>
    options.UseSqlServer(
        builder.Configuration.GetConnectionString("DefaultConnection")
    )
);
```

### AddHttpClient

```csharp
builder.Services.AddHttpClient<IAService, AService>()
    .ConfigureHttpClient((provider, httpClient) =>
    {
        httpClient.BaseAddress = new Uri("https://example.com/");
    })
    .SetHandlerLifetime(TimeSpan.FromMinutes(60));
```

### Configurations (Content of `appsettings.json`)

- **Options Pattern**: First we should create a class like the StripeSettngs in the below image, then with using the GetSection method simply we can receive any data from appsettings.json file

  ```csharp
  builder.Services.Configure<StripeSettings>(
      builder.Configuration.GetSection("Stripe")
  );
  ```

  Now we can easily inject the class configuration by the below code:

  ```csharp
  IOptionsMonitor<StripeSettings> stripeSettings;
  ```

- **Direct Way**: Another way for reading from appsettings.json file without any middle class is like the bellow:

  ```csharp
  var secretKey = builder.Configuration
      .GetSection("Stripe:SecretKey")
      .Get<string>();
  ```

## Builtin Injectable Classes

### IHttpContextAccessor

- The current session request object
- Injection syntax:

  ```csharp
  builder.Services.AddHttpContextAccessor();
  ```

### IDataProtectionProvider

- Will use for data encryption and decryption
- Injection syntax:

  ```csharp
  builder.Services.AddDataProtection();
  ```
