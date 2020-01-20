import cs50
import csv
import os
from sys import argv, exit

# Check the command line argument to make sure it is a file
if not (len(argv) == 2 and os.path.isfile(argv[1]) and ".csv" in argv[1]):
    print("Usage: python import.py filename")
    exit(1)

# Open database
db = cs50.SQL("sqlite:///students.db")

# Open CSV file for reading
with open(argv[1], "r") as file:

    # Create DictReader
    reader = csv.DictReader(file)

    # Iterate over each row in the file using the reader
    for row in reader:
        name = row["name"].split(' ')

        # If there is a middle name
        if len(name) == 3:
            # Import student's first, middle, last name into the database
            db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
                       name[0], name[1], name[2], row["house"], row["birth"])
        # If there is not a middle name
        elif len(name) == 2:
            # Import student's first, middle, last name into the database with his/her middle name being a NULL placeholder
            db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
                       name[0], None, name[1], row["house"], row["birth"])
        # If first/last name is missing or there is more than 3 name values
        else:
            print("Unacceptbale name detected")
            exit(2)

    # Success
    exit(0)
