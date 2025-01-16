# Java Fx
It is a Java-based software platform for creating rich and interactive desktop applications. It has a bunch of features, such as:
- UI Controls
- Scene Graph
- CSS Styling
- Media Support
- Animation
- FXML
- Integration
- Platform Independencies

# Setting up
We will be using the Kotlin and not Groovy, when creating the directory

Afterwards, we will make use of JavaFX plugins inside the build.gradle file.

Also we should make sure to use a version 17 of JDK!

Afterwards we will be setting up the plugins to install.

From now on, we are going to run our programs through the gradle.

We should make sure to actually make use of java.fx imports, and not other versions.

We will not be making most of our UI via the direct coding.

# JavaFX specifics
We are going to use the Scene Builder program, and afterwards we will be creating the FXML files inside the resources directory inside our Java program (FXML subdirectory - /resources/fxml/filenames).

This app can be also used as a plugin for InteliJ

We can make use of creating specific controllers.

In order to start a program, we need to make use of FXML loader, then we would need to actually build a Scene and then put it on a stage.

# Load the FXML file in the Application class
Once you started creating the Application class (the GUI itself) you would need to load the "model" you created in the fxml resources. That way you will be able to start changing and working with your stuff

# The controller
For changing the stuff inside the stuff (operating in general) with the GUI interface, we need to create **controllers** which then allow us to monitor actions on the interface. Think of it like this: FXML is your HTML, and the controller would work like your JavaScript.

To access a field inside your controller, first make sure to give a "field" in scene builder a **fx:id**. Then you will be able to select that field inside your coding. This is needed only when you need access to that button or "field"

Also you can handle actions on the fields if you specify the actions for them inside the SceneBuilder.

# Building a fresh project

## Start
Once you created yourself the project (choose gradle, Kotlin style), then you should go to **build.gradle.kts**, and start setting up

First thing  you do after creting the project, you add the plugin to the Java project

``` Java
plugins {
	id("java")
	id("org.openjfx.javafxplugin") version "0.1.0"
}
```

Load the scripts then you do

``` Java
javafx {
	modules("javafx.controls")
}
```

Also your plugins should include application plugin
```java
plugins {
	id("java")
	id("application")
	id("org.openjfx.javafxplugin") version "0.1.0"
}
```

Your class should then extend the Application class

```java
public class HelloApp extends Application {
	
}
```

And in the end you would need to specify in the application your main class
```java
application {
	mainClass = "hello.ui.fx.Program"
}
```

Next parts can be seen inside the actual assignments

Note:
We need to import additional plugins to make java work with the fxml formats too. (We are using SceneBuilder program to make scenes for fxml. We store fxml files in src/main/resources/fxml)

```java
javafx {  
    modules("javafx.controls", "javafx.fxml")  
}
```

A **controller** is a Java file that controls a Java file that controls your **fxml**.
The name of the controller is to be specified inside the SceneBuilder application
It is very important for the FXML file and the controller to be linked, otherwise they just wont work together! So it might be useful to actually create the fxml files in SceneBuilder

Note for coding: if you need to show an actual list of entities, then you would need to use a helper class (built-in) called FXCollections.observableList, and then in the field specify the type of the value

It might be handy to first create the Controller so that afterwards you can actually put that reference inside the Scene Builder