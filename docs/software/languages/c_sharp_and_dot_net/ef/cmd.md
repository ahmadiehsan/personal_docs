# CMD

## Add Migration

Will create migration files inside the Migration directory in the root of project that DbContext present in it

```shell
dotnet ef --startup-project <path/to/di/project> --project <path/to/db_context/project> migration add <migration>
```

- We should pass a meaningful name to this command

## Update Database

Will apply the migration files on the database

```shell
dotnet ef --startup-project <path/to/di/project> --project <path/to/db_context/project> database update
```

If we pass a migration name to it, this command will rollback migrations

```shell
dotnet ef --startup-project <path/to/di/project> --project <path/to/db_context/project> database update <migration>
```
