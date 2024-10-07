# DB Context & DB Set

## Description

![](db_context_and_db_set/image4.jpg)

## Syntax

![](db_context_and_db_set/image2.jpg)

- It should inherit from DbContext
- It should be a public class

## Connecting to Project

For EF inside our project, we should add it into the project services by the below code

![](db_context_and_db_set/image5.jpg)

- The GetConnectionString method will read the below part of the appsettings.json file

  ![](db_context_and_db_set/image1.jpg)

## DB Set

Is a property inside of the DbContext that will make one model accessible from the DbContext

<img src="image3.jpg" style="width:5.35in" />
