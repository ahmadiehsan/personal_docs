# dotnet CLI

## Install

We need to install dotnet SDK for using its command line

## Commands

### new

- **gitignore:** will create a proper gitignore file
- **sln:** will create a new solution in the current directory
- **console:** will create a new console app
- **classlib:** will create a new class library

### add

- **package:** will install a nuget package into the current app or library
- **reference:** will add a reference to another app or library to the current app or lirary

### sln

- **add:** will add one app or library into the current solution

### other

- **restore:** will install all of the current app or library nuget packages
- **build:** will build the current app or library in the bin directory
- **clean:** will remove the bin directory content of the current app or library
- **run:** first will run the build command for the current app and after that will use the bin directory content and will run the app (not a library, because libraries aren’t executable)
- **publish:** will create a production ready build for the current app and its dependencies
- **watch:** will run the current app via a local server (is good for development)
