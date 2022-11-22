## AirBnB Clone - The console
![HBNB](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20221122%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221122T131933Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=e44acc7b672de6bfe620a2b5fd9a4157034ace7d2530e51885a45028af7a4311)
So this project is the first step towards building a first full web application (which is an AirBnB clone). This first step consists of a custom command-line interface for data management, and the base classes for the storage of this data.

## Step 1: Write a command interpreter (The Console)

## Console and Command Usage
### Functionalities of this command interpreter
The console is a Unix shell-like command line user interface provided by the python CmdModule It prints a prompt and waits for the user for input, for our project we used (hbnb)

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc...
- Do operations on objects (count, compute stats, etc...)
- Update attributes of an object
- Destroy an object

  
### Execution
#### Your shell should work like this in interactive mode:

```
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

#### But also in non-interactive mode: (like the Shell project in C)

```
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


## Resources
- [cmd module](https://docs.python.org/3.8/library/cmd.html)
- [packages concept page](https://alx-intranet.hbtn.io/concepts/74)
- [uuid module](https://docs.python.org/3.8/library/uuid.html)
- [datetime](https://docs.python.org/3.8/library/datetime.html)
- [unittest module](https://docs.python.org/3.8/library/unittest.html#module-unittest)
- [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
- [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)

# AUTHOR
- Aminu Rabiu | arabiu033@gmail.com | [Github](https://github.com/arabiu033)
- Damilola Joshua Oluwafemi | joshuadami17@gmail.com | [Github](https://github.com/Joshdb-18)
