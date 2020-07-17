from os import system, name 
from os.path import expanduser
import os
import numpy
import pickle

root = expanduser("~") + "/.config/vOS"

def clear(): # Function to clear the screen
    if name == 'nt':  # Use 'cls' command if host is Windows
        _ = system('cls') 
    else: # Use 'clear' command if host is Mac or Linux
        _ = system('clear')

def initialize():
    print("Initializing...")
    
    if os.path.isdir(root):
        print("vOS root directory already exists at " + root)
    else:
        os.mkdir(root)
        print("Created vOS root directory at " + root)


    if os.path.isfile(root + "/sys.0s"):
        print("vOS system database already exists at " + root + "/sys.0s")
        sysDatabase = open(root + "/sys.0s", "w")
    else:
        sysDatabase = open(root + "/sys.0s", "w")
        print("Created vOS system database at " + root + "/sys.0s")
    
    systemDatabaseArray = ["username", "password", ["setting1", "setting2", "setting3"]]
    sysDatabase.write(pickle.dumps(systemDatabaseArray, protocol=0))
    print("Wrote to the system database at " + root + "/sys.0s with a placeholder database") 

clear()

if os.path.isfile('~/.config/vOS/database.0s'):
    print ("File exist")
else:
    print ("Database file does not exist")
    input = raw_input("Would you like to initialize vOS? (y/n)")
    if input.lower() == "y":
        initialize()
    else:
        print("Terminating")


