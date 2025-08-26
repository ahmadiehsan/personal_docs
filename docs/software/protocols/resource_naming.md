# Resource Naming [Rule]

## Description

For more clarity, let's divide the resource archetypes into four categories

- document
- collection
- store
- controller

Then it would be best if you always targeted to put a resource into one archetype and then use its naming convention consistently.

## Document

A document resource is a singular concept that is akin to an object instance or database record.

In REST, you can view it as a single resource inside a resource collection.
A document's state representation typically includes both fields with values and links to other related resources.

Use the "singular" name to denote the document resource archetype.

```text
http://api.example.com/device-management/managed-devices/{device-id}
http://api.example.com/user-management/users/{id}
http://api.example.com/user-management/users/admin
```

## Collection

A collection resource is a **server-managed directory of resources**.

Clients may propose new resources to be added to a collection.
However, it is up to the collection resource to choose whether to create a new resource or not.

A collection resource chooses what it wants to contain and also decides the URIs of each contained resource.

```text
http://api.example.com/device-management/managed-devices
http://api.example.com/user-management/users
http://api.example.com/user-management/users/{id}/accounts
```

Use the "plural" name to denote the collection resource archetype.

## Store

A store is a **client-managed resource repository**.
A store resource lets an API client put resources in, get them back out, and decide when to delete them.

A store never generates new URIs.
Instead, each stored resource has a URI.
The URI was chosen by a client when the resource was initially put into the store.

Use "plural" name to denote store resource archetype.

```text
http://api.example.com/song-management/users/{id}/playlists
```

## Controller

A controller resource models a procedural concept.
Controller resources are like executable functions, with parameters and return values, inputs, and outputs.

Use "verb" to denote the controller archetype.

```text
http://api.example.com/cart-management/users/{id}/cart/checkout
http://api.example.com/song-management/users/{id}/playlist/play
```
