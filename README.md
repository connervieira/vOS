# vOS
A command line OS like interface that runs off a host OS as a sub-program. That's a lot of big words, but in short, think of it like a baby computer within your current computer. It's not a full operating system, since it requires a "host os" (Your current operating system), but it has the feel of a command line OS.
It isn't really meant to be a useful, functional program, and is more of just programming project. Building a program with such a wide array of capabilities was a great way to teach myself Python, and a lot of what goes into building programs with it.
 
## How To Use
To use vOS, you'll have to be on Linux or MacOS. Windows might work, but you'll likely run into many issues.
### Linux
First, make sure that Python3 is installed. Open a Terminal and type the following commands.
`sudo apt-get install python3`

Next, you'll need to install the dependencies that vOS uses
`pip3 install pathlib`
`pip3 install numpy`
`pip3 install passlib`

Finally, you'll need to download and run 'main.py' from this repository.
`git clone https://github.com/connervieira/vOS`
`cd vOS/`

To run vOS, simply type
`python3 main.py`

### Mac
First, you'll need to install the Homebrew package manager, from https://brew.sh. Open a command prompt and enter the following command.
`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"`
Run through the on the guided installer before continuing. This process may take a while.



Make sure that Python3 is installed. Open a Terminal and type the following commands.
`brew install python3`

Next, you'll need to install the dependencies that vOS uses
`pip3 install pathlib`
`pip3 install numpy`
`pip3 install passlib`

Finally, you'll need to download and run 'main.py' from this repository.
`git clone https://github.com/connervieira/vOS`
`cd vOS/`

To run vOS, simply type
`python3 main.py`


## Features
### Custom File Format
vOS uses a custom file format, .0s, to make it easier to descern which files will work with it.

### Command Prompt
vOS has a full command prompt, complete with commands to accomplish most tasks you'd otherwise do in the TUI mode.

### Graphical
Despite running in the command line, and having a full command prompt option, vOS is graphical enough that someone with no experience on the command line would have no issue using it.
 
### Secure
When setting up a user account on vOS, the password is fully and properly hashed, to ensure that other programs can't read it.
 
### Reliable and Stable
vOS takes every chance it can get to ensure that everything runs smoothly. When first starting the system, it will check for everything single file it needs to ensure that nothing goes wrong. It also comes with a built in back up feature, in case something goes wrong. If there does happen to be a failure, vOS can load into a rescue terminal, allowing you to restore a backup, verify the system integrity, or even edit the system database yourself!
 
### Customizable
vOS is customizable in the sense that you can configure it to work how you want. If you prefer the command line over a TUI, vOS has you covered. If you prefer to use VIM as your external editor, rather than NANO, you can configure so in the settings.
