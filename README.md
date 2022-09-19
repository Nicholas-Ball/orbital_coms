
# Orbital Coms
# Index
- [Installation](#usage)
- [Get Started](#get-started)
- [API Documentation](#api-documentation)
	- [LS & GS](#ls-and-gs)
		- [Common Methods](#common-methods)
		- [Common Flags](#common-flags)
	- [GS](#gs)
		- [Getters-GS](#getters-gs)
		- [Flags](#flags-gs)
	- [LS](#ls)
		- [Senders-LS](#senders-ls)
		- [Flags](#flags-ls)
- [Devloper Documentation](#devloper-documentation)
	- [Serial Class](#serial-class)
		- [Getters](#serial-getters)

# Installation
1. Download this repo
2. Extract repo
3. From terminal, go into extracted directory
4. Type: ```python3 install.py``` (Requires sudo if on linux) (This also might take a while)
5. Put the the files from the src directory into you project directory
6. Enjoy!

# Get Started
Orbital coms is used to communicate to and from two radios at a great distance. Once you have imported the necessary documents to you project, we can begin writing!
Here is some stater code for LS to get started:
```python
# First we need to import the ls program! (Of course, if you are using gs, replace ls with gs)
import ls

# Dont worry about this for now. Keep reading to see what this does later
def cookie()
	print("Yum!")

l = ls.ls(True) # This starts ls program in debug mode!

l.send_temperature(62.0) # This will send 62.0 as its temperature
l.send_location("30.3480N, 95.7827W") # This will send its location
l.send_pressure(21.0) # This will send 21.0 to the ground station as ts current pressure

l.subscribe(ls.Events.ABORT,cookie) # When the radio gets an abort message, cookie is called

l.start() # This will start the radio and run the code in a pipe line!
# NOTE: Any code here WILL NOT RUN unless you do l.start() in another thread
```

# API Documentation

API Documentation assumes that you already constructed the object using ```ls.ls()``` or ```gs.gs()```

## LS and GS
### Common Methods
```python
.subscribe(Flag,Function) # When this program has a instance of the flag being raised, the function set will be run
```
```python
.start() # This will start the program (Has to be done in order to work)
```
### Common Flags
```python
.Event.UPDATE # This flag tells the program to run the function at the end of each cycle (~24 times a second)
```
```python
.Event.FALL # This flag tells the program in the event of no subscribed event is set, run this program instead
```
## GS
### Getters-GS
```python
.get_temperature() # Returns the currently set temperature as a string
```
```python
.get_location() # Returns the currently set location as a string ({0N,0W} format encouraged)
```
```python
.get_pressure() # Returns the currently set pressure as a string
```
### Flags-GS
```python
.Event.LOCATION # This flag tells the program to run a function when the GS gets a location command (Location will be set automatically)
```
```python
.Event.PRESSURE # This flag tells the program to run a function when the GS gets a pressure command (Pressure will be set automatically)
```
```python
.Event.TEMPERATURE # This flag tells the program to run a function when the GS gets a pressure command (Pressure will be set automatically)
```

## LS
### Senders-LS
```python
.send_temperature(inp) # Sends the temapture to GS
```
```python
.send_location(inp) # Send Location to GS
```
```python
.send_pressure(inp) # Send pressure to GS
```
### Flags-LS
```python
.Events.ABORT # Run a function upon reciving an abort command
```
```python
.Events.CUT # Run a function upon reciving a cut command
```
```python
.Events.LAUNCH # Run a function upon reciving an launch command
```
# Developer Documentation
This part of the documentation is for all developer working on this library and writing code intended to be used within the API.

## Serial Class
This class is used for direct communication to and from the radio with serialized data.

### Serial Methods
```python
.start() # This will start the serial communication to and from the radio
```
```python
.transmit(data) # This will transmit a given serialized set of data to the radio
```
```python
.collect() # This will collect data that has been recived by the radio and return it
```

### Serial Global Vars
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
