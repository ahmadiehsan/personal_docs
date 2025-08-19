# Safety vs Transparency

## Description

You might remember that in the Composite Pattern chapter, the composites (Menus) and the leaves (MenuItems) had the same set of methods, including the add() method.
Because they had the same set of methods, we could call methods on MenuItems that didn't make sense (like trying to add something to a MenuItem by calling add()).
The benefit of this was that the distinction between leaves and composites was transparent: the client didn't have to know whether it was dealing with a leaf or a composite; it just called the same methods on both.

Here, we've decided to keep the composite's child maintenance methods separate from the leaf nodes: that is, only Flocks have the add() method.
We know it doesn't make sense to try to add something to a Duck, and in this implementation, you can't.
You can only add() to a Flock.
So this design is safer—you can't call methods that don't make sense on components—but it's less transparent.
Now the client has to know that a Quackable is a Flock to add Quackables to it.

As always, there are tradeoffs when you do OO design and you need to consider them as you create your composites.
