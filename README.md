## Synopsis

This project is a python web application to solve the divisibility problem available [here](www.spoj.com/problems/SMPDIV).


## Dependencies

This application depends heavily on the micro framework Flask and python 2.7, for more detailed install instructions please refer to the framework's official install [guide](http://flask.pocoo.org/docs/0.11/installation/). On a ubuntu based system with [pip](https://pip.pypa.io/en/stable/), a system wide install can be done with:

```
$sudo pip install flask
```

## Running

To run the application simply run:

```
../anchor$ python run.py
```

The application should be available at http://localhost:5000

## Tests

To run all the tests simply run:

```
../anchor$ python -m unittest discover
```

## Input

Input should be formatted as described in the problem description and provided as a text (.txt) file to be upload to the application.


## Project structure

The project is structured as a major package (divisibility) with core components organized as modules such as the following:

Module | Purpose
------ | -------
config | Core constants and default messages
division | Division related operations
exception | Application's internal exceptions
parser | Input parsing related operations
validator | Input validation operations
views | Application's endpoints treatment and routing

Templates are served from the /templates folder.


## Design

This application was designed with the goal of being functional yet simple, thus the choice Flask framework, known for its small footprint and great extendability. Code modularity is achieved by the means of python modules and classes are avoided where there is no strong entity feeling. The main pipeline is:

1) Views serves the index page and receives the upload file after a POST on /upload.  
2) File's extension is verified.  
3) Input is parsed and validated according the problem description by the parser and validator modules. If there is any problem with the data a Exception is raised and the feedback is returned to the user.  
4) Once the input is parsed and clean, division module is called for each input entry.  
5) Output is returned to user.  

The core functionality, the divisibility is achieved by verifying for each number int the range if it's divisible by x and not divisible by y. Although other ways are possible (such as computing the union difference between the divisible sets for x and y) this was chose for the better performance and overall simplicity.


##Assumptions

1)The application is mostly used in a light way, with few inputs and small ranges, better knowledge of the expected load of the application and expected input can be used to tune user experience.  
2)The data may be unformatted.  
3)Only numbers within the description range are accepted.  
4)User should receive feedback with the input is problematic (a more organic feedback may be achieved using Javascript).  
5)The output must be calculated on the fly and not stored.  
6)Application should not have access restrictions (since it does not deal with sensitive information).  


## License

Apache 2.0, you know the drill ;)
