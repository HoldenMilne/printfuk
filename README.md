# printfuk
Completely override your python print function with complete garbage that sometimes looks approximately correct

# How to install
Simply install the package either by downloading this git repository and moving the python source code where it needs to or install it using pip.

## Manual (Not preferred)
Copy the printfuk.py file into the one of the paths listed from the following code:
```
import sys
sys.path
```

## Pip
Make sure pip is installed with `pip --version`.  If you get a version print out, then pip is installed.  Otherwise, [install pip](https://pip.pypa.io/en/stable/installation/). 
Once pip is installed type into a console `pip install printfuk`.  And that's it.

## Importing
All you have to do is write `from printfuk import print` at the top of your python script file, and you will never have to worry about clean, nice looking print messages ever again!

# How to use
The print statement behaves more or less like the default print statement in terms of how you most people use it.  It does not handle the following keywords arguments currently:
 * file
 * flush

This version only prints to sys.stdout and is not bufferred.  However, the other keyword arguments, sep and end are handled as per usual.  This package also handles the standard multiple printing in the form of ```print(a,b,c,...)``` and concatenates them with the separator "sep=separator" before printing just like before.  It also handles the end keyword more or less the same.  However, in order to ensure that a user can't print standard text in the normal behaviour, if the end keyword argument is a string of length greater than 1, the this string will also be messed up in the same manner.

The package also adds more keyword arguments:
 * delay - default: 0.1 / float \[0,inf) - Specifies the time delay at which characters are printed in order in seconds.
 * color - default: 88 / innt 
 * startAfter -
 * maxCharMod -
 * useColor -
