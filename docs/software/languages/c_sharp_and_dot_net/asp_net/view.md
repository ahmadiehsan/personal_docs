# View

## Layout View

The `Views/Shared/_Layout.cshtml` is the mother of all pages

## Partial Views

- A partial view is a `.cshtml` markup file without an `@page` directive maintained within the Views folder (MVC) or Pages folder (Razor Pages)
- ASP.NET will look at the below path for resolving a partial view:

   - Razor Pages

     1. Currently executing page's folder
     2. Directory graph above the page's folder
     3. `/Shared`
     4. `/Pages/Shared`
     5. `/Views/Shared`

   - MVC

     1. `/Areas/<Area-Name>/Views/<Controller-Name>`
     2. `/Areas/<Area-Name>/Views/Shared`
     3. `/Views/Shared`
     4. `/Pages/Shared`

- Name of them should start with _
- Simply with the below syntax we can import them inside of the other pages:

   ```html
   <partial name="_PartialName" />
   ```

## View Model

At the top of each .html file, we should have a `@model` tag, this tag will point into the ViewModel of the HTML file, like the below code:

```html
@model BulkyBook.Models.ViewModels.ProductVM
```

For this tag we can easily pass the Entity model, or for the complex scenarios, we can create a custom ViewModel like the below:

```csharp
public class ProductVM {
    public Product Product { get; set; }
    public IEnumerable<SelectListItem> CategoryList { get; set; }
    public IEnumerable<SelectListItem> CoverTypeList { get; set; }
}
```

## Tag Helpers

- Tag Helpers are introduced with ASP.NET Core.
- Tag Helpers enable server-side code to participate in creating and rendering HTML elements in Razor files.
- Tag Helpers are very focused around the html elements and much more natural to use.

```html
@* -------HTML Helper-------- *@
@Html.Label("FirstName", "FirstName : ", new { @class = "form-control" })

@* -------TAG Helper-------- *@
<label class="form-control" asp-for="FirstName"></label>
```

```html
@* -------HTML Helper-------- *@
@Html.LabelFor(m=>m.FirstName, new { @class="col-md-2 control-label" })

@* -------TAG Helper-------- *@
<label asp-for="FirstName" class="col-md-2 control-label"></label>
```

```html
@* -------HTML Helper-------- *@
@using (Html.BeginForm("Index", "Users", FormMethod.Post, new { @class = "form-horizontal" }))
{
}

@* -------TAG Helper-------- *@
<form class="form-horizontal" method="post" asp-controller="Users" asp-action="Index"></form>
<form class="form-horizontal" method="post" asp-page="Users/Index"></form>
```

## View Component

1. The runtime searches for the view in the following paths:

   - `/Views/{Controller Name}/Components/{View Component Name}/{View Name}`
   - `/Views/Shared/Components/{View Component Name}/{View Name}`
   - `/Pages/Shared/Components/{View Component Name}/{View Name}`

2. The default view name for a view component is Default, which means view files will typically be named Default.cshtml
3. Render syntax

   ```html
   @await Component.InvokeAsync("Name of view component", {Anonymous Type Containing Parameters})
   ```
