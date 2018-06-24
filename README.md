# Fibonacci

This is a RESTful web service that outputs n numbers in the Fibonacci sequence based on the request variable INP

This document assumes that you have at least limited Linux experience.

## Requirements:
```
Python 3.6.5
pip 9.0.3
pipenv, version 2018.05.18
Flask
```

## Initialization/Installation:
1. Install Python
2. Install pip
3. Install pipenv
4. Clone the repository
```
git clone git@github.com:LarryLacy/virtustream.git
```
5. Change to the virtustream/fibonacci directory
6. Initialize your environment for Python 3
```
pipenv --three
```
7. install Flask

## Usage:
In the virtustream directory, start Flask:
```
./bootstrap.sh
```

In a second terminal execute the following where “INP” is the variable name and “8” is the desired number of digits to be returned.
```
curl -X POST  http://localhost:5000/fib?INP=8
```

## Credits, influences:
This implementation relies most heavily on:

https://auth0.com/blog/developing-restful-apis-with-python-and-flask/

Other influences

https://www.w3schools.com/python/python_while_loops.asp
https://www.digitalocean.com/community/tutorials/how-to-do-math-in-python-3-with-operators
http://hplgit.github.io/primer.html/doc/pub/looplist/._looplist-bootstrap006.html

## Background

This is my first RESTful web service and the first time I've worked with Flask. It is the second Python script I've ever written.  I initially wrote this script in bash.  The original script is fib.sh in the fibonacci directory.  Once I had the logic, I converted it to Python.  Having never worked with Flask before, it is important to note that bootstrap.sh is taken directly from the auth0 site listed above.  I've considered polishing this script but that would mean looking at other peoples versions, or asking one of my developer friends for help.  If I were to do either of those, it would not be an example of my work.  The intent of this work is to display my capability.  Because of that fact, it is important to me that this be an original work flaws and all. I recognise that it's not done the "Python" way. nor are there any security or coding "best practices". These are things I have yet to learn.


