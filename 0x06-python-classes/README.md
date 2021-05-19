## Python - Classes and Objects
Object Oriented Programming

- ##### 0-square.py
An empty class `Square` that defines a square

- ##### 1-square.py
A class Square that defines a square by: (based on 0-square.py) \n
  	Private instance attribute: size
	Instantiation with size (no type/value verification)

- ##### 2-square.py
A class `Square` that defines a square by: (based on `1-square.py`)
  - Private instance attribute: `size`
  - Instantiation with optional size: `def __init__(self, size=0):`
  - Size must be an integer, otherwise raise a TypeError exception with \n
   the message `size must be an integer`
  - If size is less than 0, raise a ValueError exception with the message \n
  `size must be >= 0`

- ##### 3-square.py
  - A class `Square` that defines a square by: (based on `2-square.py`)
  - Instantiation with optional size: `def __init__(self, size=0):`
    - `size` must be an integer, otherwise raise a `TypeError` exception \n
      with the message `size must be an integer`

- ##### 4-square.py
