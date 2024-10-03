# Structure

## Project Content

### appsettings.json

- In the root of the project there is a file named appsettings.Development.json that contains project settings like DB connection credential, log configs, and etc
- This file can contains other versions like appsettings.Production.json or appsettings.Staging.json
- We can access to its content with the builder.Configuration inside the Program.cs file

### Program.cs

- This is the entry point of the project
- Inside of this file, we can easily access the appsettings.json content with the builder.Configuration code
