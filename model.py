import os
import sqlite3

def checkDB():
    """Check to see if a database exists"""
    return os.path.isfile(os.environ['DBPATH'])

def buildDB():
    """Main function to build the full database"""
    print("CHECK")
