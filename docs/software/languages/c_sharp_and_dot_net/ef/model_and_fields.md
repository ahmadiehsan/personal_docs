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

This will be done inside of the DbContext class and within the below method

```csharp
protected override void OnModelCreating(ModelBuilder modelBuilder) {
  ...
```

Or we can create separate config classes for each model

```csharp
public class AdvertismentConfig : IEntityTypeConfiguration<Advertisment> {
    public void Configure(EntityTypeBuilder<Advertisment> builder) {
        builder.Property(c => c.Price).HasConversion(c => c.Value.Value, d => Price.FromLong(d));
        builder.Property(c => c.OwnerId).HasConversion(c => c.Value.ToString(), d => UserId.FromString(d));
        builder.Property(c => c.ApprovedBy).HasConversion(c => c.Value.ToString(), d => UserId.FromString(d));
        builder.Property(c => c.Text).HasConversion(c => c.Value, d => AdvertismentText.FromString(d));
        builder.Property(c => c.Title).HasConversion(c => c.Value, d => AdvertismentTitle.FromString(d));
    }
}
```

We should add them inside the `OnModelCreating` method

```csharp
modelBuilder.ApplyConfiguration(new FluentBookConfig());
modelBuilder.ApplyConfiguration(new FluentBookDetailsConfig());
modelBuilder.ApplyConfiguration(new FluentBookAuthorConfig());
```

## Model

### Table Name

- Convention: By default, EF will use the DbSet property name for the table name, for example in the below code EF will use Categories for table name

  ```csharp
  public DbSet<Category> Categories { get; set; }
  ```

- Data Annotation:

  ```csharp
  [Table("tb_Category")]
  public class Category
  ```

- Fluent API:

  ```csharp
  protected override void OnModelCreating(ModelBuilder modelBuilder) {
      modelBuilder.Entity<Category>().ToTable("tb_Category");
  }
  ```

### ToView

- Fluent API:

  ```csharp
  protected override void OnModelCreating(ModelBuilder modelBuilder) {
      modelBuilder.Entity<BookDetailsFromView>().HasNoKey().ToView("GetOnlyBookDetails");
  }
  ```

## Fields

### Primary Key

- Convention: By default EF will use the Id field or `<ModelName>Id` field as primary key without need any annotation

  ```csharp
  public class Category {
      public int Id { get; set; }
  }
  ```

- Data Annotation: For the fields other than Id or `<ModelName>Id`, we can explicitly define our primary key like the below

  ```csharp
  [Key]
  public int Category_Id { get; set; }
  ```

- Fluent API:

  ```csharp
  protected override void OnModelCreating(ModelBuilder modelBuilder) {
      modelBuilder.Entity<Category>().HasKey(c => c.Category_Id);
  }
  ```

  Example 1: The below code will create a composite-key

  ```csharp
  modelBuilder.Entity<BookAuthor>().HasKey(ba => new { ba.Author_Id, ba.Book_Id });
  ```

  Example 2: The below code will tell EF that this table doesn't have primary key

  ```csharp
  modelBuilder.Entity<BookDetailsFromView>().HasNoKey();
  ```

### Foreign Key

- Convention: EF will create FK and CategoryId field in the below code

  ```csharp
  public class Book {
      public Category Category { get; set; }
  }
  ```

- Data Annotation: If want to have a field name other than CategoryId, we can use the below code

  ```csharp
  public class Book {
      [ForeignKey("Category")]
      public int Category_Id { get; set; }
      public Category Category { get; set; }
  }
  ```

### One-to-One Relation

- Convention:

  ```csharp
  public class Book {
      public BookDetail BookDetail { get; set; }
  }

  public class BookDetail {
      public Book Book { get; set; }
  }
  ```

- Data Annotation:

  ```csharp
  public class Book {
      [ForeignKey("BookDetail")]
      public int BookDetail_Id { get; set; }
      public BookDetail BookDetail { get; set; }
  }

  public class BookDetail {
      public Book Book { get; set; }
  }
  ```

- Fluent API:

  ```csharp
  public class Book {
      public int Book_Id { get; set; }
      public int BookDetail_Id { get; set; }
      public BookDetail BookDetail { get; set; }
  }

  public class BookDetail {
      public Book Book { get; set; }
  }

  protected override void OnModelCreating(ModelBuilder modelBuilder) {
      modelBuilder.Entity<Books>().HasKey(b => b.Book_Id);
      modelBuilder.Entity<Books>()
          .HasOne(z => z.BookDetail)
          .WithOne(z => z.Book)
          .HasForeignKey<Books>("BookDetail_Id");
  }
  ```

### One-to-Many Relation

- Convention:

  ```csharp
  public class Book {
      public Publisher Publisher { get; set; }
  }

  public class Publisher {
      public List<Books> Books { get; set; }
  }
  ```

  !!! info

      Can be List<> or ICollection<>

- Data Annotation:

  ```csharp
  public class Book {
      [ForeignKey("Publisher")]
      public int Publisher_Id { get; set; }
      public Publisher Publisher { get; set; }
  }

  public class Publisher {
      public List<Books> Books { get; set; }
  }
  ```

- Fluent API:

  ```csharp
  public class Book
  {
      public int BookId { get; set; }

      public int Publisher_Id { get; set; }
      public Publisher Publisher { get; set; }
  }

  public class Publisher
  {
      public List<Books> Books { get; set; }
  }

  protected override void OnModelCreating(ModelBuilder modelBuilder)
  {
      modelBuilder.Entity<Books>().HasKey(b => b.BookId);
      modelBuilder.Entity<Books>()
          .HasOne(z => z.Publisher)
          .WithMany(z => z.Books)
          .HasForeignKey(z => z.Publisher_Id);
  }
  ```

### Many-to-Many Relation

- Convention:

  ![](model_and_fields/image11.jpg)

  !!! info

      Can be ICollection<> or List<>

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
