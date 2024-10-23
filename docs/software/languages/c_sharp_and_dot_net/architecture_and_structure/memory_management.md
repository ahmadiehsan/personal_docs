# Memory Management

## Schema

<img src="image5.jpg" style="width:4in" />

## Stack

- Part of ram
- Very fast
- Last in, first out
- All the local variables will store in here
- Reference of one obj will store here

## Heap (a.k.a Virtual Memory)

Key Points:

- Part of ram
- Slower than stack
- All the objects will store here
- Has 64 MB space

Generation:

Heap contains three segments (called generations):

- Generation 2 (Long-Lived Generation)
- Generation 1 (Survival Generation)
- Generation 0 (Short-Lived Generation)

!!! info

    <span dir="rtl">اول موقع ساخت object اون آبجکت داخل G0 ساخته میشه، بعد از یه مدتی منتقل میشه به G1 و بعدش هم به G2</span>

- The **"Generation 0"** is the youngest generation and contains newly created short-lived objects and collected at first priority. The objects survive longer, are promoted to **"Generation 1"**.
- The **"Generation 1"** is buffer between **"Generation 0"** and **"Generation 2"**.

   - The **"Generation 1"** mainly contains frequently-used and longer-lived objects.
   - **Ex**: The objects created in the previously-executed methods, but still accessible.

- The **"Generation 2"** contains the longest-lived objects that were created long-back and still is being used, by different statements in the program.

## Garbage Collector (GC)

Description:

- CLR automatically allocates memory for all objects created anywhere in the application, whenever it encounters "new ClassName( )" statement. This process is called as "Memory Management", which is done by "Memory Manager" component of CLR.
- All objects are stored in "Heap" (a.k.a. virtual memory).
- Heap is only-one for the entire application life time.
- The default heap size 64 MB (approx.), and extendable.
- When CLR can't find space for storing new objects, it performs a process called "Garbage Collection" automatically, which includes "identification of un-referenced objects and deleting them from heap; so that making room for new objects". This process is done by "Garbage Collector (GC)" component of CLR.

When GC gets triggered?

- There are **NO** specific timings for GC to get triggered.
- GC automatically gets triggered in the following conditions:

   - When the "heap" is full or free space is too low.
   - When we call `GC.Collect()` explicitly.

Tips:

- All objects are created based on classes; stored in 'heap'.
- For each application execution, a new heap will be created (and only one).
- All reference variables (local variables of methods) are stored in stack. For each method call, a new stack will be created.

## Managed vs Unmanaged Resources

| **Unmanaged Resources**                                                                             | **Managed Resources**                                                                      |
|-----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| The objects that are not created by CLR and not managed by CLR are called as "Unmanaged Resources". | The objects that are created by CLR are called as "Managed Resources".                     |
| **Ex:** File streams, database connections.                                                         | These will participate in "Garbage Collection" process, which is a part of .NET Framework. |
