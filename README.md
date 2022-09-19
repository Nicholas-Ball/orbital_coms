
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

API Documentation assumes that you already constructed the object using ```ls.ls()``` or ```gs.gs()```

### LS & GS
#### Common Methods
```python
.subscribe(Flag,Function) # When this program has a instance of the flag being raised, the function set will be run
```
```python
.start() # This will start the program (Has to be done in order to work)
```
#### Common Flags
```python
.Event.UPDATE # This flag tells the program to run the function at the end of each cycle (~24 times a second)
```
```python
.Event.FALL # This flag tells the program in the event of no subscribed event is set, run this program instead
```
### GS
#### Getters-GS
```python
.get_temperature() # Returns the currently set temperature as a string
```
```python
.get_location() # Returns the currently set location as a string ({0N,0W} format encouraged)
```
```python
.get_pressure() # Returns the currently set pressure as a string
```
#### Flags - GS
```python
.Event.LOCATION # This flag tells the program to run a function when the GS gets a location command (Location will be set automatically)
```
```python
.Event.PRESSURE # This flag tells the program to run a function when the GS gets a pressure command (Pressure will be set automatically)
```
```python
.send_temperature(inp) # Sends the temapture to GS
```

### LS
#### Senders-LS
```python
.send_temperature(inp) # Sends the temapture to GS
```
```python
.send_location(inp) # Send Location to GS
```
```python
.send_pressure(inp) # Send pressure to GS
```
```python
.set_abort(inp) # Set function to call upon reading an abort command
```
#### Flags - LS

## Developer Documentation
This part of the documentation is for all developer working on this library and writing code intended to be used within the API.

### Serial Class
This class is used for direct communication to and from the radio with serialized data.

#### Serial Methods
```python
.start() # This will start the serial communication to and from the radio
```
```python
.transmit(data) # This will transmit a given serialized set of data to the radio
```
```python
.collect() # This will collect data that has been recived by the radio and return it
```

#### Serial Global Vars
```python
RX_CHANNEL # This is the channel where the radio will read for incoming transmission
```
```python
RX_FREQENCY # This is the freqency where the radio will read for incoming transmission
```
```python
TX_CHANNEL # This is the channel where the radio will write for outgoing transmissions
```
```python
TX_FREQENCY # This is the freqency where the radio will write for outgoing transmission
```
