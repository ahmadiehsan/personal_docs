# Identity

## Identity and Role

Claim:

The personal information inside one identity

For example:

- first name
- last name
- id number
- national id

<img src="image13.jpg" style="width:4.63238in" />

Identity:

Identity objects represent users

<img src="image6.jpg" style="width:4.64106in" />

Role (Legacy):

Roles represent memberships and security contexts

<img src="image15.jpg" style="width:4.15532in" />

Principal:

The principal object encapsulates both an identity object and a role

<img src="image9.jpg" style="width:5.60254in" />

<img src="image17.jpg" style="width:5.72917in" />

## User Object

Description:

- User is a builtin property in the ASP.NET controllers
- We can access to the User by HttpContext also

Methods:

- **HasClaim:** will check does user have specific claim or not

## Authentication

Authentication Service:

![](identity/image18.jpg)

- **AddAuthentication:** will tell ASP.NET to use which authentication service (MyCookieAuth) for authenticating the user
- **AddCookie:** will tell ASP.NET to set the user data in where when we are authenticating the user with the MyCookieAuth authentication service
- Another example

  <img src="image22.jpg" style="width:4.475in" />

IAuthenticationService:

<img src="image8.jpg" style="width:3.59594in" />

Every class that wants to implement a new authentication service, should implement this interface, for example by using the AddCookie method, APS.NET will add a cookie based authentication service into its authentication services.

SignIn:

<img src="image24.jpg" style="width:5.52752in" />

Will tell ASP.NET to authenticate the user (claimsPrincipal) with the MyCookieAuth authentication service

Authentication Middleware:

<img src="image2.jpg" style="width:3.97345in" />

Will tell ASP.NET to use my authentication service choice in the AddAuthentication, and try to authenticate the current user

## Authorization

Authorization Service & Policy:

<img src="image23.jpg" style="width:3.01159in" />

<img src="image10.jpg" style="width:4.76313in" />

- **AddAuthorization:** will tell ASP.NET that we want to update the default authorization service
- **AddPolicy:** will add a new access policy
- **RequireClaim (static perm):** will tell ASP.NET that for passing the MustBelongToHRDepartment policy, the user should have a Department claim with the HR value in his/her identity
- **RequireRole:** except from RequireClaim we can use the below code for checking does the user has specific role or not

  <img src="image21.jpg" style="width:4.70833in" />

- **Requirements.Add (dynamic perm):** will tell ASP.NET that for passing the HRManagerOnly policy, the user should pass the custom HRManagerProbationRequirement requirement
- 1st example

  <img src="image4.jpg" style="width:4.32917in" />

- 2nd example

  <img src="image3.jpg" style="width:3.625in" />

Authorize Annotation:

- User should be at least authenticated to access to this page:

  <img src="image19.jpg" style="width:3.52298in" />

- User should be authenticated and pass the MustBelongToHRDepartment policy to access to this page

  <img src="image11.jpg" style="width:4.47059in" />

- User should be authenticated and has the Manager role to access to this controller

  <img src="image20.jpg" style="width:4.43333in" />

- User can access to an action in the controller that is authorization required

  <img src="image5.jpg" style="width:3.72083in" />

IAuthorizationService:

<img src="image14.jpg" style="width:5.07998in" />

Authorization Middleware:

<img src="image12.jpg" style="width:2.96713in" />

## Identity Framework

Description:

![](identity/image25.jpg)

Microsoft package for easier work with user and its related actions like sign-in, sign-out, change password, and etc.

- The down side of it is that it’s tied with EF framework

Usage:

<img src="image16.jpg" style="width:4.268in" />

- **AddIdentity:** will add the core functionality of identity framework
- **AddDefaultTokenProviders:** will add bunch of authentication ways

<img src="image1.jpg" style="width:3.16644in" />

<img src="image7.jpg" style="width:2.55in" />

- Three helper classes of identity framework that we can DI them in our controllers
- **UserManager:**

   - get or update or save a user
   - add a claim to a user
   - remove a claim from a user
   - add a role to a user
   - remove a role from a user

- **SignInManager:** will help us to sign-in or sign-out a user
- **RoleManager:** will help us to add or remove a role
