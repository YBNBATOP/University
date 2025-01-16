# Custom Exceptions
## Why we need them?
One of the problems might be exposing sensitive data throught the exceptions (ex. try to load a file that does not exist)
Such things at first can be solved by creating a logger.

## Create a new one instead of throwing a generic one
Sometimes we can not throw a generic exception, so that we need to create our own class (usually in the /util package), that will be built upon a exception.
```java
public class InsufficientFundsException extends RuntimeException {  
	public InsufficientFundsException() {  
		super();  
	}  
	public InsufficientFundsException(String message) {  
		super(message);  
	}  
	public InsufficientFundsException(String message, Throwable cause) {  
		super(message, cause);  
	}  
}
```

By doing such manipulations you actually hide sensitive data from the exceptions (unless you log everything and then you can have it for yourself).
# JDBC
## Why Database?
Sometimes you can either use the files (which we used to have and write to), or we can start storing information inside the actual database.

## How do we do it?
We would first create a database, and ditch the files we used to read from.
We would need to create a Java Class that would actually be responsible for our databases manipulation (in our case we would use /data package)

## What next?
We need to connect to the database!

```java
private static final STRING URL = "jdbc:mysql//localhost:3306/hospital2324";
private static final STRING USR = "root";
private static final STRING PWD = "dsadasdadwadwsdwadw";

Connection connection = DriverManager.getConnection(URL, USR, PWD)
```
We should use **DataGrip** to actually get to use the database and create them.

Sometimes there is a need to wrap the connection establishment in a try-catch
And of course throw our **own** exception.
The additional information in this case should be better thrown by the Logger!

**IMPORTANT**: We would need to implement the dependencies in the plugins of **build.gradle.kts** file

## I want to get information
Then you would want to actually get information from the database
We create a statement, and then a query
When we get the information, it comes in a **ResultSet**. Afterwards we can furtherly manipulate the data we get.

## How exactly?
We convert from SQL convention to Java, so out of the ResultSet we get, we then can start getting more information

```java
while(rs.next()) {
	String name - rs.getString("name") //here you can specify what kind of data you want
	LOGGER.log(Level.INFO, name);
}
```

By doing this you literally get through all of lines and read the data you need!

## Why leave open?
After we actually open our connection, and do our stuff, then we also need to CLOSE the resources
Results, statements, connections, all of them should get closed!
This can be done by implementing a try-catch with resources.

```java
try (our stuuff) {

} catch (ex e) {

}
```

This will ensure that the resources are closed after we actually opened and worked.

**IMPORTANT**: It is very important to not store any data inside the actual classes (like passwords and stuff), also the user we are using should not have too high privileges, we only need like to access one database, and maybe INSERT, SELECT data.

By doing all this, your program and code becomes more secure.
# Configuration Files
## Why store information in config files
We usually need to store some information outside of a class, so that we can then use it in our full project!

## How do I do that?
We create a **config.properties** in the **/resources** directory.
We set up information like:
```java
db.pwd=YES
```
Everything is stored as strings

## How do I access that information
We would need to actually load the properties.
From there we can access the information itself.

It might be also handy to actually create your own Config class that can do more sutff.

**IMPORTANT**: When creating actual information about the properties, we then need to actually make sure we do not overload our system. We would want to create only one instance of the properties.
We would actually configure our class in such a way, so that we would have a **static** over all the program.

# Improvement
Sometimes we also want to make sure that we can do more stuff, such as inserting information in the database.

# How do I add data
Of course we need to open a connection
Then we would again need to execute a query

**IMPORTANT**: Never use string concatination, because otherwise you just put in dangerous SQL Injection. This is why we use **statement.prepareStatement**, as a prepared statement. Instead of the values, you need to actually put **?**, so that then you work with it like a string.format function.

Also, it should be important to secure your config file with encryption (add a plugin for that!)