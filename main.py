from os import system, name 
from pathlib import Path
from os.path import expanduser
import os
import numpy
import pickle
import sys


if (str(Path.home()) == "/root"): # Terminate if the program is being run as root
    print("vOS can't be run as root.")
    print("Terminating")
    sys.exit()

root = str(Path.home()) + "/.config/vOS"

def clear(): # Function to clear the screen
    if name == 'nt':  # Use 'cls' command if host is Windows
        _ = system('cls') 
    else: # Use 'clear' command if host is Mac or Linux
        _ = system('clear')

def initialize():
    print("Initializing...")
    
    if os.path.isdir(root + ""):
        print("vOS root directory already exists at " + root)
    else:
        os.mkdir(root + "")
        print("Created vOS root directory at " + root)


    if os.path.isfile(root + "/sys.0s"):
        print("vOS system database already exists at " + root + "/sys.0s")
        sysDatabase = open(root + "/sys.0s", "wb")
    else:
        sysDatabase = open(root + "/sys.0s", "wb")
        print("Created vOS system database at " + root + "/sys.0s")
    
    systemDatabaseArray = ["firstname", "lastname", "username", "password", ["setting1", "setting2", "setting3"]]
    sysDatabase.write(pickle.dumps(systemDatabaseArray, protocol=0))
    print("Wrote to the system database at " + root + "/sys.0s with a placeholder database") 
    sysDatabase.close()

    sysDatabase = open(root + "/sys.0s", "rb")
    # print(str(pickle.loads(sysDatabase.read())))

    print("\n")
    firstname = input("First Name: ")
    lastname = input("Last Name: ")
    username = input("Username: ")
    password = input("Password (will be stored in plain text): ")
    clear()
    
    sysDatabase = open(root + "/sys.0s", "wb")
    systemDatabaseArray = [firstname, lastname, username, password, ["setting1", "setting2", "setting3"]]
    sysDatabase.write(pickle.dumps(systemDatabaseArray, protocol=0))
    sysDatabase.close()

    print("Wrote information to system database at " + root + "/sys.0s")
    input("Press enter to terminate.")
    sys.exit()

clear()

if os.path.isfile(root + "/sys.0s"): # Check if system database has already been initialized
    print("vOS is already initalized")
    print("Starting")
    
else:
    print ("Database file does not exist")
    selection = input("Would you like to initialize vOS? (y/n)")
    clear()
    if selection.lower() == "y":
        initialize()
    else:
        print("Terminating")
        sys.exit()


