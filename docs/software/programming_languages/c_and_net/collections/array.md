# Array

## Description

![](array/image23.jpg)

## Key Points

![](array/image27.jpg)

- By default, all of the array elements will store by their default value (int: 0, bool: false, string and other obj: null)
- Arrays will store the reference of objects not the actual object
- Arrays are object, so their elements (regardless of being primitive or non-primitive) will store in heap

## Array Initializer

<img src="image8.jpg" style="width:4.83333in" />

## Nested Arrays

### Multidimensional Array

![](array/image30.jpg)

- Childe arrays should be the same size

<img src="image9.jpg" style="width:1.44167in" />

### Jagged Arrays

![](array/image17.jpg)

<img src="image6.jpg" style="width:3.37083in" />

## System.Array

### Features

<img src="image14.jpg" style="width:2.71439in" />

- All of the arrays internally will convert into this class

### IndexOf

<img src="image22.jpg" style="width:4.92917in" />

<img src="image24.jpg" style="width:2.53302in" />

![](array/image21.jpg)

<img src="image15.jpg" style="width:3.80521in" />

### BinarySearch

<img src="image25.jpg" style="width:5.2875in" />

<img src="image1.jpg" style="width:2.62719in" />

![](array/image13.jpg)

### Clear

<img src="image28.jpg" style="width:5.7875in" />

<img src="image2.jpg" style="width:2.46633in" />

![](array/image12.jpg)

### Resize

<img src="image20.jpg" style="width:5.41667in" />

![](array/image4.jpg)

- In case of increase, the new elements will fill with the type default value
- Actually, this method will create a new array and will copy the elements into the new one

### Sort

<img src="image10.jpg" style="width:4.35417in" />

- By default will sort the array in ascending order

### Reverse

<img src="image18.jpg" style="width:4.58333in" />

- For sorting an array in descending order, first we should use sort method and then passing the result into this method

### IndexFromEnd and Range Operator

![](array/image16.jpg)

<img src="image5.jpg" style="width:3.12917in" />

## Copy One Array

### Shallow (CopyTo & Clone)

![](array/image19.jpg)

<img src="image26.jpg" style="width:3.36661in" />

![](array/image7.jpg)

### Deep

There isn’t any specific way for deep copy in .NET but we can write the deep clone behaviour with ICloneable like the below:

![](array/image3.jpg)

<img src="image11.jpg" style="width:2.9875in" />

## Anonymous Array

![](array/image29.jpg)
