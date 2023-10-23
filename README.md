# The AirBnB Clone Console Project :house_with_garden: :star2:

Greetings! We're thrilled to introduce our Python project, which revolves around the development of a personalized console or command-line interpreter designed for overseeing a data management system. This project is a vital component of a broader system where we handle diverse data types represented by different classes and actively engage in managing their persistence.


## The Command Interpreter :computer:
The command interpreter we're crafting is tailored to handle an array of object types, offering commands for tasks such as creating new objects, administering existing ones, extracting information, and more. It's thoughtfully designed to be user-friendly, featuring a straightforward syntax and delivering comprehensive feedback to users.


## How to start :rocket:
To initiate the console, please proceed to your project directory within your terminal, and execute the console file, which we'll refer to as "console.py." Here's the command:


```
$ ./console.py
```
## How to use :bulb:

While operating within our custom console, you can commence the execution of commands. The syntax is intuitive, ensuring a straightforward interaction with the system:

create <class name> - Initiates the creation of a new instance of the specified <class name>, saves it to a JSON file, and displays its unique identifier.
show <class name> <id> - Presents the textual representation of an instance, identified by the class name and ID.
destroy <class name> <id> - Removes an instance based on the class name and ID.
all <class name> or simply all - Provides a listing of all instances of a specific class, or, when no class is specified, it retrieves all instances across all classes.
update <class name> <id> <attribute name> "<attribute value>" - Allows for the modification of an instance, identified by class name and ID, by adding or updating a specific attribute.

## Examples :eyes:
Here are some examples of how you can use the commands:

```
(hbnb) create User
246c227a-d5c1-403d-9bc7-6a47bb9f0f68
(hbnb) show User 246c227a-d5c1-403d-9bc7-6a47bb9f0f68
[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68', 'created_at': '2023-10-20T22:31:03.879122', 'updated_at': '2023-10-20T22:31:03.879153'}
(hbnb) update User 246c227a-d5c1-403d-9bc7-6a47bb9f0f68 first_name "Omar"
(hbnb) all User
[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68', 'created_at': '2023-10-20T22:31:03.879122', 'updated_at': '2023-10-20T22:31:03.879153', 'first_name': 'Hajar'}
```
## Contributors :sparkles:
The list of contributors [`AUTHORS`](./AUTHORS) file.
