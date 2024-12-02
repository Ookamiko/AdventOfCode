#!/usr/bin/python

import os
import sys

import requests

from template.generic import get_solve_function as fct_template

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
    elif res.status_code != requests.codes.ok:
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

    return fct(input)