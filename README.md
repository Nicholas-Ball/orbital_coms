
# Orbital Coms
##	Index
- [Usage](#usage)
- [Get Started](#get-started)
- [API Documentation](#api-documentation)
	- [Getters](#getters)
	- [Setters](#setters)
	- [Preset Communications](#preset-communication)

## Usage
Just copy everything from the src folder into your program!

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
coms.transmit() #<- We just transmited the temperature 69! Very noice!

coms.abort() #<- Lets hope to never use this...
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
### Preset Communication
```python
.abort() # This will set and transmit an abort message with optimizations*
```
```python
.cut() # This will set and transmit a cut message with optimizations*
```
*optimizations means this command will gain priority and be preformed quicker than if transmitted normally
