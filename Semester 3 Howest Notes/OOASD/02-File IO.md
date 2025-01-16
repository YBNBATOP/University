Sometimes there is a need to store the data, without allowing it (the data) to be lost on next restart

That is why we can start using logs to save data as log files which we write and read from.

We have some ways to create a file:
- Custom format
Human-readable and eidtable data
Time-consuming and error-prone to implement
Requires writing custom parsing and formatting functions

- Java Serialization
Effortless data storage in Java
Minimal coding required
Not human-readable or easily processed by non-Java application
Tightly coupled to Java, limiting interoperability
Watch out with reading/writting data of old versions

- JSON Serialization
Relatively easy to program using established libraries
Data is readable/writable for informed humans
Interoperable with other programs, including different languages.
Slightly more complex than Java Serialization
Requires library dependencies for serialization/deserialization.

The most basic (but hard) way to implement writting to a file. Imagine having a Map of A date and diagnosis. At that moment we would need to create an interface of PatientLog, then implement a SimplePatientLog (this would be used as a helper class) and PatientLogEntry (this would be used as new values)

# Read/Write text to a cli
For basic input recording we can make use of **Scanner** built-in method. It requires an InputStream.

System.in is a InputStream
System.out is a PrintStream
They are both are IO-streams. They represent the command-line from the System. If we can link them to the data of _a file_ we can replace Standart IO with file IO.

**printf** and **String.format** have a lot of possibilities to actually write strings in different methods. (most of the times they use representations with the %s and other stuff).

# Read/Write text to a file
If you have the proper toString methods, then you can write almost any information to the cli at least.

Afterwards you can create a PrintStream, wrap it with a proper **try/catch** structure.
Also inside of a PrintStream you can include a **FileOutputStream**, so that you can give the name to a file, and also specify whether to override the data, or append data.

Also we would need to wrap a creation of a file into a try/catch structure 2 times.
``` java
private void writeToFile(Course c) {  
    try {  
        try(PrintStream ps = new PrintStream(new FileOutputStream("demo.txt", true))) {  
            ps.println(c);  
        }  
    } catch (FileNotFoundException e) {  
        throw new RuntimeException(e);  
    }  
}
```

# Read/Write objects to file
Instead of actually creating our own formats, we can only use outputting objects to the file and reading it back.

``` java
try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("demo.txt"))) {  
    oos.writeObject(c);  
    //oos.writeObject(c.toFullString());  
} catch (IOException e) {  
    throw new RuntimeException(e);  
}
```

In order to read the file we should do something like:
``` java
private Course readFromFile(String filename) {  
    try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(filename))){  
        System.out.println(ois.readObject());  
        return (Course) ois.readObject();  
    } catch (IOException | ClassNotFoundException e) {  
        Logger.getAnonymousLogger().log(Level.SEVERE, "SOMETHING WRONG" + e);  
        return null;  
    }  
}
```

For reading the files it might be very important to return a class type value,  because then you can assign the values to an empty class and then you will get the values. As well you might try to simply write the output to the CLI.

# Read/Write directories/files
**File** is a wrapper for a path-to-file-or-dir, many/most methods are self explainatory
```java
File f = new File("data.txt");  
if (!f.exists()) {  
	try {  
		boolean success = f.createNewFile();  
	} catch (IOException e) {  
		...  
	}  
}
```
Here it would probably check whether a file exists or not, and if it does not, then it would get created.

If the file is a directory, we can enumerate its contents 
```java
if(d.isDirectory()) {
	File d = new File("./path/with/files");
	for (File f : d.listFiles) {
		//do stuff here
	}
}
```

# Serialize objects to JSON
We can make use of Jackson in order to serialize/deserialize stuff to files

``` java
ObjectMapper json = new ObjectMapper();  
Patient original = new Patient(...);  
String txt = json.writeValueAsString(original);  
Patient deserialized = json.readValue("txt", Patient.class);
```

## Serialize
It uses getters to populate properties (except when annotated with @JsonIgnore)

```java
public class Person() {
	public String getName() {}
	public Calendar getBirthDate() {}
	@JsonIgnore public String getSocialSecurityNumber() {}
	public int computeAge() {}
}
```

It also uses methods/fields annotated with @JsonProperty to populate properties.

``` java
public class Person {
	@JsonProperty("gender") private Gender gender;

	public String getName() {}
	@JsonIgnore public Calendar getBirthDate() {}
	@JsonProperty("age") public int computeAge() {}
}
```

## Deserialize
It uses setters in combination with an empty constructor. As a downside we prefer getters and setters to be as little as possible.

It uses constructor (@JsonCreator) with arguments (@JsonProperty)

```java
@JsonCreator
private Person(
	@JsonProperty("name") String name,
	@JsonProperty("age") int age
) {
	this.name = name;
	this.age = age;
}

// OR

...

) {
	return new Person(name, age);
}
```

