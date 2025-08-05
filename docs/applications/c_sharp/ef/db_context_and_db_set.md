# DB Context & DB Set

## Description

- The `DbContext` class is an integral part of Entity Framework.
- An instance of DbContext represents a session with the database which can be used to query and save instances of your entities to a database.
- DbContext in EF Core allows us to perform the following tasks:

   - Manage database connection
   - Configure model & relationship
   - Querying database
   - Saving data to the database
   - Configure change tracking
   - Caching
   - Transaction management

## Syntax

```csharp
public class ApplicationDbContext : DbContext {
    public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options) : base(options) {
    }
}
```

- It should inherit from DbContext
- It should be a public class

## Connecting to Project

For EF inside our project, we should add it into the project services by the below code

```csharp
builder.Services.AddDbContext<ApplicationDbContext>(option => {
    option.UseSqlServer(builder.Configuration.GetConnectionString("DefaultSQLConnection"));
});
```

- The GetConnectionString method will read the below part of the `appsettings.json` file

  ```json
  "ConnectionStrings": {
      "DefaultSQLConnection": "Server=.;Database=Magic_VillaAPI;TrustServerCertificate=True;"
  },
  ```

## DB Set

Is a property inside the DbContext that will make one model accessible from the DbContext

```csharp
public DbSet<Category> Categories { get; set; }
```
