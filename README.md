# brainfuck
You thought Brainfuck was bad?  Think again.  Get ready to meet...

## EPIC BRAINFUCK

# Motivation
Contrary to many other codebases, this repository is not just about writing yet **another** Brainfuck compiler.
Just search "brainfuck" on GitHub, and you'll see just how many people have already written compilers, and
how many different languages it has been written in. It's incredible for a language so basic and rudimentary,
how much attention it has garnered over the years. Indeed, it is quite the brainteaser to write stuff using
only eight characters.

However, "brainteaser" is perhaps a euphemism for the language's actual name, so I began to think: how can I
crank up the "brain-teasing" if you'd like and make this language even more difficult to work with? The answer?
Who said that ```>``` means ```++ptr```, where ```ptr``` points to an "infinitely long" ```char``` array?  Why
can't we use other characters to signify that?  And who said we needed to have concrete aliases for these
bits of C code?  This is where this Brainfuck repository deviates from most.  Not only did I write an interpreter
for "traditional" Brainfuck code, but I also wrote **several** variants in which the syntax of Brainfuck changes
from interpretation to interpretation.  Toss in some unexpected behaviours (e.g. massive file write out of nowhere),
and there you have it: **EPIC** Brainfuck shenanigans!

# Requirements
As you can see in the repository, there are **four** Python files, so in order to run any of the code, you **need** to
download and install Python on your machine or check if your OS already has Python built-in. That is all you need.
The code was written so as to have minimal dependencies on any external libraries beyond those packaged with Python
itself. Once you have Python on your machine, you can now download the code!

# Installation
There are three ways to install this code. If you want the most current (development) version of the source code, you can either run the following command from the terminal:
```
git clone https://github.com/gfyoung/brainfuck.git
```

**OR**

you can click [here](https://github.com/gfyoung/brainfuck/archive/master.zip) to download a ZIP file of the ```master```
branch and unzip the files locally.

Once downloaded, run ```python setup.py build_ext -i``` in the terminal to do an inplace installation, just in case you already have ```brainfuck``` installed elsewhere. You can also run ```python setup.py install``` if that does not apply.

If you want to download the most recent, stable version of the source code, run the following command in the terminal:
```
pip install brainfuck
```

If ```pip``` is having issues, visit the download page [here](https://pypi.python.org/pypi/brainfuck) to download
a ZIP file of the source code and follow the instructions described above when downloading a ZIP file of the ```master```branch.

Once you have the files located somewhere in your local directory, ```cd``` to that directory to make sure all files
were successfully downloaded. If so, you have successfully installed the source code!

# Usage
The main file that you want to run is ```Brainfuck.py```. It is the only Python executable for starters, and it is also dependent on the other three files provided.

```
Brainfuck.py [-h] [-i] [-l] [-f file] [-c code] [-v]

-h : display documentation
-i : interpreter specification

There are six options here:

"nice"    - traditional Brainfuck interpreter, no shenanigans
"reset"   - resets character array to all zeros and the array pointer to
            point at that zeroth element of that array after each execution
"chars"   - changes the eight characters used when coding and the semantics
            behind them after each execution
"file"    - writes 'LOL' 1000 times to a "log" file after every executation
"browser" - opens a tab in your browser playing the "Troll Song" sung by
            Eduard Khil on YouTube after every execution
"random"  - choose an interpreter at random

-l : whether or not to launch the Brainfuck console after running a piece
     of Brainfuck code. Note that this argument is not necessary should no
     code be provided. The console will start automatically

-f : the path to a Brainfuck code file that is to be run. The path can be
     absolute, or it can be relative to the location of this executable

-c : a piece of Brainfuck code to interpret

-v : display the version of the Brainfuck interpreter
```

# Language Documentation
Regardless of interpreter, Brainfuck keeps track of two data structures behind the scenes. The first is an array of characters
appropriately denoted as ```array``` in the code. While ```array``` stores integers in Python, the elements will be restricted to the
range ```[0, 2**8 - 1]``` in accordance with macros like ```UCHAR_MIN``` and ```UCHAR_MAX``` in C. In theory, this array is infinite, but
in practice, the size of ```array``` is defaulted to ```30000```. The second is a pointer to the current index to the array denoted as
```ptr``` in the code. As the interpreters are written in Python, pointers have less of a significance compared to languages such as C.
However, keeping track of the current index in ```array``` is necessary in Brainfuck.

With these two data structures, we can now talk about syntax. Every interpreter has eight characters of significance in Brainfuck.
All other characters are simply ignored by the interpreter. In traditional Brainfuck, these characters are:

|     Character       |                                         Meaning                                                                                                                                                                                                                                                                                                         |
|:-------------------:|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|       ```>```       | Increment ```ptr``` by one, modulus the number of elements in ```array``` (i.e. 30000)                                                                                                                                                                                                                                                                  |
|       ```<```       | Decrement ```ptr``` by one, modulus the number of elements in ```array``` (i.e. 30000)                                                                                                                                                                                                                                                                  |
|       ```+```       | Increment ```array[ptr]``` by one, modulus 2**8                                                                                                                                                                                                                                                                                                         |
|       ```-```       | Decrement ```array[ptr]``` by one, modulus 2**8                                                                                                                                                                                                                                                                                                         |
|       ```.```       | Output the character stored at ```array[ptr]```                                                                                                                                                                                                                                                                                                         |
|       ```,```       | Accept one character as input and stored it at ```array[ptr]```                                                                                                                                                                                                                                                                                         |
|       ```[```       | If ```array[ptr] == 0```, instead of proceeding then to the next instruction, iterate through the subsequent characters until the **matching** right parenthesis has been found. Then proceed to the instruction following that matching parenthesis. If none is found, an error message will be raised, and the interpretation terminates immediately. |
|       ```]```       | If ```array[ptr] != 0```, instead of proceeding then to the next instruction, iterate through the previous characters until the **matching** left parenthesis has been found. Then proceed to the instruction following that matching parenthesis. If none is found, an error message will be raised, and the interpretation terminates immediately.    |

# Brainfuck.py Documentation
When you launch ```Brainfuck.py```, you will see a console like this prompting you for characters.
```
>>>
```

You are free to type any Brainfuck code that you want, and it will be interpreted and executed automatically. Let's increment
```array[0]``` by 40 and then hit ENTER.
.
```
>>> ++++++++++++++++++++++++++++++++++++++++
>>>
```

Want to double check that you in fact added 40 to ```array[0]```? As ```ptr``` currently points at zero, you can call ```.``` to
print out the character stored at ```array[0]```, OR you can call the following special command:
```
...
>>> ARRPLZ[0]
-
>>>
```

```ARRPLZ``` can also take arguments in the form of ```[start : end]```, but do note that the endpoint is **exclusive**.

You can also get the current value of ```ptr``` by typing ```PTRPLZ```, as follows:
```
...
>>> PTRPLZ
0
>>>
```

In case you're simply tired of having your brain "fucked with," type the following:
```
...
>>> GMTFOH

~
```
**FYI**: ```GMTFOH``` = "Get me the fuck out of here"

Feeling rather adventurous and want to try some **EPIC** Brainfuck? Then launch the console with an interpreter other than the "nice" one!
How are things different? Well, first, you need to know what the eight important characters are so that the modified Brainfuck will be
properly interpreted. You can do so by typing:
```
>>> HELPPLZ!!!

LONG LIVE BRAINFUCK!

       1 --> >
       q --> ,
       e --> <
       4 --> -
       g --> +
       t --> [
       w --> ]
       . --> .

LONG LIVE THE TROLL!

>>>
```

For other special commands (i.e. ```PTRPLZ```, ```ARRPLZ```, and ```GMTFOH```), the interpreter will respond to those commands only
**25%** of the time. Yes, that means you will have to type the command about **four** times before it will respond. That is the naturing
of trolling and further "fucking with" the mind.

# Bugs and Features
Find a bug in the code? Want another feature added to the codebase? Submit an issue **OR** feature request [here](https://github.com/gfyoung/brainfuck/issues)!

# Contributing
Interested in contributing? You are more than welcome! To start, **fork** this repository and clone your fork to your computer. Then,
to start hacking away, create a **feature branch** off ```master```. Once, you're done, submit it as a pull request (PR)! Requirements
are not very stringent. Just make sure that you properly document changes in your commits (e.g. descriptive commit messages) and / or
add documentation to any code that you modify should you **change** or **add** any functionality.
