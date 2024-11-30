# IO

## Description

This namespace contains classes to perform File I/O operations.

| **Namespace** | **Class**                     |
|---------------|-------------------------------|
| System.IO     | `class File`                  |
| System.IO     | `class DriveInfo`             |
| System.IO     | `class FileStream`            |
| System.IO     | `class Directory`             |
| System.IO     | `class FileNotFoundException` |
| System.IO     | `class StreamWriter`          |
| System.IO     | `class FileInfo`              |
| System.IO     | `class StreamReader`          |
| System.IO     | `class DirectoryInfo`         |
| System.IO     | `class BinaryWriter`          |
| System.IO     | `class BinaryReader`          |

## Classes

### File

- Static class that manipulates file.
- All methods of this class are static methods.
- For doing one action is good but for doing multiple actions at once it's better to use `FileInfo` class

```csharp
System.IO.File.Method();
```

Methods:

| Method                                                                  | Description                                                                                     |
|-------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| `static FileStream Create( string path )`                               | Create / overwrites a file at the specified path.                                               |
| `static bool Exists( string path )`                                     | Determines whether the file exists in the disk or not.                                          |
| `static void Copy( string sourceFile, string destFile )`                | Copies the source file to the destination location.                                             |
| `static void Move( string sourceFile, string destFile )`                | Moves the source file to the destination location.                                              |
| `static void Delete( string path )`                                     | Deletes the specified file permanently.                                                         |
| `static void WriteAllLines( string path, IEnumerable<string> contents)` | Creates / overwrites a file; writes specified lines of content to the file; and close the file. |
| `static string[] ReadAllLines( string path )`                           | Reads file content as text and returns all lines.                                               |
| `static string ReadAllText( string path )`                              | Reads file content as text and returns the same.                                                |
| `static void WriteAllText( string path, string contents )`              | Creates / overwrites a file; writes specified content to the file; and close the file.          |

### FileInfo

- Represents a file and provides methods to manipulate the file.
- For doing multiple actions at onces is good but for doing one action it's better to use File class

```csharp
FileInfo referenceVariable = new FileInfo("Your File Path Here");
```

Properties:

| Property                  | Description                                                           |
|---------------------------|-----------------------------------------------------------------------|
| `bool Exists`             | Determines whether the file exists in the disk or not.                |
| `string FullName`         | Represents full path (including file name and extension) of the file. |
| `string Name`             | Represents only name of the file (without path).                      |
| `string DirectoryName`    | Represents only path of the file (without file name).                 |
| `string Extension`        | Represents only file extension (without file name).                   |
| `DateTime CreationTime`   | Represents date and time of file creation.                            |
| `DateTime LastWriteTime`  | Represents date and time of last modification of the file.            |
| `DateTime LastAccessTime` | Represents date and time of last access of the file.                  |
| `long Length`             | Represents file size (in the form of number of bytes).                |

Methods:

| Method                                                 | Description                                                                                                         |
|--------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| `FileInfo CopyTo(string destFilePath, bool overwrite)` | Copies the file into the new destination path. It returns an object of `FileInfo` class, representing the new file. |
| `void MoveTo(string destFilePath)`                     | Moves the file into the new destination path (must be in the same drive).                                           |
| `void Delete()`                                        | Deletes the file permanently.                                                                                       |
| `FileStream Create()`                                  | Creates the file at the specified path and returns an object of `FileStream` with 'Create' mode to write data.      |
| `FileStream Open(FileMode mode, FileAccess access)`    | Opens the file with the specified mode and access, returns a `FileStream` object that can write/read file data.     |
| `FileStream OpenRead()`                                | Opens the file in 'Read' mode and returns a `FileStream` object that can read the file data.                        |
| `FileStream OpenWrite()`                               | Opens the file in 'OpenOrCreate' mode and returns a `FileStream` object to write the file data.                     |
| `StreamWriter CreateText()`                            | Opens the file in 'Create' mode and returns a `StreamWriter` object to write text to the file.                      |
| `StreamWriter AppendText()`                            | Opens the file in 'Append' mode and returns a `StreamWriter` object to write appended text to the file.             |
| `StreamReader OpenText()`                              | Opens the file in 'Open' mode and returns a `StreamReader` object that can read text from the file.                 |

### Directory

- Static class that manipulates directory (folder).
- All methods of this class are static methods.

```csharp
System.IO.Directory.Method();
```

Methods:

| Method                                                              | Description                                                                                                                        |
|---------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| `static DirectoryInfo CreateDirectory(string path)`                 | Create a directory at the specified path.                                                                                          |
| `static void Delete(string path, bool recursive)`                   | **true**: Deletes the directory including subdirectories and all files. <br> **false**: Deletes the directory only if it is empty. |
| `static bool Exists(string path)`                                   | Determines whether the directory exists in the disk or not.                                                                        |
| `static string[] GetDirectories(string path)`                       | Returns string[] that contains paths of subdirectories in the specified directory.                                                 |
| `static string[] GetDirectories(string path, string searchPattern)` | Returns string[] that contains paths of subdirectories that match the specified search pattern.                                    |
| `static string[] GetFiles(string path)`                             | Returns string[] that contains paths of files in the specified directory.                                                          |
| `static string[] GetFiles(string path, string searchPattern)`       | Returns string[] that contains paths of files that match the specified search pattern.                                             |
| `static void Move(string sourceDir, string destDir)`                | Moves the source directory to the specified destination location in the same drive.                                                |

### DirectoryInfo

Class that represents a directory (folder) on the disk and performs manipulations on directories.

```csharp
DirectoryInfo referenceVariable = new DirectoryInfo("Directory Path Here");
```

Properties:

| Property                  | Description                                                     |
|---------------------------|-----------------------------------------------------------------|
| `bool Exists`             | Determines whether the directory exists in the disk or not.     |
| `string FullName`         | Represents full path of the directory.                          |
| `string Name`             | Represents only name of the directory (without path).           |
| `DirectoryInfo Parent`    | Represents parent directory of the current directory.           |
| `DirectoryInfo Root`      | Represents root (drive) of the directory.                       |
| `DateTime CreationTime`   | Represents date and time of directory creation.                 |
| `DateTime LastWriteTime`  | Represents date and time of last modification of the directory. |
| `DateTime LastAccessTime` | Represents date and time of last access of the directory.       |

Methods:

| Method                                                      | Description                                                                                         |
|-------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| `void Create()`                                             | Create the directory at the current path.                                                           |
| `DirectoryInfo CreateSubDirectory(string path)`             | Creates a sub directory at the current path with specified name.                                    |
| `void Delete(bool recursive)`                               | `true`: Deletes the directory including sub directories. `false`: Deletes directory only if empty.  |
| `DirectoryInfo[] GetDirectories()`                          | Returns `DirectoryInfo[]` that represents sub directories of current directory.                     |
| `DirectoryInfo[] GetDirectories(string searchPattern)`      | Returns `DirectoryInfo[]` that represents sub directories that match with specified search pattern. |
| `FileInfo[] GetFiles()`                                     | Returns `FileInfo[]` that represents files of current directory.                                    |
| `FileInfo[] GetFiles(string searchPattern)`                 | Returns `FileInfo[]` that represents files that match with specified search pattern.                |
| `void MoveTo(string destDirName)`                           | Moves the current directory to the specified location in the same drive.                            |

### DriveInfo

- Class that represents a drive and performs manipulations on drives.
- You can read both fixed / removable drives.

```csharp
DriveInfo referenceVariable = new DriveInfo("Your Drive Name Here");
```

Properties:

| Property                      | Description                                             |
|-------------------------------|---------------------------------------------------------|
| `string Name`                 | Represents name of the drive.                           |
| `string DriveType`            | Represents type of drive either 'Fixed' or 'Removable'. |
| `string VolumeLabel`          | Represents label of the drive (set by user).            |
| `DirectoryInfo RootDirectory` | Represents root directory of the drive.                 |
| `long TotalSize`              | Represents total size (bytes) of the drive.             |
| `long AvailableFreeSpace`     | Represents total free space (bytes) of the drive.       |

### FileStream

- Class that performs file I/O operations.
- Writes / reads data in byte[ ] format.
- For multiple file operation on one single file, this class is good, but for single operation like only read or only write the StreamReader and StreamWriter classes are better

```csharp
FileStream referenceVariable = new FileStream( "File Path", FileMode.Create, FileAccess.Write );
```

Example:

```csharp
// => FileStream for Writing
FileStream fileStream = new FileStream(filePath, FileMode.Create, FileAccess.Write);
//FileStream fileStream = File.Create(filePath);
//FileStream fileStream = File.Open(filePath, FileMode.Create, FileAccess.Write);
//FileStream fileStream = File.OpenWrite(filePath);
//FileStream fileStream = fileInfo.Create();
//FileStream fileStream = fileInfo.Open(FileMode.CreateNew, FileAccess.Write);
//FileStream fileStream = fileInfo.OpenWrite();

// => FileStream for Reading
FileStream fileStream2 = new FileStream(filePath, FileMode.OpenOrCreate, FileAccess.Read);
//FileStream fileStream2 = File.Open(filePath, FileMode.OpenOrCreate, FileAccess.Read);
//FileStream fileStream2 = File.OpenRead(filePath);
//FileStream fileStream2 = fileInfo.Open(FileMode.OpenOrCreate, FileAccess.Read);
//FileStream fileStream2 = fileInfo.OpenRead();

// => Creating and Writing to a File
// Create content
string content = "Dog is one of the domestic animal";
byte[] bytes = System.Text.Encoding.ASCII.GetBytes(content);

// Write
fileStream.Write(bytes, 0, bytes.Length);
fileStream.Close();
```

Methods:

| Method                                            | Description                                                                                                                                                 |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `void Write(byte[] array, int offset, int count)` | Writes the specified no. of bytes specified by count, based on the byte[] specified by 'array' into the file, after the no. of bytes specified by 'offset'. |
| `int Read(byte[] array, int offset, int count)`   | Reads the specified no. of bytes specified by count, into the byte[] specified by 'array' from the file, after the no. of bytes specified by 'offset'.      |
| `void Close()`                                    | Closes the file.                                                                                                                                            |

FileMode:

| Mode                    | Description                                                                                                                                                      |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `FileMode.CreateNew`    | It specifies that the o/s should create a new file. If the file already exists, an IOException will be thrown.                                                   |
| `FileMode.Create`       | It specifies that the o/s should create a new file. If the file already exists, it will be overwritten.                                                          |
| `FileMode.Open`         | It specifies that the o/s should open an existing file. If the file doesn't exist, a FileNotFoundException will be thrown.                                       |
| `FileMode.OpenOrCreate` | It specifies that the o/s should open an existing file. If the file doesn't exist, a new file will be created. It is useful for reading content of the file.     |
| `FileMode.Append`       | It specifies that the o/s should open an existing file and seek to the end of the file in order to write content at the end. It is useful with FileAccess.Write. |

FileAccess:

| Mode                   | Description                                              |
|------------------------|----------------------------------------------------------|
| `FileAccess.Read`      | It is used to read content from an existing file.        |
| `FileAccess.Write`     | It is used to write content to a file.                   |
| `FileAccess.ReadWrite` | It can be used for both read/write operations in a file. |

### StreamWriter

- Class that writes text data into the file.
- Internally uses FileStream.
- Is a wrapper around the FileStream for writing strings

```csharp
StreamWriter referenceVariable = new StreamWriter("File Path");
```

Example:

```csharp
// 4 ways to create new object of StreamWriter
// StreamWriter streamWriter = new StreamWriter(filePath);
// StreamWriter streamWriter = new StreamWriter(fileStream);
// StreamWriter streamWriter = fileInfo.AppendText();
using (StreamWriter streamWriter = fileInfo.CreateText()) {
    streamWriter.WriteLine("Russia has population about 145,934,000");

    // some code here

    streamWriter.WriteLine("Germany has population about 83,783,000");
}
```

Methods:

| Method                       | Description                                      |
|------------------------------|--------------------------------------------------|
| `void Write(string content)` | Writes the specified string content to the file. |
| `void Close()`               | Close the file.                                  |

### StreamReader

- Class that reads text data from the file.
- Internally uses `FileStream`.
- Is a wrapper around the FileStream for reading strings

```csharp
StreamReader referenceVariable = new StreamReader("File Path");
```

Example:

```csharp
// 3 ways to create object of StreamReader:
// StreamReader streamReader = new StreamReader(filePath);
// StreamReader streamReader = fileInfo.OpenText();

FileStream fileStream2 = new FileStream(filePath, FileMode.Open, FileAccess.Read);
using (StreamReader streamReader = new StreamReader(fileStream2)) {
    string content_from_file = streamReader.ReadToEnd();
    Console.WriteLine("\nFile read. File content is:");
    Console.WriteLine(content_from_file);
}
```

Methods:

| Method                                               | Description                                                                                                                                                                |
|------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `int Read(char[] buffer, int startIndex, int count)` | Reads the specified number of characters (using 'count') from the file into the specified buffer (char[]) and inserts the characters at the specified index of the buffer. |
| `string ReadToEnd()`                                 | Reads complete content of the file in text format and returns the same as a string.                                                                                        |
| `string ReadLine()`                                  | Reads a line from the file in text format and returns the same as a string.                                                                                                |
| `void Close()`                                       | Closes the file.                                                                                                                                                           |

### BinaryWriter

- Class that writes binary data into the file.
- Internally uses `FileStream`.
- For example, 65 is written as `1000001`.

```cs
BinaryWriter referenceVariable = new BinaryWriter(fileStream);
```

Methods:

| Method            | Description                                                             |
|-------------------|-------------------------------------------------------------------------|
| `void Write(...)` | Writes any type of value (only primitive types / string) into the file. |
| `void Close()`    | Close the file.                                                         |

### BinaryReader

- Class that reads binary data from the file.
- Internally uses FileStream.

```csharp
BinaryReader referenceVariable = new BinaryReader(fileStream);
```

Methods:

| Method                                                                                                                                                                                                     | Description                                                 |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| `ReadByte()`                                                                                                                                                                                               | Reads and returns a byte value from the file.               |
| `ReadSByte(),` `ReadInt16(),` `ReadUInt16(),` `ReadInt32(),` `ReadUInt32(),` `ReadInt64(),` `ReadUInt64(),` `ReadSingle(),` `ReadDouble(),` `ReadDecimal(),` `ReadChar(),` `ReadString(),` `ReadBoolean()` | Reads and returns the specific type of value from the file. |
| `Close()`                                                                                                                                                                                                  | Closes the file.                                            |
