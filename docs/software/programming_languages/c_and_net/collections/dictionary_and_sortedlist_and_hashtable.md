# Dictionary & SortedList & Hashtable

## Dictionary

Syntax:

![](dictionary_and_sortedlist_and_hashtable/image9.jpg)

<img src="image26.jpg" style="width:3.70417in" />

<img src="image19.jpg" style="width:3.08333in" />

Description:

<img src="image14.jpg" style="width:4.88333in" />

![](dictionary_and_sortedlist_and_hashtable/image5.jpg)

Features:

Overview:

![](dictionary_and_sortedlist_and_hashtable/image27.jpg)

- All of the shared features can be used for the Dictionary

## SortedList

Syntax:

![](dictionary_and_sortedlist_and_hashtable/image8.jpg)

Description:

<img src="image13.jpg" style="width:4.88333in" />

![](dictionary_and_sortedlist_and_hashtable/image17.jpg)

- Will use BinarySearch in the background

Features:

Overview:

![](dictionary_and_sortedlist_and_hashtable/image11.jpg)

- All of the shared features can be used for the SortedList
- The below features are specific to the SortedList

IndexOfKey:

<img src="image2.jpg" style="width:2.4625in" />

IndexOfValue:

<img src="image4.jpg" style="width:2.55in" />

vs Dictionary:

- Dictionary: fast insert, slow search
- SortedList: slow insert, fast search
- Dictionary will use linear search for finding key
- SortedList will sort the keys after each new insert

## Hashtable

Syntax:

<img src="image23.jpg" style="width:4.67083in" />

<img src="image20.jpg" style="width:2.425in" />

<img src="image22.jpg" style="width:2.95833in" />

Description:

<img src="image18.jpg" style="width:3.17917in" />

<img src="image15.jpg" style="width:3.90833in" />

- GetHashCode method of the key value will be used in the index calculation process
- when we want to using the objs of our custom class as the key inside a hashtable, we should implement the GetHashCode method of that class
- Elements with the same calculated index will be stored in the same index with the linked list data structure
- Each time, when the size of hashtable changes, all of the exists indexes will calculated automaticaly

Features:

Overview:

![](dictionary_and_sortedlist_and_hashtable/image12.jpg)

Type Conversion:

- Hashtable will return System.Object instance, becuse we can store any type of data in hashtables
- After retriving data from hashtable (with \[TKey\] or foreach loop), we should covert the result

vs SortedList:

- Hashtable O(1) is faster than SortedList O(log n) in retiriving data
- Both of them have cost in data insert

![](dictionary_and_sortedlist_and_hashtable/image1.jpg)

## Shared Features

\[TKey\]:

<img src="image10.jpg" style="width:2.375in" />

Keys:

<img src="image24.jpg" style="width:2.2125in" />

Values:

<img src="image6.jpg" style="width:2.4625in" />

Add:

<img src="image7.jpg" style="width:1.75417in" />

Remove:

<img src="image25.jpg" style="width:1.4625in" />

ContainsKey:

<img src="image16.jpg" style="width:2.2375in" />

ContainsValue:

<img src="image21.jpg" style="width:2.52083in" />

Clear:

<img src="image3.jpg" style="width:1.18333in" />
