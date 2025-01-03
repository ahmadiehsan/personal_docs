# RESTful API [HTTP1]

## Description

REST defines 6 architectural constraints that make any web service a truly RESTful API

- Uniform interface
- Client-server
- Stateless
- Cacheable
- Layered system
- Code on demand (optional)

REST doesn't have any relation with HTTP, which means we can have a RESTful API on every protocol by following these constraints

## REST Constraints

### Uniform Interface

As the constraint name itself applies, you MUST decide API interface for resources inside the system that are exposed to API consumers and follow religiously. A resource in the system should have only one logical URI, and that should provide a way to fetch related or additional data. It's always better to synonymize a resource with a web page.

Any single resource should not be too large and contain each and everything in its representation. Whenever relevant, a resource should contain links (HATEOAS) pointing to relative URIs to fetch related information.

Also, the resource representations across the system should follow specific guidelines such as naming conventions, link formats, or data format (XML and/or JSON).

All resources should be accessible through a common approach such as HTTP GET and similarly modified using a consistent approach.

Once a developer becomes familiar with one of your APIs, he should be able to follow a similar approach for other APIs.

### Client–Server

This constraint essentially means that client applications and server applications MUST be able to evolve separately without any dependency on each other. A client should know only resource URIs, and that's all. Today, this is standard practice in web development, so nothing fancy is required from your side. Keep it simple.

Servers and clients may also be replaced and developed independently, as long as the interface between them is not altered.

### Stateless

Roy fielding got inspiration from HTTP, so it reflected in this constraint. Make all client-server interactions stateless. The server will not store anything about the latest HTTP request the client made. It will treat every request as new. No session, no history.

If the client application needs to be a stateful application for the end-user, where the user logs in once and does other authorized operations after that, then each request from the client should contain all the information necessary to service the request – including authentication and authorization details.

No client context shall be stored on the server between requests. The client is responsible for managing the state of the application.

### Cacheable

In today's world, the caching of data and responses is of utmost importance wherever they are applicable/possible. The webpage you are reading here is also a cached version of the HTML page. Caching brings performance improvement for the client side and better scope for scalability for a server because the load has been reduced.

In REST, caching shall be applied to resources when applicable, and then these resources MUST declare themselves cacheable. Caching can be implemented on the server or client side.

Well-managed caching partially or eliminates some client-server interactions, further improving scalability and performance.

### Layered System

REST allows you to use a layered system architecture where you deploy the APIs on server A, store data on server B, and authenticate requests in Server C, for example. A client cannot ordinarily tell whether it is connected directly to the end server or an intermediary along the way.

### Code on Demand (optional)

Well, this constraint is optional. Most of the time, you will be sending the static representations of resources in the form of XML or JSON. But when you need to, you are free to return executable code to support a part of your application, e.g., clients may call your API to get a UI widget rendering code. It is permitted.

## Richardson Maturity Model

Leonard Richardson analyzed a hundred different web service designs and divided these designs into four categories. These categories are based on how much the web services are REST compliant.

<img src="image1.jpg" style="width:4in" />
