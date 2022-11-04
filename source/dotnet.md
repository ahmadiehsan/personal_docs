# .NET

## Command Line

### new solution

```shell
cd <projects>
mkdir CoolApp
cd CoolApp
dotnet new sln
```

### new project

```shell
cd <solution_dir>
mkdir src
dotnet new <project_type: classlib> -o src/<ProjectName>
dotnet sln add src/<ProjectName>
```

