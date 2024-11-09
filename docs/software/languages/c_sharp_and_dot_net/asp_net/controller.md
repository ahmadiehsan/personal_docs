# Controller

## Varieties

### API

```csharp
[Route("api/VillaAPI")]
[ApiController]
public class VillaAPIController : ControllerBase
{
    [HttpGet]
    [ProducesResponseType(StatusCodes.Status200OK)]
    public ActionResult<IEnumerable<VillaDTO>> GetVillas()
    {
        return Ok(VillaStore.villaList);
    }
}
```

- It inherited form ControllerBase
- Every controller name must end with the suffix Controller
- If we don't mention to the \[HttpGet\] annotation directly, the \[HttpGet\] will be used as the default one
- The \[ApiController\] annotation will add some automatic functionalities to the controller, for example by default will check the ModelState property and will generate 400 response if it isn't valid
- The \[ProducesResponseType\] annotation will help to ASP.NET to generate a better swagger page

### MVC

```csharp
public class HomeController : Controller
{
    private readonly ILogger<HomeController> _logger;

    public HomeController(ILogger<HomeController> logger)
    {
        _logger = logger;
    }

    public IActionResult Index()
    {
        return View();
    }
}
```

- It inherited form Controller
- In the above image, the View() method, automatically will find the proper view and will render it
- Every controller name must end with the suffix Controller

### Razor Page

```csharp
[BindProperties]
public class CreateModel : PageModel
{
    private readonly ApplicationDbContext _db;

    public Category Category { get; set; }

    public CreateModel(ApplicationDbContext db)
    {
        _db = db;
    }

    public void OnGet()
    {
    }

    public async Task<IActionResult> OnPost()
    {
        await _db.Category.AddAsync(Category);
        await _db.SaveChangesAsync();
        return RedirectToPage("Index");
    }
}
```

- In the above code, the `[BindProperties]` code will automatically bind incoming data inside of HTTP form-data into the class properties, so no need to write a parameter for the OnPost method.

### Controller vs ControllerBase

The Controller class inherited from ControllerBase and added some members that are only needed to support Views.

```csharp
public abstract class Controller : ControllerBase
{
    public dynamic ViewBag { get; }
    public virtual ViewResult View(object model) { }
    // more View support stuff
}
```

!!! info

    Don't create a web API controller by deriving from the Controller class. Controller derives from ControllerBase and adds support for views, so it's for handling web pages, not web API requests. There's an exception to this rule: **if you plan to use the same controller for both views and web APIs, derive it from Controller.**

## Methods

### API Methods

| Helper Method  | Description                                              |
|----------------|----------------------------------------------------------|
| Ok             | return 200 status code                                   |
| NotFound       | return 404 status code                                   |
| BadRequest     | return 400 status code                                   |
| CreatedAtRoute | return 201 status code with the record url in the header |
| NoContent      | return 204 status code                                   |

### MVC Methods

| Action Result         | Helper Method                         | Description                                                                                         |
|-----------------------|---------------------------------------|-----------------------------------------------------------------------------------------------------|
| ViewResult            | View                                  | Renders a view as a Web page.                                                                       |
| PartialViewResult     | PartialView                           | Renders a partial view, which defines a section of a view that can be rendered inside another view. |
| RedirectResult        | Redirect                              | Redirects to another action method by using its URL.                                                |
| RedirectToRouteResult | RedirectToAction <br> RedirectToRoute | Redirects to another action method.                                                                 |
| ContentResult         | Content                               | Returns a user-defined content type.                                                                |
| JsonResult            | Json                                  | Returns a serialized JSON object.                                                                   |
| JavaScriptResult      | JavaScript                            | Returns a script that can be executed on the client.                                                |
| FileResult            | File                                  | Returns binary output to write to the response.                                                     |
| EmptyResult           | (None)                                | Represents a return value that is used if the action method must return a null result (void).       |

### Razor Page Methods

| ActionResult         | Helper Method                                                                                             | Description                                                                                                                                                                                                  |
|----------------------|-----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ContentResult        | Content                                                                                                   | Takes a string and returns it with a text/plain content-type header by default. Overloads enable you to specify the content-type to return other formats such as text/html or application/json, for example. |
| FileContentResult    | File                                                                                                      | Returns a file from a byte array, stream or virtual path.                                                                                                                                                    |
| NotFoundResult       | NotFound                                                                                                  | Returns an HTTP 404 (Not Found) status code indicating that the requested resource could not be found.                                                                                                       |
| PageResult           | Page                                                                                                      | Will process and return the result of the current page.                                                                                                                                                      |
| PartialResult        | Partial                                                                                                   | Returns a Partial Page.                                                                                                                                                                                      |
| RedirectToPageResult | RedirectToPage RedirectToPagePermanent RedirectToPagePreserveMethod RedirectToPagePreserveMethodPermanent | Redirects the user to the specified page.                                                                                                                                                                    |
| ViewComponentResult  |                                                                                                           | Returns the result of executing a ViewComponent.                                                                                                                                                             |

### Configurations (Content of `appsettings.json`)

By injecting `IConfiguration` into the class constructor, easily we can access to the settings.

```csharp
public string SendGridSecret { get; set; }

public EmailSender(IConfiguration _config)
{
    SendGridSecret = _config.GetValue<string>("SendGrid:SecretKey");
}
```

### Model Binding

Controllers and Razor pages work with data that comes from HTTP requests. For example, route data may provide a record key, and posted form fields may provide values for the properties of the model. Writing code to retrieve each of these values and convert them from strings to .NET types would be tedious and error-prone. Model binding automates this process. The model binding system:

- Retrieves data from various sources such as route data, form fields, and query strings.
- Provides the data to controllers and Razor pages in method parameters and public properties.
- Converts string data to .NET types.
- Updates properties of complex types.

### Action Result (Return Type)

- ActionResult is a result of action methods/pages or return types of action methods/page handlers.
- Action result is a parent class for many of the derived classes that have associated helpers.
- The IActionResult return type is appropriate when multiple ActionResult return types are possible in an action.
- With the IActionResult interface, easily we can return everything that we want as the response, for example rendering the view, or redirecting to the home page, because all of this response types are child of IActionResult

MVC Application:

```csharp
public IActionResult Index()
{
    return View();
}
```

Razor Page Application:

```csharp
public IActionResult OnPost()
{
    return Page();
}
```

## Properties

### Logger

We can easily inject the logger into the controller inside of constructor

```csharp
private readonly ILogger<VillaAPIController> _logger;

public VillaAPIController(ILogger<VillaAPIController> logger)
{
    _logger = logger;
}
```

### User

If you need to get the user from within the controller, use the `User` property of Controller.

### ModelState

- Will store the form validation result
- For example like the below code we can check does our form is valid or not

  ```csharp
  if (ModelState.IsValid) {
      // Your flow here
  }
  ```

## Data Interpolation

### Interpolation Varieties

Sending data from controller into the corresponding view

| **VIEWBAG**                                                                                                                             | **VIEWDATA**                                                                                                                             | **TEMPDATA**                                                                                   |
|-----------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| ViewBag transfers data from the Controller to View, not vice-versa. Ideal for situations in which the temporary data is not in a model. | ViewData transfers data from the Controller to View, not vice-versa. Ideal for situations in which the temporary data is not in a model. | TempData can be used to store data between two consecutive requests.                           |
| ViewBag is a dynamic property that takes advantage of the new dynamic features in C# 4.0                                                | ViewData is derived from ViewDataDictionary, which is a dictionary type.                                                                 | TempData internally uses Session to store the data. So think of it as a short-lived session.   |
| Any number of properties and values can be assigned to ViewBag                                                                          | ViewData value must be type cast before use.                                                                                             | TempData value must be type cast before use. Check for null values to avoid runtime error.     |
| The ViewBag's life only lasts during the current http request. ViewBag values will be null if redirection occurs.                       | The ViewData's life only lasts during the current http request. ViewData values will be null if redirection occurs.                      | TempData can be used to store only one-time messages like error messages, validation messages. |
| ViewBag is actually a wrapper around ViewData.                                                                                          |                                                                                                                                          |                                                                                                |

!!! info

    ViewBag internally inserts data into ViewData dictionary. So the key of ViewData and property of ViewBag must **NOT** match.

### ViewBag

```csharp
ViewBag.CategoryList = CategoryList;
```

```html
asp-items="ViewBag.CategoryList"
```

### ViewData

1. passing data directly

  ```csharp
  ViewData["CoverTypeList"] = CoverTypeList;
  ```

  ```html
  asp-items="@(ViewData["CoverTypeList"] as IEnumerable<SelectListItem>)"
  ```

2. passing data with `[ViewData]` annotation and receiving it via ViewModel

  ```csharp
  public class IndexModel : PageModel
  {
      [ViewData]
      public string Message { get; set; }

      public void OnGet()
      {
          Message = "Hello World";
      }
  }
  ```

  Now the `Message` property can be accessed in the view via the `Model` property or the ViewData dictionary:

  ```html
  @page
  @model IndexModel
  @{

  }
  <h2>@Model.Message</h2>
  <h2>@ViewData["Message"]</h2>
  ```

### TempData

```csharp
TempData["success"] = "Category created successfully";
```

```html
<script type="text/javascript">
    toastr.success('@TempData["success"]');
</script>
```

## View Component

### Description

View components are similar to partial views, but they're much more powerful. View components **don't use model binding**, they depend on the data passed when calling the view component

A view component:

- Renders a chunk rather than a whole response.
- Includes the same separation-of-concerns and testability benefits found between a controller and view.
- Can have parameters and business logic.
- Is typically invoked from a layout page.

View components are intended anywhere reusable rendering logic that's too complex for a partial view, such as:

- Dynamic navigation menus
- Tag cloud, where it queries the database
- Sign in panel
- Shopping cart
- Recently published articles
- Sidebar content on a blog
- A sign in panel that would be rendered on every page and show either the links to sign out or sign in, depending on the sign in state of the user

A view component consists of two parts:

- The class, typically derived from ViewComponent
- The result it returns, typically a view

### Syntax

```csharp
public class ShoppingCartViewComponent : ViewComponent
{
    private readonly IUnitOfWork _unitOfWork;
    public ShoppingCartViewComponent(IUnitOfWork unitOfWork)
    {
        _unitOfWork = unitOfWork;
    }

    public async Task<IViewComponentResult> InvokeAsync()
    {
        return View(0);
    }
}
```

- A view component should inherit from ViewComponent
- It can have DI
- A view component defines its logic in an:

   - `InvokeAsync` method that returns `Task<IViewComponentResult>`.
   - `Invoke` synchronous method that returns an `IViewComponentResult`.

- And finally should return the View method result (The corresponding .cshtml file to the view component)
