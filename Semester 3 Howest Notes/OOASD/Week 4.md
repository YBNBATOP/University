TIP:
Never Log sensitive data

Do not put sensitive information into the exceptions
# Custom Exceptions
To make an exception of your own, create the package **util** where you actually put the Exception class yourself

```java
public class HospitalException extends RuntimeException {
	public HospitalException(String message) {
		super(message);
	}
}
```

Afterwards you will be able to throw your own exceptions instead of something default
This does a very good job at securing the data

# DatabaseIO (Or database repository)
## Begin
To start with, make sure that you create yourself a package called **data**, and inside there you can already create your own files that are responsible for managing information (storing, receiving)

## Accessing the database
First of all, before actually talking to the database, and manipulating the data inside it, you need to actually create a connection

```java
private static final String URL = "jdbc:mariadb://localhost:3306";
private static final String USR = "root"; //default
private static final String PWD = "root"; //default
Connection connection = DriverManager.getConnection(URL, USR, PWD)
```

The connection might as well throw an exception (SQLException)
So we need to wrap everything in a try-catch

```java
try {
	Connection connection = DriverManager.getConnection(URL, USR, PWD);
	LOGGER.log(Level.INFO, "CONNECTION SUCCESFFULL");
} catch {
	LOGGER.log(Level.WARNING, "FAILED TO LOAD PATIENTS FROM DB", e);
	throw new HospitalException("FAILED TO LOAD PATIENTS");
}
return Collections.emptyList();
```

## What else?
Apart from creating and actual connection, we also need to make sure that we have the suitable drivers for it to work.
That is why we make our way to the **build.gradle.kts**, and then we need to specify dependecies.

For example go and google **gradle mysql java** and then insert the lines with the dependency inside the file

After that - you can finally make a connection to your database

Here you are, you finally created the connection, go ahead and do something more with it

## Creating statements
You create a statement, and then you can actually execute it

```java
Statement statement = connection.createStatement();
statement.executeQuery("SELECT * FROM patients")
```

### Retrieving information
After, for example, a query, we do get the result of the actual information
The return type of all this is a **ResultSet**

So we wrap all of it with the ResultSet
```java
ResultSet rs = statement.executeQuery("SELECT * FROM patients")
```

You literally get all the value like you would do it in datagrip

#### Read information 
When information comes in, it is literally read line by line 
So the pointer by default points to the very top row, then it actually goes down one line at a time (manually)

So you will literally go through the lines and check for the content
```java
if (rs.next()) {
	sout(resultSetToPatient(rs))
}
```

This way you will be able to transform the lines into actual lines for the **cmd** or any other way that you actually want

You can get your information by just accessing the actual labels like:
```java
String name = rs.getString("name")
```
This makes it very easy to actually access attributes

But all this will read only one line
So that lets change it to the actual **while** so that it keeps going while you have your input

Also good idea - if you want to return the value = create an empty list, and then add in there all the information you transformed (i.e. patient in this case)

### Close your stuff
One issue about the resources you open (in this case - the database connection), you need to close it after you make use of it.
The solution for this is easy - try-with-resources
You need to put the resources inside the creation before executing everything else

```java
try (
	Connection connection = DriverManager.getConnection(URL, USR, PWD)
	Statement statment = connection.createStatemenet();
	ResultSet rs = statemenet.executreQuery("SELECT * FROM patients")
)
```
By just doing this, you already get rid of a headache of closing the resources after you opened them.

IMPORTANT NOTE:
It is important not to use the **root** user for accessing the database, but use the other users you create yourself, and granting only the ability to INSERT and SELECT for example (so limit your shit).

## Securing intel
From now, it would be very handy to actually store your information in a special file (in our case - config file)

We create it all in the **resources** file and call it **config.properties**

```java
db.url=blablabla
db.usr=hospital_usr
db.pwd=IamGod123
//no need for quotes
```

To read the actual files:
```java
Properties properties = new Properties();
properties.load(DatabaseIO.class.getResourceAsStream("/config/config.properties")); // it all works like an actual javafx with the loader.
```
And then you can use
```java
Connection connection = DriverManager.getConnection(properties.getProperty("db.url", "db.usr", "db.pwd")
```
This way you are actually creating all the stuff you need

The properties handling should be better put in a separate class called **Config** in a util **package** , which will be responsible for getting ( reading ) properties (load the config file, and give the keys where needed)

Make sure to also cover the case of actually having 2 different instances of a Config class, so that make it **static**! That way everyone will be able to access it

## Config implementations
So that your code stays safe as well as the config files, make sure to have this kind of structure inside your Config class:

```java
public class Config {
	private static final Config instance = new Config();
	public static Config getInstance() {
		return instance
	}
	private Config() {
		try {
			properties = new Properties();
properties.load(Config.class.getResourceAsStream("/config/config.properties")
		}
	}
}
```

By doing everything this way, you will make sure that the actual config file can be created only once, and it will be done by the class itself

It is called a singleton pattern (you make sure there is only one instance of Config class in your whole application)



## Writing data to the database

To store information we will mainly have to do the same thing as when we were retrieving information
We need to open a connection
Then we need to create a statement, and execute an update (it is very important to avoid SQLi, by not using String concatination)
That is why we are going to make use of prepared statements

```java
PreparedStatement statement = connection.prepareStatement("INSERT INTO patients(bla, bla2, bla3) VALUES (?, ?, ?)");

statement.setString(1, person.getName());
statement.setString(2, person.getID());
statement.setString(3, person.getLastName());

statement.executeUpdate
```
Using the method above, you are just inserting the values inside the actual statement
And of course you need to executeUpdate

**IMPORTANT NOTE:**
The statement is the same resource, so make sure to put that in the try-with-resources so that you do not forget to close your resources

But also, it might be very important to get the automatically generated keys from the database
So what we would do is 
```java
PreparedStatement statement = connection.prepareStatement("INSERT INTO patients(bla, bla2, bla3) VALUES (?, ?, ?)", Statement.RETURN_GENERATED_KEYS);
```
This will make sure to bring with it the last generated key

This will also return us an ResultSet
```java
ResultSet rs = statement.getGeneratedKeys();
if(rs.next()) {
	int x = rs.getInt(1);
	return new Patient(new NN(person.getBirthDate(), x), person)
} else {
	throw new HospitalException("ERROR!") //this is essential because if you do not get the generated id, then it means it havent been created actually

```
ResultSet is also a resource, so sometimes we will need to put that in a try with resources by itself

```java
try (ResultSet rs = statement.getGeneratedKeys)
```

## Miscellaneous stuff
It is a good idea to actually encrypt the values of the config file

First thing we do - add the encryption framework as a dependency inside the **build.gradle.kts**

We can use it as this:
```java
TextEncryptor = Encryptors.text("<password>", "<>");
String encrypted = encryptor.encrypt("IamGod123");
sout(encrypted);

String original = encryptor.decrypt(encrypted);
sout(original);
```