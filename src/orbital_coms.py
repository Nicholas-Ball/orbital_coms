#
#   Description: This file is the class wrapper/front end class for transmitting
#   data to and from the orbital radio
#

import serial

class coms(object):
    """coms class file for communicate to and from the launch station"""

    # constructor for orbital communications
    def __init__(self,DEBUG = False):
        super(coms, self).__init__()

        # set defualt gps location (Purdue Bell Tower)
        self.Location = "40.4273N, 86.9141W"

        # set defualt pressure reading
        self.Pressure = "1"

        # set the defualt internal temperature reading
        self.Temperature = "69"

        # set the defualt command
        self.Command = "NONE"

        # set debug value
        self.Debug = DEBUG

        # set function to preform on an abort to nothing
        self.on_abort = self.nothing

        # set function to preform on a cut message to nothing
        self.on_cut = self.nothing

# ------------------------------------------------------------------------------
# Getters
# ------------------------------------------------------------------------------

    # returns location as a String
    def get_location(self) -> str:
        """
             Get current location value

             Return:
                (String): Current Location Value
        """
        return self.Location

    # returns pressure as a String
    def get_pressure(self) -> str:
        """
             Get current pressure value

             Return:
                (String): Current Pressure Value
        """
        return self.Pressure

    # returns location as a String
    def get_temperature(self) -> str:
        """
             Get current temperature value

             Parameters:
                (String): Current temperature Value
        """
        return self.Temperature

    # returns current command as a String
    def get_command(self) -> str:
        """
             Get current command value

             Parameters:
                (String): Current Command Value
        """
        return self.Command

# ------------------------------------------------------------------------------
# Setters
# ------------------------------------------------------------------------------

    # sets location as a String
    def set_location(self,inp:str):
        """
             Sets a location value

             Parameters:
                inp (String): New Location Value
        """
        self.Location = inp

    # sets pressure as a String
    def set_pressure(self,inp:str):
        """
             Set the pressure reading

             Parameters:
                inp (String): New Pressure Value
        """
        self.Pressure = inp

    # sets location as a String
    def set_temperature(self,inp:str):
        """
             Set the internal temperature reading

             Parameters:
                inp (String): New temperature Value
        """
        self.Temperature = inp

    # sets current command as a String
    def set_command(self,inp:str):
        """
            ***Intended for use within the class and special cases***
             Sets a new value of a command being

             Parameters:
                inp (String): New Command Value
        """
        self.Command = inp

    # sets function to call upon reciving an abort command
    def set_abort(self,inp):
        """
             Set a function to be run if the command is "ABORT"

             Parameters:
                inp (Function): New abort function to set
        """
        self.on_abort = inp

    # sets function to call upon reciving a cut command
    def set_cut(self,inp):
        """
             Set a function to be run if the command is "CUT"

             Parameters:
                inp (Function): New cut function to set
        """
        self.on_cut = inp

    # sets function to call upon reciving a launch command
    def set_launch(self,inp):
        """
             Set a function to be run if the command is "LAUNCH"

             Parameters:
                inp (Function): New launch function to set
        """
        self.on_launch = inp
# ------------------------------------------------------------------------------
# Special Functions
#-------------------------------------------------------------------------------
    def nothing(self):
        """
             This is for place holding unassigned function vars
        """
        print("Wow! Much empty!")


    # transmit data
    def transmit(self):
        """
            ***Potentally will be depricated***
             Transmit all values and the current command
        """
        print("[*] Transmitting values...")
        print("[!] Transmited!")
        test = serial.serial()
        test.get_radios()

    # collect incoming messages and set values
    def collect(self):
        """
            ***Potentally will be depricated***
             Collect all that are in queue and update current model
        """
        print("[*] Collecting values...")
        print("[!] Collected!")
        print("[*] Updating values...")
        print("[!] Updated!")

    # transmit an abort message
    def abort(self):
        """
             Send an abort command
        """
        self.set_command("ABORT")
        self.transmit()

    # transmit a cut message
    def cut(self):
        """
             Send a cut command
        """
        self.set_command("CUT")
        self.transmit()
# ------------------------------------------------------------------------------
# Debug Functions
#-------------------------------------------------------------------------------

    # this function will pretend that an abort message was recived and will call on itself
    def force_abort(self):
        """
             For debuging an abort call to this system
        """
        self.on_abort()

    # this function will pretend that an abort message was recived and will call on itself
    def force_cut(self):
        """
             For debuging a cut call to this system
        """
        self.on_cut()

    # this function will pretend that an abort message was recived and will call on itself
    def force_launch(self):
        """
             For debuging a launch call to this system
        """
        self.on_launch()
