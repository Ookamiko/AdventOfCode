# Summary

This is a simple python project allowing to retrieve input from the [AdventOfCode website](https://adventofcode.com/) and send it to a function for resolution.

There is a template folder containing all basic definition to quickly implement a new year.

# Dependancy

This project is made available for python 3.8+.

To work it need the [requests](https://pypi.org/project/requests/) module :
```
python -m pip install requests
```

# Use of project

## Defining a new year

To define a totally new year with premade function, follow those steps :
1. Make a full copy of the template folder
2. Rename the copied folder as you wish (preferably named it after the year you want to define)
3. In adventofcode.py, import the `get_solve_function` from `YOUR_NEW_FOLDER_NAME.generic`. Alias this import.
4. In adventofcode.py `def solve(year, day, level)` function, add a condition to implement the `fct` variable with the `ALIAS_GIVEN(day, level)`.

Example of adventofcode.py implementing solution for year 2022 :
```python
#!/usr/bin/python

import os
import sys

import requests

from datetime import datetime, timedelta
from template.generic import get_solve_function as fct_template

# Import made for year 2022
from year_2022.generic import get_solve_function as fct_2022

# Session ID. Check README file to see how to retrieve this value.
CONST_ID = ""
CONST_URL = f"https://adventofcode.com/"

def default(input):
    sys.exit("""
No function define for year passed as argument.
Looked at the README file to know how to define a new year.
        """
        )

def get_input(year, day):
    cookies = {
        'session': CONST_ID,
    }

    res = requests.get(CONST_URL + year + "/day/" + day + "/input", cookies=cookies)

    if res.status_code == 404:
        sys.exit('No input found. Are you sure to ask for a year-day available ?')
    else:
        sys.exit(res.text)

    return res.content.decode('UTF-8')

def solve(year, day, level):

    if CONST_ID == "":
        sys.exit("""
No session ID defined.
Looked at the README file to know how to set it up.
        """)

    input = get_input(year, day)
    fct = default

    # Condition to use the correct fct_x loaded
    if year == '2022':
      fct = fct_2022(day, level)

    return fct(input)
```

## Retrieve your session id

The program use your session id from the [AdventOfCode website](https://adventofcode.com/) to retrieve your specific input.

This session id can be find in your cookie once you are logged on the website.

To retrieve it (work on Edge, Firefox, Chromium) :
- Log on [AdventOfCode website](https://adventofcode.com/) on any navigator.
- Press `F12` to open the dev tool.
- Navigate the dev tool to find your cookie (e.g. on Chromium : Application > Storage > Cookies).
- Locate the cookies use by the [AdventOfCode website](https://adventofcode.com/).
- Copy the value for the `session` cookie.
- Implement the `CONST_ID` variable in the adventofcode.py file with this value.

Normally the session id has a big expiration date, however it's possible that the program specify that you need to log on to retrieve your specific inputs. If it's your case, it might means that your session id has expired. Just implement the `CONST_ID` variable with your newly session id.

## Your resolution

Once you have define a year and that you have implemented your session id, all it's left to be is to resolve the puzzles.

Insid your newly created folder, you will find a day folder with files for each day. Those files define two functions `level1(input)` and `level2(input)`. You only to have to resolve your puzzle and make those function return your solution to make the program work.

To be noted, you can return which type of variable you want, the program will stringify it with the use of `str()`.

## Command use

Once you want to check your solution for a specific year-day-level puzzle, you need to call the program using command line.

To ask for a resolution, you just need to use this command on the root folder :
```
py main.py [year] [day] [level]
```

- Year : int greater or equal to 2015 (smallest year available)
- Day : int between 1 and 25 include
- Level : 1 or 2

Example of asking to resolve the first level of 12/2022 puzzle :
```
py main.py 2022 12 1
```

Example of result :
```
py main.py 2022 12 1
Start execution for problem 2022-12-1.
Solution : 520
Executed in 13.393798s
``` 

The program also display the time taken to resolve the puzzle with your solution. It's a good indicator if you need/want to improve it.

# Git management

The git repository contains two branch types :
- master
- solution/***year***

On the master branch you will find the project without solution on the release tag as well as merge from branches solution/***year*** where all puzzle have been completed.

To find the solutions of a specific year not merged into the master branch, refer to the specific solution/***year*** branch.
