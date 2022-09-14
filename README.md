# Orbital Coms
##	Index
- [Usage](#usage)
- [Get Started](#get-started)
- [API Documentation](#api-documentation)
	- [Getters](#getters)
	- [Setters](#setters)
	- [Preset Communications](#preset-communication)
- [Devloper Documentation](#devloper-documentation)
	- [Serial Class](#serial-class)
		- [Getters](#serial-getters)

## Installation
1. Download this repo
2. Extract repo
3. From terminal, go into extracted directory
4. Type: ```python3 install.py``` (Requires sudo if on linux) (This also might take a while)
5. Put the the files from the src directory into you project directory
6. Enjoy!

## Get Started
Orbital coms is used to communicate to and from two radios at a great distance. Once you have imported the necessary documents to you project, we can begin writing!
Here is some stater code to get started:
```python
# We need to import the class file in order for our magic to work!
import orbital_coms

# This is the consructor for orbital coms and a start of untold power! :)
coms = orbital_coms.coms()

# Now with the coms setup, we can start transmitting things!
coms.set_temperature("69")
coms.transmit() #<- We just transmitted the temperature 69! Very noice!

coms.abort() #<- Lets hope to never use this...but this will quickly send an abort command!

# we can make a function and pass it to the radio when we get a command!
def cookie():
	print("Something went wrong...")

# We set the function cookie to be called when we get an abort command
coms.set_abort(cookie)
coms.force_abort() #<-- this will print "Something went wrong..."!
```

## API Documentation

API Documentation assumes that you already constructed the object using ```orbital_coms.coms()```

### Getters
```python
.get_command() # Returns the currently set command as a string
```
```python
.get_temperature() # Returns the currently set temperature as a string
```
```python
.get_location() # Returns the currently set location as a string ({0N,0W} format encouraged)
```
```python
.get_pressure() # Returns the currently set pressure as a string
```
### Setters
```python
.set_command(inp) # Set command as a string ***NOT ADVISED! INTENDED FOR SPECIAL CASES***
```
```python
.set_temperature(inp) # Set temperature with a string
```
```python
.set_location(inp) # Set location with a string ({0N,0W} format encouraged)
```
```python
.set_pressure(inp) # Set pressure with a string
```
```python
.set_abort(inp) # Set function to call upon reading an abort command
```
```python
.set_cut(inp) # Set function to call upon reading a cut command
```
```python
.set_launch(inp) # Set function to call upon reading a launch command
```
### Preset Communication
```python
.abort() # This will set and transmit an abort message with optimizations*
```
```python
.cut() # This will set and transmit a cut message with optimizations*
```
```python
.launch() # This will set and transmit a launch message with optimizations*
```
*optimizations means this command will gain priority and be preformed quicker than if transmitted normally

### Debug
```python
.force_abort() # This will pretend an abort command was given and run the abort code
```
```python
.force_cut() # This will pretend a cut command was given and run the cut functions
```
```python
.force_launch() # This will pretend an abort command was given and run the abort code
```
## Developer Documentation
This part of the documentation is for all developer working on this library and writing code intended to be used within the API.

### Serial Class
This class is used for direct communication to and from the radio with serialized data.
#### Serial Getters
```python
.get_radios() # This will return all radios connected to this device
```
