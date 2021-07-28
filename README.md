# CARDANO ROVER EXPERIENCE

Thank you for sending the test I really enjoyed playing with CARDANO's ROVER.

This solution is inspired in the project flask-blueprints which is a template to use
flask in a framework-ish way. As its name implies it (ab)uses flask's blueprints.

To make it simpler for you to run I left a server with the solution working at:

http://morangodynamic.mooo.com:5000

I can provide shell access to it if you are interested in running tests 


Get the source code:

    git@github.com:HBalija/flask-blueprints.git


App is divided into two blueprints, site and api. They both use the same
context defined in `config/base.py` settings file, along with other
settings variables which can be defined in separate `.env` file.
Other variables can be easily added in the same manner.
That way, settings are easily adjustable for both develompment and
production purposes.

Tests use their settings, hardcoded inside `config/test.py`.
`Tests.py` defines a location for the test loader to search for tests, as well
as settings for coverage.

Please feel free to reach out and ask for a server reset in case it crashes (hopefully not but I deployed it yesterday and it has experienced chinese bot attacks already)

## Quick start


Navigate to cardano-blueprints folder:

    cd cardano-blueprints

Create a `python3` virtual environment:

    virtualenv --python=/usr/bin/python3 venv

* I strongly suggest using python 3.8 which is the version I used for coding this

Source virtual env

    source ./venv/bin/activate

Install requirements:

    pip install -r requirements.txt

Create `.env` file and set variales as shown in env,sample. (i left it there for you to use)

## Running app

To start develoment server, run:

    ./run.py

Navigate to:

    127.0.0.1:5000

## Running tests

To run tests, run:

    ./tests.py


## test results
    Name                                             Stmts   Miss Branch BrPart  Cover
    ----------------------------------------------------------------------------------
    app/__init__.py                                     12      0      0      0   100%
    app/api/__init__.py                                  2      0      0      0   100%
    app/api/routes.py                                   13      2      6      5    63%
    app/controllers/command_executer.py                 64      0     24      1    99%
    app/grid.py                                         41     12     14      2    75%
    app/modules/__init__.py                              0      0      0      0   100%
    app/modules/command_parser.py                       42     16      8      2    64%
    app/modules/command_protocol.py                     16      0      8      1    96%
    app/modules/rover_movement.py                       11      1      4      0    93%
    app/rover.py                                         7      0      0      0   100%
    app/site/__init__.py                                 2      0      0      0   100%
    app/site/routes.py                                  11      3      6      5    53%
    app/tests/test_api.py                               16      2      0      0    88%
    app/tests/test_controllers_command_executer.py      84      0      0      0   100%
    app/tests/test_grid.py                              95      0      0      0   100%
    app/tests/test_modules_command_parser.py            61      1      0      0    98%
    app/tests/test_modules_command_protocol.py          14      0      0      0   100%
    app/tests/test_modules_rover_movement.py            17      0      0      0   100%
    app/tests/test_rover.py                             14      0      0      0   100%
    ----------------------------------------------------------------------------------
    TOTAL                                              522     37     70     16    91%
    Ran 48 tests in 0.031s

As you can see coverage is good, but there are some inherited code that I did not test and also some complains
from the coverage that are false positives. With a little effort It would be easy to raise the coverage meassure. 


# Solution analisis

* I like the overall result, the code uses principles of clean architecture trying to have technology far from use cases and entities.

* Main mechanisms were written using concepts of functional programming (pure functions) for easier testing and you can find it under
    /app/modules

* The logic that glues everything together was implemented in the controller under
   /app/controllers

* I simulated entities as models that would be stored in a database for a real world web app. 

# Cons of the solution

* I intentionally left a couple of flaws just to be able to create this section.

* The angle is an ever increasing (depends on the command) value, and it could overflow causing unpredictable results (not tested). This could be easily improved by using modular aritmetics rather than plain math. 

* UI could improve, I wanted to keep it as simple as possible. But you should be able to use it and verify.

* This could be packaged in a docker container or a nix description to make it simpler to deploy and implement. 

* Some assertions share tests, there are different opinions about this. I did it because it saved time to implement this way.

* Test folder structure is not ideal, but good enough for these requirements.
