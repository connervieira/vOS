from os import system, name 
import getpass
from pathlib import Path
from os.path import expanduser
import os
import numpy
import pickle
import sys
from passlib.context import CryptContext


if (str(Path.home()) == "/root"): # Terminate if the program is being run as root
    print("vOS can't be run as root.")
    print("Terminating")
    sys.exit()

root = str(Path.home()) + "/.config/vOS"


passwordContext = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=30000
)

def encryptPassword(password):
    return passwordContext.hash(password)


def checkPassword(password, hashed):
    return passwordContext.verify(password, hashed)

def commandPrompt():
    
    while True:
        commandlineinput = input(systemDatabaseArray[2] + "@vOS:$ ")
        if commandlineinput == "exit":
            break
        elif commandlineinput == "help":
            print("exit - Exit the command prompt")
            print("help - Get a list of all commands")
            print("terminate - Terminate vOS, and return to the host OS")
            print("verify - Verify the integrity of the vOS filesystem")
            print("rescue - Manually edit the system database with your external editor of choice")
            print("saferescue - Manually edit the system database ignoring your preferred editor (Useful if database is corrupt)")
            print("backup - Back up the system database")
            print("restore - Restore the system database")
                
        elif commandlineinput == "terminate":
            print("Terminating vOS")
            sys.exit()
        elif commandlineinput == "verify":
            verifyIntegrity()
        elif commandlineinput == "rescue":
            edit(root + "/sys.0s", systemDatabaseArray[4][0])
        elif commandlineinput == "saferescue":
            edit(root + "/sys.0s", "nano")
        elif commandlineinput == "backup":
            if os.path.isfile(root + "/sys.bkp"):
                _ = system("rm " + root + "/sys.bkp")
                print("Deleted old backup")
            _ = system("cp " + root + "/sys.0s " + root + "/sys.bkp")
            print("Backed up system database")
        elif commandlineinput == "restore":
            if os.path.isfile(root + "/sys.bkp"):
                if os.path.isfile(root + "/sys.0s"):
                    _ = system("rm " + root + "/sys.0s")
                    print("Deleted current system database")
                else:
                    print("No present database found")
                _ = system("cp " + root + "/sys.bkp " + root + "/sys.0s")
                print("Restored system database from backup")

def clear(): # Function to clear the screen
    if name == 'nt':  # Use 'cls' command if host is Windows
        _ = system('cls') 
    else: # Use 'clear' command if host is Mac or Linux
        _ = system('clear')

def edit(fileToEdit, editor): # Function to edit a file in an external editor
    _ = system(editor + " " + fileToEdit)

def verifyIntegrity():
    if os.path.isdir(str(Path.home()) + "/.config") == False:
        print("Error: ~/.config is missing")
        print("This suggests that your host OS might be damaged")
    else:
        if os.path.isdir(root + "") == False:
            print("Error: ~/.config/vOS is missing")
        else:
            if os.path.isfile(root + "/sys.0s") == False:
                print("Error: ~/.config/vOS/sys.0s is missing")
            else:
                print("The vOS file system appears to be intact")
            


def initialize():
    print("Initializing...")

    if os.path.isdir(str(Path.home()) + "/.config") == False:
        print("~/.config doesn't exist")
        print("This most likely means you are running a non-unix based OS")
        print("vOS is not supported on non-unix platforms, but you can still attempt to use it at your own risk")
        print("Create a folder called '.config' in your home folder and re-run vOS if you still want to attempt to use vOS")
        sys.exit()
    
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

    print("\n")
    firstname = input("First Name: ")
    lastname = input("Last Name: ")
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    clear()
    
    sysDatabase = open(root + "/sys.0s", "wb")
    systemDatabaseArray = [firstname, lastname, username, encryptPassword(password), ["nano", "setting2", "setting3"]]
    sysDatabase.write(pickle.dumps(systemDatabaseArray, protocol=0))
    sysDatabase.close()

    print("Wrote information to system database at " + root + "/sys.0s")
    input("Press enter to terminate.")
    sys.exit()

clear()

if os.path.isfile(root + "/sys.0s"): # Check if system database has already been initialized
    print("vOS is already initalized")
    print("Starting")

    sysDatabase = open(root + "/sys.0s", "rb")
    systemDatabaseArray = pickle.loads(sysDatabase.read())
    
    print("Username: " + systemDatabaseArray[2])
    passwordi = getpass.getpass("Password: ")
    clear()

    if checkPassword(passwordi, systemDatabaseArray[3]):
        print("Authentication successful")
        
        while True:
            clear()
            titlebar = " " + systemDatabaseArray[2] + " - " + "Main" + " "
            topbarsize = ""
            for i in titlebar:
                topbarsize = topbarsize + "_"
            print(" " + topbarsize)
            print("|" + titlebar + "\\")
            print("|----------------------------------------")
            print("| 1. Command Prompt                      |")
            print("| 2. Files                               |")
            print("| 3. Settings                            |")
            print("| 4. Tweaks                              |")
            print("| 5. Programs                            |")
            print("| 6. Terminate                           |")
            print("|________________________________________|")
            selection = input("Selection: ")
            
            if selection == "1":
                clear()
                commandPrompt()
            elif selection == "2":
                pass
            elif selection == "3":
                
                clear()
                titlebar = " " + systemDatabaseArray[2] + " - " + "Settings" + " "
                topbarsize = ""
                for i in titlebar:
                    topbarsize = topbarsize + "_"
                print(" " + topbarsize)
                print("|" + titlebar + "\\")
                print("|----------------------------------------")
                print("| 1. External Editor                     |")
                print("|________________________________________|")
                selection = input("Selection: ")
                
                if selection == "1":
                    print("Current external editor: " + systemDatabaseArray[4][0])
                    selection = input("New external editor: ")
                    systemDatabaseArray[4][0] = selection
                    
                    sysDatabase = open(root + "/sys.0s", "wb")
                    sysDatabase.write(pickle.dumps(systemDatabaseArray, protocol=0))
                    sysDatabase.close()
                else:
                    clear()
                    print("Unrecognized input")
                    print("Please enter the number of a selection")
                    input("")
                


            elif selection == "4":
                pass
            elif selection == "5":
                pass
            elif selection == "6":
                print("Terminating")
                sys.exit() 
            else:
                clear()
                print("Unrecognized input")
                print("Please enter the number of a selection")
                input("")

    else:
        print("Incorrect password")
        print("Terminating")
        sys.exit()
    
   

else:
    print("Database file does not exist")
    selection = input("Would you like to initialize vOS? (y/n)")
    clear()
    if selection.lower() == "y":
        initialize()
    else:
        selection = input("Would you like to open a rescue command prompt? (y/n)")
        if selection.lower() == "y":
            systemDatabaseArray = ["firstname", "lastname", "username", "password", ["setting1", "setting2", "setting3"]]
            commandPrompt()
            print("Terminating")
            sys.exit()
        else:
            print("Terminating")
            sys.exit()


