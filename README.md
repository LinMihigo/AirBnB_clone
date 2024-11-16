# AirBnB_clone

## Project Description
The ALx AirBnB Clone project is a full-stack application inspired by the core functionality of the AirBnB platform. This project focuses on building an interactive console for managing various data models such as users, properties, and bookings, which will eventually be integrated into a web framework. It showcases the development of a custom back-end environment, complete with serialization, storage, and data manipulation.

## Getting started
### Prerequisites (Optional)
- Python 3.8.5
- Ubuntu 20.04
### Installation
1. Clone the repo:
```bash
git clone git@github.com:LinMihigo/AirBnB_clone.git
```
2. Navigate into the repo directory:
```bash
cd AirBnB_clone
```
### Starting the console
```bash
$ ./console.py
```
## Usage
Inside the console, you can perform the following actions:

- Create new objects (e.g., User, Place, Amenity).
- Show information about objects.
- Update existing objects.
- Delete objects.

Run `echo "help" | ./console.py` to see list of available command
<br />
Run `echo "help <command>" | ./console.py` to see what a command does.

### Example commands:
Table of commands:
| Command | Example |
| --- | --- |
| Run the console | `./console.py` |
| Quit the console | `(hbnb) quit` |
| Display the help for a command | `(hbnb) help <command>` |
| Create an object (prints its id) | `(hbnb) create <class>` |
| Show an object | `(hbnb) show <class> <id>` or `(hbnb) <class>.show(<id>)` |
| Destroy an object | `(hbnb) destroy <class> <id>` or `(hbnb) <class>.destroy(<id>)` |
| Show all objects, or all instances of a class | `(hbnb) all` or `(hbnb) all <class>` |
| Update an attribute of an object | `(hbnb) update <class> <id> <attribute name> "<attribute value>"` or `(hbnb) <class>.update(<id>, <attribute name>, "<attribute value>")` |

Interactive mode:
```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
Non-interactive mode:
```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## Testing
All tests are in the tests dir
### Documentation
Modules:
```bash
python3 -c 'print(__import__("my_module").__doc__)'
```
Classes:
```bash
python3 -c 'print(__import__("my_module").MyClass.__doc__)'
```
Functions:
```bash
# Outside of a class
python3 -c 'print(__import__("my_module").my_function.__doc__)'

# Inside a class
python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
```

### Unittests

Interactive mode:
```bash
python3 -m unittest discover tests
```
Non-interactive mode:
```bash
$ echo "python3 -m unittest discover tests" | bash
```
