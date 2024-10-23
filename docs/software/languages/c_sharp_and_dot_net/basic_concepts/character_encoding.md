# Character Encoding

## Description

It is a concept that tells you represent characters into numbers (or any specific format).

| ASCII                                                                            | UTF-16 / Unicode                                                    |
|----------------------------------------------------------------------------------|---------------------------------------------------------------------|
| American Standard Code for Information Interchange                               | Universal Code                                                      |
| Each character occupies 7 bits (generally considered as 1 byte)                  | Each character occupies 2 or 4 bytes (generally considered as 2 bytes) |
| 128 characters (0 to 127)                                                        | About 144697 characters (approx)                                    |
| Includes all keyboard characters with alphabets, digits, special characters etc. | Includes all natural language characters along with ASCII.          |

- Each Unicode has its hexadecimal unique number
- The U+ before each Unicode is the hexadecimal identifier
- In C# the \\u prefix means Unicode

```csharp
string sentence = "The quick brown fox jumps over the lazy dog";
byte[] bytes = System.Text.Encoding.Unicode.GetBytes(sentence);
string sentence2 = System.Text.Encoding.Unicode.GetString(bytes);
```

## Popular Encodings

ASCII table:

| Decimal | Hex | Char                   |
|---------|-----|------------------------|
| 0       | 00  | [NULL]                 |
| 1       | 01  | [START OF HEADING]     |
| 2       | 02  | [START OF TEXT]        |
| 3       | 03  | [END OF TEXT]          |
| 4       | 04  | [END OF TRANSMISSION]  |
| 5       | 05  | [ENQUIRY]              |
| 6       | 06  | [ACKNOWLEDGE]          |
| 7       | 07  | [BELL]                 |
| 8       | 08  | [BACKSPACE]            |
| 9       | 09  | [HORIZONTAL TAB]       |
| 10      | 0A  | [LINE FEED]            |
| 11      | 0B  | [VERTICAL TAB]         |
| 12      | 0C  | [FORM FEED]            |
| 13      | 0D  | [CARRIAGE RETURN]      |
| 14      | 0E  | [SHIFT OUT]            |
| 15      | 0F  | [SHIFT IN]             |
| 16      | 10  | [DATA LINK ESCAPE]     |
| 17      | 11  | [DEVICE CONTROL 1]     |
| 18      | 12  | [DEVICE CONTROL 2]     |
| 19      | 13  | [DEVICE CONTROL 3]     |
| 20      | 14  | [DEVICE CONTROL 4]     |
| 21      | 15  | [NEGATIVE ACKNOWLEDGE] |
| 22      | 16  | [SYNCHRONOUS IDLE]     |
| 23      | 17  | [END OF TRANS. BLOCK]  |
| 24      | 18  | [CANCEL]               |
| 25      | 19  | [END OF MEDIUM]        |
| 26      | 1A  | [SUBSTITUTE]           |
| 27      | 1B  | [ESCAPE]               |
| 28      | 1C  | [FILE SEPARATOR]       |
| 29      | 1D  | [GROUP SEPARATOR]      |
| 30      | 1E  | [RECORD SEPARATOR]     |
| 31      | 1F  | [UNIT SEPARATOR]       |
| 32      | 20  | [SPACE]                |
| 33      | 21  | !                      |
| 34      | 22  | "                      |
| 35      | 23  | #                      |
| 36      | 24  | $                      |
| 37      | 25  | %                      |
| 38      | 26  | &                      |
| 39      | 27  | '                      |
| 40      | 28  | (                      |
| 41      | 29  | )                      |
| 42      | 2A  | *                      |
| 43      | 2B  | +                      |
| 44      | 2C  | ,                      |
| 45      | 2D  | -                      |
| 46      | 2E  | .                      |
| 47      | 2F  | /                      |
| 48      | 30  | 0                      |
| 49      | 31  | 1                      |
| 50      | 32  | 2                      |
| 51      | 33  | 3                      |
| 52      | 34  | 4                      |
| 53      | 35  | 5                      |
| 54      | 36  | 6                      |
| 55      | 37  | 7                      |
| 56      | 38  | 8                      |
| 57      | 39  | 9                      |
| 58      | 3A  | :                      |
| 59      | 3B  | ;                      |
| 60      | 3C  | <                      |
| 61      | 3D  | =                      |
| 62      | 3E  | >                      |
| 63      | 3F  | ?                      |
| 64      | 40  | @                      |
| 65      | 41  | A                      |
| 66      | 42  | B                      |
| 67      | 43  | C                      |
| 68      | 44  | D                      |
| 69      | 45  | E                      |
| 70      | 46  | F                      |
| 71      | 47  | G                      |
| 72      | 48  | H                      |
| 73      | 49  | I                      |
| 74      | 4A  | J                      |
| 75      | 4B  | K                      |
| 76      | 4C  | L                      |
| 77      | 4D  | M                      |
| 78      | 4E  | N                      |
| 79      | 4F  | O                      |
| 80      | 50  | P                      |
| 81      | 51  | Q                      |
| 82      | 52  | R                      |
| 83      | 53  | S                      |
| 84      | 54  | T                      |
| 85      | 55  | U                      |
| 86      | 56  | V                      |
| 87      | 57  | W                      |
| 88      | 58  | X                      |
| 89      | 59  | Y                      |
| 90      | 5A  | Z                      |
| 91      | 5B  | [                      |
| 92      | 5C  | \                      |
| 93      | 5D  | ]                      |
| 94      | 5E  | ^                      |
| 95      | 5F  | _                      |
| 96      | 60  | \`                     |
| 97      | 61  | a                      |
| 98      | 62  | b                      |
| 99      | 63  | c                      |
| 100     | 64  | d                      |
| 101     | 65  | e                      |
| 102     | 66  | f                      |
| 103     | 67  | g                      |
| 104     | 68  | h                      |
| 105     | 69  | i                      |
| 106     | 6A  | j                      |
| 107     | 6B  | k                      |
| 108     | 6C  | l                      |
| 109     | 6D  | m                      |
| 110     | 6E  | n                      |
| 111     | 6F  | o                      |
| 112     | 70  | p                      |
| 113     | 71  | q                      |
| 114     | 72  | r                      |
| 115     | 73  | s                      |
| 116     | 74  | t                      |
| 117     | 75  | u                      |
| 118     | 76  | v                      |
| 119     | 77  | w                      |
| 120     | 78  | x                      |
| 121     | 79  | y                      |
| 122     | 7A  | z                      |
| 123     | 7B  | {                      |
| 124     | 7C  | [pipeline]             |
| 125     | 7D  | }                      |
| 126     | 7E  | ~                      |
| 127     | 7F  | [DEL]                  |

Unicode table:

[Link](https://en.m.wikipedia.org/wiki/List_of_Unicode_characters)
