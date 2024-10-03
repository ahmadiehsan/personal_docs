# Controller

## Description

For API:

<img src="image14.jpg" style="width:5.85833in" />

- It inherited form ControllerBase
- Every controller name must end with the suffix Controller
- If we don’t mention to the \[HttpGet\] annotation directly, the \[HttpGet\] will be used as the default one
- The \[ApiController\] annotation will add some automatic functionalities to the controller, for example by default will check the ModelState property and will generate 400 response if it isn’t valid
- The \[ProducesResponseType\] annotation will help to ASP.NET to generate a better swagger page

For MVC:

<img src="image16.jpg" style="width:5.55417in" />

- It inherited form Controller
- In the above image, the View() method, automatically will find the proper view and will render it
- Every controller name must end with the suffix Controller

For Razor Page:

<img src="image10.jpg" style="width:4.49583in" />

- In the above image, the \[BindProperties\] code will automatically bind incoming data inside of HTTP form-data into the class properties, so no need to write a parameter for the OnPost method

Controller vs ControllerBase:

The Controller class inherited from ControllerBase and added some members that are only needed to support Views.

![](controller/image8.jpg)

<img src="image21.jpg" style="width:5.9375in" />

## Methods

For API:

- Ok: return 200 status code
- NotFound: return 404 status code
- BadRequest: return 400 status code
- CreatedAtRoute: return 201 status code with the record url in the header
- NoContent: return 204 status code

For MVC:

![](controller/image24.jpg)

For Razor Page:

![](controller/image26.jpg)

Configurations (Content of appsettings.json):

By injecting IConfiguration into the class constructor, easily we can access to the settings.

![](controller/image25.jpg)

Model Binding:

Controllers and Razor pages work with data that comes from HTTP requests. For example, route data may provide a record key, and posted form fields may provide values for the properties of the model. Writing code to retrieve each of these values and convert them from strings to .NET types would be tedious and error-prone. Model binding automates this process. The model binding system:

- Retrieves data from various sources such as route data, form fields, and query strings.
- Provides the data to controllers and Razor pages in method parameters and public properties.
- Converts string data to .NET types.
- Updates properties of complex types.

Action Result (Return Type):

![](controller/image9.jpg)

- With the IActionResult interface, easily we can return everything that we want as the response, for example rendering the view, or redirecting to the home page, because all of this response types are child of IActionResult

![](controller/image23.jpg)

## Properties

Logger:

![](controller/image12.jpg)

- We can easily inject the logger into the controller inside of constructor

User:

![](controller/image2.jpg)

ModelState:

- Will store the form validation result
- For example like the below code we can check does our form is valid or not

  <img src="image20.jpg" style="width:2.98333in" />

Data Interpolation:

![](controller/image17.jpg)

- Sending data from controller into the corresponding view

<img src="image5.jpg" style="width:4.775in" />

<img src="image1.jpg" style="width:2.31667in" />

1. passing data directly

  <img src="image7.jpg" style="width:4.2in" />

  <img src="image11.jpg" style="width:4.75417in" />

2. passing data with \[ViewData\] annotation and receiving it via ViewModel

  <img src="image13.jpg" style="width:4.80833in" />

<img src="image4.jpg" style="width:5.73333in" />

![](controller/image3.jpg)

## View Component

Description:

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

Class Syntax:

1. A view component should inherit from ViewComponent

  ![](controller/image18.jpg)

2. It can have DI

  ![](controller/image19.jpg)

3. And should have the InvokeAsync method

  ![](controller/image6.jpg)

  ![](controller/image22.jpg)

4. And finally should return the View method result (The corresponding .cshtml file to the view component)

  ![](controller/image15.jpg)
