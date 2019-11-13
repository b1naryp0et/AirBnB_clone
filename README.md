# AirBnB_Clone - The Console :house:
#### AirBnB_CLone is a simplified command interpreter. The console includes many of the most basic features of a "regular" console.

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
