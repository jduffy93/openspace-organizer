# openspace-organizer
01 - Project for becode - openspace-organizer

## Description

This program can be used to randomly assign a list of people around multiple tables in a room.

## Installation

To run this program you will need Python and the Python library Pandas.
This code was run in Python 3.11.5 in a conda environment.

## Usage

To run this program you need to run main.py in a Python environment, and have an excel spreadsheet with a list of names.

Many variables/paramenters have a default value assigned to them, which will allow this program to be run with minimal input.\<br>
However, in the future I plan to add more functionality and ability to change these values, without the user having to edit the code themselves.\<br>
For the moment here is a list of the variables with default values:\<br>
    - number_of_tables = 6 - This sets the number of tables in a room\<br>
    - capacity = 4 - This sets the number of seats around a table\<br>
    - free = True - This controls if a seat is occupied or not. Currently the program assumes every seat is free to begin with.\<br>
    - filename = 'openspace_output.txt' - This controls the path and filename of the output.
