## Python - Input/Output
### General Concepts:
      - How to open a file
      - How to write text in a file
      - How to read the full content of a file
      - How to read a file line by line
      - How to move the cursor in a file
      - How to make sure a file is closed after using it
      - What is and how to use the with statement
      - What is JSON
      - What is serialization
      - What is deserialization
      - How to convert a Python data structure to a JSON string
      - How to convert a JSON string to a Python data structure

 ### Tasks:
      - 0-read_file.py
      a function that reads a text file (UTF8) and prints it to stdout:

      - 1-write_file.py
      a function that writes a string to a text file (UTF8) and
      returns the number of characters written:

      - 2-append_write.py
      a function that appends a string at the end of a text file (UTF8) and
      returns the number of characters added:
      Prototype: `def append_write(filename="", text=""):`

      - 3-to_json_string.py
      a function that returns the JSON representation of an object (string):
      Prototype: `def to_json_string(my_obj):`

      - 4-from_json_string.py
      a function that returns an object (Python data structure)
      represented by a JSON string:
      Prototype: `def from_json_string(my_str):`

      - 5-save_to_json_file.py
      a function that writes an Object to a text file, using a JSON representation:
      Prototype: `def save_to_json_file(my_obj, filename):`

      - 6-load_from_json_file.py
      a function that creates an Object from a "JSON file"
      Prototype: `def load_from_json_file(filename):`

      - 7-add_item.py
      a script that adds all arguments to a Python list, and
      then save them to a file:

      - 8-class_to_json.py
      a function that returns the dictionary description with simple
      data structure (list, dictionary, string, integer and boolean)
      for JSON serialization of an object:

      - 9-student.py
      a class `Student` that defines a student by:
      - Public instance attributes:
      	- first_name
	- last_name
	- age

      - 10-student.py
      Additional attributes to class `Student`

      - 11-student.py
      Additional methods to class `Student`

      - 12-pascal_triangle.py
      Technical interview preparation:
      		-  a function def pascal_triangle(n): that returns a list of lists of integers representing the s triangle of n:Pascal
		- Returns an empty list if n <= 0
		- Assume n will always be an integer
