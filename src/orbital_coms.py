#
#   Description: This file is the class wrapper/front end class for transmitting
#   data to and from the orbital radio
#


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
        self.temperature = "69"

        # set the defualt command
        self.Command = "NONE"

        #set debug value
        self.Debug = DEBUG

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
        return self.temperature

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
        self.temperature = inp

    # sets current command as a String
    def set_command(self,inp:str):
        """
            ***Intended for use within the class and special cases***
             Sets a new value of a command being

             Parameters:
                inp (String): New Command Value
        """
        self.Command = inp

# ------------------------------------------------------------------------------
# Special Functions
#-------------------------------------------------------------------------------

    # transmit data
    def transmit(self):
        """
            ***Potentally will be depricated***
             Transmit all values and the current command
        """
        print("Transmited!")

    # collect incoming messages and set values
    def collect(self):
        print("Transmitting values...")
        """
            ***Potentally will be depricated***
             Collect all that are in queue and update current model
        """
        print("Collecting values...")
        print("Collected!")

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
