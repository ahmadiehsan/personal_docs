# Routing

## Description

### MVC

The URL pattern for routing is considered after the domain name.

- `https://localhost:55555/Category/Index/3`
- `https://localhost:55555/{controller}/{action}/{id}`

| URL                                       | Controller | Action  | Id   |
|-------------------------------------------|------------|---------|------|
| https://localhost:55555/Category/Index    | Category   | Index   | Null |
| https://localhost:55555/Category          | Category   | Index   | Null |
| https://localhost:55555/Category/Edit/3   | Category   | Edit    | 3    |
| https://localhost:55555/Product/Details/3 | Product    | Details | 3    |

- We should have a file followed the `<ControllerName>Controller.cs` naming convention inside the Controllers directory
- Inside the Views directory, we should have a directory followed the `<ControllerName>` convention that contains one `<ActionName>.cshtml` file for each action method inside the controller

### Razor Page

- Routing in Asp.net Razor pages maps URL's to Physical file on disk.
- Razor pages need a root folder.
- Index.cshtml is the default document.

| URL                    | Maps To                                                |
|------------------------|--------------------------------------------------------|
| www.domain.com         | /Pages/Index.cshtml                                    |
| www.domain.com/index   | /Pages/Index.cshtml                                    |
| www.domain.com/account | /Pages/account.cshtml <br> /Pages/account/index.cshtml |

- All the pages and codes are combined in one directory named Pages
- For each page there are two files, `<PageName>.cshtml` and `<PageName>.cshtml.cs`
