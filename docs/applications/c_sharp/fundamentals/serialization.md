# Serialization

## BinaryFormatter

Class that serializes (converts) an object-state into binary format and stores in binary file.

- Serialization is a process of converting an object from one format to another format.
- It can also read existing object-state from the binary file.
- Full path: `System.Runtime.Serialization.Formatters.Binary.BinaryFormatter`

```csharp
BinaryFormatter referenceVariable = new BinaryFormatter();
```

Example:

```csharp
[Serializable]
public class Country {
    public short CountryID { get; set; }
    public string CountryName { get; set; }
    public long Population { get; set; }
    public string Region { get; set; }
}

// create object
Country country = new Country()
{
    CountryID = 1,
    CountryName = "Russia",
    Population = 145934000,
    Region = "Eastern Europe"
};

// create FileStream
string filePath = @"c:\practice\russia.txt";
FileStream fileStream = new FileStream(filePath, FileMode.Create, FileAccess.Write);

// create BinaryFormatter
BinaryFormatter binaryFormatter = new BinaryFormatter();
binaryFormatter.Serialize(fileStream, country);
fileStream.Close();

// Code for deserialization
FileStream fileStream2 = new FileStream(filePath, FileMode.Open, FileAccess.Read);
Country country_from_file = (Country)binaryFormatter.Deserialize(fileStream2);
```

Methods:

| Method             | Description                                                                                              |
|--------------------|----------------------------------------------------------------------------------------------------------|
| `Serialize(...)`   | Converts the object-state into the binary file, using the specified FileStream (with Write access).      |
| `Deserialize(...)` | Reads the existing object-state from the binary file, using the specified FileStream (with Read access). |

## JsonSerializer

A flexible static class for serializing objects and deserializing jsons

Methods:

`Serialize(...)`:

```csharp
string jsonString = JsonSerializer.Serialize(weatherForecast);
```

```csharp
string fileName = "WeatherForecast.json";
string jsonString = JsonSerializer.Serialize(weatherForecast);
File.WriteAllText(fileName, jsonString);
```

```csharp
string fileName = "WeatherForecast.json";
using FileStream createStream = File.Create(fileName);
await JsonSerializer.SerializeAsync(createStream, weatherForecast);
await createStream.DisposeAsync();

var options = new JsonSerializerOptions { WriteIndented = true };
string jsonString = JsonSerializer.Serialize(weatherForecast, options);
```

`Deserialize(...)`:

```csharp
WeatherForecast? weatherForecast = JsonSerializer.Deserialize<WeatherForecast>(jsonString);
```

```csharp
string fileName = "WeatherForecast.json";
using FileStream openStream = File.OpenRead(fileName);
WeatherForecast? weatherForecast = await JsonSerializer.DeserializeAsync<WeatherForecast>(openStream);
```

## JavaScriptSerializer (JSON for .NET Framework)

Class that serializes (converts) an object-state into JSON format.

- It can also convert JSON data into an object of any class.
- Full path: `System.Web.Script.Serialization.JavaScriptSerializer`

Example:

```csharp
// create object of JavaScriptSerializer
JavaScriptSerializer javaScriptSerializer = new JavaScriptSerializer();
string filePath = @"c:\practice\customer.txt";
StreamWriter streamWriter = new StreamWriter(filePath);

// Serialize
string json = javaScriptSerializer.Serialize(customer);
streamWriter.WriteLine(json);
streamWriter.Close();
Console.WriteLine("Serialized");

// Deserialize
StreamReader streamReader = new StreamReader(filePath);
Customer customer_from_file = javaScriptSerializer.Deserialize(streamReader.ReadToEnd(), typeof(Customer)) as Customer;
```

Methods:

| Task               | Code Example                                                              |
|--------------------|---------------------------------------------------------------------------|
| `Serialize(...)`   | `javaScriptSerializer.Serialize( YourObject )`                            |
| `Deserialize(...)` | `javaScriptSerializer.Deserialize( string jsonData, typeof(ClassName) )`  |

## XmlSerializer

Class that serializes (converts) an object-state into XML format and stores in XML file.

- It can also read existing object-state from the XML file.
- Full path: `System.Xml.Serialization.XmlSerializer`

```csharp
XmlSerializer referenceVariable = new XmlSerializer( typeof(ClassName) );
```

Methods:

| Method             | Description                                                                                           |
|--------------------|-------------------------------------------------------------------------------------------------------|
| `Serialize(...)`   | Converts the object-state into the XML file, using the specified FileStream (with Write access).      |
| `Deserialize(...)` | Reads the existing object-state from the XML file, using the specified FileStream (with Read access). |
