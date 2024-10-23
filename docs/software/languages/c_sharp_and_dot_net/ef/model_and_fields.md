# Model & Fields

## Mappings

### Description

This means mapping one class and its properties to the database table and its fields

![](model_and_fields/image31.jpg)

### Conventions

Will be done automatically by EF

### Annotations

This will be done by the C# annotations

### Fluent API

- This will be done inside of the DbContext class and within the below method

  <img src="image28.jpg" style="width:5.63333in" />

- Or we can create separate config classes for each model

  ![](model_and_fields/image18.jpg)

  We should add them inside of OnModelCreating method

  <img src="image6.jpg" style="width:5.34167in" />

## Model

### Table Name

- Convention: By default, EF will use the DbSet property name for the table name, for example in the below code EF will use Categories for table name

  <img src="image5.jpg" style="width:5.35in" />

- Data Annotation:

  <img src="image26.jpg" style="width:4.35417in" />

- Fluent API:

  <img src="image2.jpg" style="width:5.43333in" />

### ToView

- Fluent API:

  ![](model_and_fields/image20.jpg)

## Fields

### Primary Key

- Convention: By default EF will use the Id field or `<ModelName>Id` field as primary key without need any annotation

  <img src="image4.jpg" style="width:3.36667in" />

- Data Annotation: For the fields other than Id or `<ModelName>Id`, we can explicitly define our primary key like the below

  <img src="image13.jpg" style="width:4.35in" />

- Fluent API:

  <img src="image23.jpg" style="width:5.2in" />Example 1: The below code will create a composite-key

  ![](model_and_fields/image7.jpg)

  Example 2: The below code will tell EF that this table doesn't have primary key

  <img src="image12.jpg" style="width:4.8625in" />

### Foreign Key

- Convention: EF will create FK and CategoryId field in the below code

  <img src="image8.jpg" style="width:4.3875in" />

- Data Annotation: If want to have a field name other than CategoryId, we can use the below code

  <img src="image25.jpg" style="width:4.42083in" />

### One-to-One Relation

- Convention:

  ![](model_and_fields/image19.jpg)

- Data Annotation:

  ![](model_and_fields/image27.jpg)

- Fluent API:

  ![](model_and_fields/image29.jpg)

### One-to-Many Relation

- Convention:

  ![](model_and_fields/image16.jpg)

  tip: can be List<> or ICollection<>

- Data Annotation:

  ![](model_and_fields/image30.jpg)

- Fluent API:

  ![](model_and_fields/image17.jpg)

### Many-to-Many Relation

- Convention:

  ![](model_and_fields/image11.jpg)

  tip: can be ICollection<> or List<>

- Fluent API:

  ![](model_and_fields/image15.jpg)

### Column Name

- Data Annotation:

  <img src="image21.jpg" style="width:4.34583in" />

- Fluent API:

  <img src="image3.jpg" style="width:5.42083in" />

### Required

- Data Annotation:

  <img src="image14.jpg" style="width:4.35in" />

- Fluent API:

  <img src="image10.jpg" style="width:5.22917in" />

### Max Length

- Data Annotation:

  <img src="image24.jpg" style="width:4.36667in" />

- Fluent API:

  <img src="image9.jpg" style="width:5.44167in" />

### Not Mapped

- Data Annotation:

  <img src="image1.jpg" style="width:4.34167in" />

- Fluent API:

  <img src="image22.jpg" style="width:5.46667in" />

### Database Generated

Data Annotation & Fluent API:

![](model_and_fields/image32.jpg)

- Identity: Will set by the DB at row creation
- None: Will prevent the DB to set
- Computed: Will set by the DB at row creation or update
