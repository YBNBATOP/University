# Recap Object Orientation

### Classes
Classes can have:
- Fields (states)
- Methods (behaviour)
- They start with a capital letter

### Objects 
Objects are instances of classes
Like:

``` java
Cat c = new Cat("Garfield");
System.out.println(c.getName());

c.eat();
c.sleep();
```
### Fields and Properties: getters and setters
A getter is a method that returns the value of a field.
A setter is a method that updates the value of a field.
Getters/Setters should be written only for necessary fields.

``` java
class TimeOfDay {
	private int hours;

	public int getHours() { return hours;} // getter

	public void setHours(int newHours) { // setter
		if(newHours >= 0 && newHours <= 24) {// protect local state from invalid data
			hours = newHours;
		}
	}
}
```

### Constructors
They are special methods
They are called when creating (constructing) an object
Don't forget about Constructor Chaining (using a more basic constructor and building something more upon it), Copy Constructors (that create instances of the same objects, or same values).

### Interfaces
Different use cases:
- For example, a printer driver for macOS, Windows and Linux
- Should support same behaviour, but implemented differently

``` java
public interface Printable {  
	void print(Printer prn);  
}  
public class Page implements Printable {  
@Overrides  
public void print(Printer prn) {  
	prn.enqueue(getContents());  
}  
}
```



### Equality and comparison
Don't forget:
- Java Strings: compare using **.equals** method
- Do not use ==
- Implementing **equals** and **hashCode** methods
- Comparing objects: make a class Foo implement Comparable<>of the same class -> compareTo method

### Collections
Don't forget about:
- List
- Map
- Set
their properties and their implementations





### Exceptions (and using them in testing)
- When things could go wrong
- Catch the exception that gets thrown

``` java
try {
	//some code
} catch (ExceptionType1 | ExceptionType 2 ex) {
	//handle the exception
}
```
- Throwing IllegalArgumentException or IllegalStateException (basic ones)
- Later: our own exceptions


### Enums

``` java
public Enum Weekday {
	MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY;
}
```
You can compare enum instances using ==
Using switch-case is also allowed




### Static
- Static fields:
>When the value is independent of objects

>When the value is supposed to be shared across all objects

- Static methods:
>To access/manipulate static variables and other static methods that don't depend upon objects

>Static methods are widely used in utility and helper classes

>To create (a collection) of instances of the class: e.g. createDeck in the class Card (factory method)



### Final
- Use the **final** keyword to make variables final
- A final variable: cannot be reassigned
Must have an initial value:
- Parameters: when method is called;
- Local variables: when declared;
- Fields: either in declaration or in constructor;
**Rule of Thumb**: make your fields final when possible!
**Attention**: final collections -> cannot be reassigned, but you can modify the contents (inside) of the collection. 



### Packages
Convention: reverse domain names
Example: **be.ti.howest.ooasd.helloworld**
Don't forget about packages and visibility

### Inheritance
A Dog is an Animal -> inheritance: Dog extends Animal
A Page can be Printed -> inheritance: Page implements Printable

### Abstract
When it doens't make sense to create objects of a class

``` java
public abstract class Shape {
	public abstract double calculateSurface();
}

public class Rectangle extends Shape {
	@Override
	public double calculateSurface() {
		return getWidth() * getheight();
	}
}
```

### Inheritance vs composition
You can only inherit from one super class
You can compose multiple instances of objects
Delegate

# Unit Testing

### The goal of unit testing
- Enable sustainable growth of the software project
- Avoid the stagnation phase and maintain the development pace over time
- Trust that your changes won't lead to regression/bugs
- A tool that provides insureance against a vast majority of **regressions**
It's quite easy to grow a project, especially whem you start from scratch, but it's harder to sustain this growth process over the time. So this is all about being **consistent**

### What makes a successful test suite

1. It's integrated into the development cycle.
2. It targets only most important parts of your code base! (Testing business logic gives you the best return on your time investment).
3. It provides maximum value with minimum maintenance costs.

### What is a unit test?
In essence, a unit test is an automated test that verifies a small piece of code (a unit), and does it quickly.
Tests shouldn't verify **units of code**.
Tests should rather verify **units of behaviour**.
It should test something that is meaningful for the **problem domain** and a **business person**.
The unit could span across multiple classes or only one class, or even take up just a tiny method.

### Four pillars of a good unit test.
1. Protection against regressions
Regression == software bug. The larger the code - the more bugs you can have. The more **business logic** you test, the less bugs you might possibly have.
2. Resistance to refactoring
If you refactor code, and your tests still run - then you did a good job. Also it allows to see the faulty code before actually launching something into production.
3. Fast feedback
The faster the tests, the more tests you can run at once
4. Maintainability
Make sure your tests are easy(ier) to read. Also make sure that your tests are not hard to run.

# Stream
### Streams API
This are mainly the same thing as any JS HOF (higher order function)

The basic structure should be:
Stream Source (a collection, any type) -> Operations (filtering, sorting, mapping etc.) -> Terminal Operation (like sum, or average, or collect into another collection)

_Examples_:
- Creating a stream from a list of values
``` java
Stream.of("Jughead","Betty","Archie","Veronica")
	.map(String::toLowerCase) //since the value is a string we can call a lamda expression. Also works for others like Integer::intValue. ClassName::method
	.sorted()
	.forEach(System.out::println);

OUTPUT:
archie
betty
jughead
veronica
```

- Converting a collection into a stream
``` java
List<Product> products = new ArrayList<>();  
products.add(new Product(1, "cookies", 2.99));  
products.add(new Product(2, "chocolate", 3.99));  
products.add(new Product(3, "bananas", 1.99));

products.stream()
		.filter(e -> e.getPrice() > 2)
		.sorted(Comparator.compareDouble(Product::getPrice))
		.forEach(System.out::println);

OUTPUT:
Product{id=1, name='cookies', price=2.99}  
Product{id=2, name='chocolate', price=3.99}
```

### Intermediate operations
Return a stream, we can apply chaining for them. Like: map(), filter(), sorted() etc

### Terminal operations
Return nothing (void) or a non-stream result (int, double ...)
Therfore after a terminal operation, no longer possible to chain. Like: forEach(), sum(), max() etc

### Transforming object streams to primitive streams
``` java
double avg - products.stream()
	.mapToDouble(e -> e.getPrice)
	.average()
	.orElse(0);
```
**average()** returns an OptionalDouble
by calling **orElse(0)** will return the double inside or 0 if there is none.
```java
IntStream.range(1,4)
	.mapToObj(e -> new Product(e, "Prod " + e, e*2))
	.forEach(System.out::println);
```

```java
Stream.of("Jughead", "Betty", "Archie", "Veronica")
	.map(e -> {
		System.out.println(e);
		return e.toUpperCase();
	})
```
In this case nothing gets printed, because Intermediate operations are only evaluated if a terminal operation is present.

``` java
Stream.of("Jughead", "Betty", "Archie", "Veronica")
	.map(e -> {
		System.out.println(e);
		return e.toUpperCase();
	})
	.forEach(System.out::println);

OUTPUT:

Jughead  
JUGHEAD  
Betty  
BETTY  
Archie  
ARCHIE  
Veronica  
VERONICA
```
The stream doesn't move horizontally executing all the map operations first and then the forEach operations. In this case: each element moves along the chain vertically, as is demonstrated by this snippet's output. (so every element is printed out, then transformed into Upper Case, and then pritned out again in the forEach loop)



### Collect
A collect is a very useful terminal operation
It allows you to transform elements of a stream into a different result like List, Set, Map

``` java
List<Person> persons = new ArrayList<>();  
persons.add(new Person("Jughead", 18));  
persons.add(new Person("Betty", 18));  
persons.add(new Person("Veronica", 21));  
persons.add(new Person("Archie", 20));  

List<Person> filteredPersons =  
	persons.stream()  
			.filter(p -> p.getAge() > 18)  
			.collect(Collectors.toList());
```

``` java
Map<Integer, List<Person>> personsPerAge =  
persons.stream()  
	.collect(Collectors.groupingBy(Person::getAge));  

personsPerAge.forEach((a, p) -> System.out.println(
		String.format("%s %s", a, p)));
```

# TIPS
Sometimes it might be very useful to first get a hang of the program you are planning to build, scheme it, and then get to work on it.

If someone of your team does not understand a code, then do not use it.

Packages are sometimes called in reverse domain name.

It is very important to create class (especially if they have something that needs to be created), and delegate the work properly. For example: if you have an enhanced value, then create a class for it, and do not care.
