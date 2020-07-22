# AirBnB_Clone - The Console :house:
![air_bnb_screens](https://user-images.githubusercontent.com/51524966/88120343-b0ca5280-cb90-11ea-85e0-2182d266d899.png)
## Description
#### AirBnB_CLone is a simplified command interpreter. The console includes many of the most basic features of a "regular" console.This is the very first project of the multiple AirBnB Clone projects we're asked to create at Holberton School, each of which build on each other.

## About Me
Hi, I'm Faizan, a software engineer with an interest in Data Science. I spent the last year learning how to code through the project based curriculum at Holberton School. Before learning software engineering, I was in management. You can find out more about me here:
* Faizan Khan 🌌 [b1naryp0et](https://github.com/b1naryp0et) | [@b1nary_p0et](https://twitter.com/b1nary_p0et) | [My LinkedIn](https://www.linkedin.com/in/fkkhan/) | [This Project's Repo](https://github.com/maybe-william/RocketRiders)

## Developing AirBnB_Clone
This was the first team project at Holberton, which involved python! Jon Patterson, my partner for this project, hadn't worked together yet so we decided it would be fun to work with someone new on a project which was quite involved. Fortunately, we encountered no major issues.

## Implemented and Non-Implemented Features
Most of the major features we endeavored to implement did end up being present in this project. This includes infusing our command interpreter with common commands such as "create" and "destroy".

Features we didn't implement but may explore in the future are updating certain instance based on their ID with a dictionary and more unit tests.

## Challenges
We didn't encounter any major challenges when completing this project. The only two that come to mind are some scheduling and pep-8 compliance issues.

## Synopsis

The console is the first of 4 components of Holberton School's AirBnB Project. This project utilizes and reinforces some fundamental concepts of higher level programming. The aim of the AirBnB project is to deploy our server a simple duplicate of the AirBnB website, **HBnB**. For this portion of the project, we have created a command interpreter to create and manipulate objects.

#### Capabilities of The Console:
* Create a new objects (ex: a new User or a new Place)
* Retrieve objects from files
* Perform operations on objects (counting)
* Update attributes of an object
* Can destroy objects

## Table of Contents
* Installation and Usage
* Commands
* Base Model
* File Storage
* Other Classes
* Example
* File Descriptions
* Bugs
* Authors



## Installation and Usage

For best results, please use Python3 on an ubuntu-based system to execute the program
```
$ git clone [repository link]  
$ cd AirBnB_Clone
$ ./console.py (To run console in interactive mode)
$ echo "help" | ./console.py (To run console in non-interactive mode)
```


## Commands
The Console supports the following commands:
  

* `EOF` - Exits the console 
* `quit` - Exits the console
* `create <class>` - Creates a new instance of`and saves it.
* `destroy <class> <id>` - Deletes an instance.
* `showshow <class> <id>` - Display the specified object.
* `all` - Display string representation of all instances 
* `update` - Updates attribute. 


## Base Model

The Base Model contains the following public instance attributes:

-   id: string: Generates  uuid when BaseModel instance is created.
-   created_at: Contains date and time information of instance at creation.
-   updated_at: Contains date and time information of an instance during update.
-   **str**: prints: [] (<self.id>) <self.**dict**> Public instance methods:
-   save(self): updates public instance attribute
-   to_dict(self): returns a dictionary containing all keys/values of  **dict** .

## File Storage

Serialization and deserialization processesare used to store objects. The following is a list of attributes in  **file_storage.py**

-   __file_path: string path to the JSON file 
-   __objects: dictionary stores objects by id
-   all(self): returns dictionary __objects
-   new(self, obj): sets in __objects 
-   save(self): serializes __objects to JSON 
-   reload(self): deserializes the JSON file to __objects

### Other Classes

More classes inherited from base model:

-   User
-   Amenity
-   Review
-   Place
-   City
-   State


## Example
```
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) help quit
Quit command to exit the program

(hbnb) 
(hbnb) 
(hbnb) quit 
guillaume@ubuntu:~/AirBnB$ 
```

## File Descriptions

Listed below are the descriptions of the files in this repo:

File | Description  
--------|---------------  
`models/base_model.py` | Defines common attributes for other classes
`models/engine/file_storage.py` | Serializes instances to a JSON file and deserializes JSON file to instances
`console.py`| Contains the entry point of the command interpreter
`models/user.py` | Class that inherit from `BaseModel`
`models/state.py` | Class that inherit from `BaseModel`
`models/city.py` | Class that inherit from `BaseModel`
`models/amenity.py` | Class that inherit from `BaseModel`
`models/place.py` | Class that inherit from `BaseModel`
`models/review.py` | Class that inherit from `BaseModel`




## Bugs
Unable to locate bugs at this time.

## Authors
Faizan Khan :surfer:
Jonathan Patterson -:candy:
