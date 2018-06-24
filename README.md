# Fibonacci

This is a RESTful web service that outputs n numbers in the Fibonacci sequence based on the request variable INP

This document assumes that you have at least limited Linux experiance.

## Requirements:

Python 3.6.5
pip 9.0.3
pipenv, version 2018.05.18
Flask

## Usage:
Start Flask:
```
./bootstrap.sh
```

In a second terminal execute the following where “INP” is the variable name and “8” is the desired number of digits to be returned.
```
curl -X POST  http://localhost:5000/fib?INP=8
```

## Credits, influences and background:

https://auth0.com/blog/developing-restful-apis-with-python-and-flask/
https://www.w3schools.com/python/python_while_loops.asp
https://www.digitalocean.com/community/tutorials/how-to-do-math-in-python-3-with-operators
http://hplgit.github.io/primer.html/doc/pub/looplist/._looplist-bootstrap006.html



