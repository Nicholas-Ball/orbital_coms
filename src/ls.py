class ls():
    def __init__(self,DEBUG = False):
            super(ls, self).__init__()

    # sends location as a String
    def send_location(self,inp:str):
        """
             Sets a location value

             Parameters:
                inp (String): New Location Value
        """
        print("[*] Sending location...")
        print("[!] Location sent!")

    # sends pressure as a float
    def send_pressure(self,inp:float):
        """
             Set the pressure reading

             Parameters:
                inp (String): New Pressure Value
        """
        print("[*] Sending pressure...")
        print("[!] Pressure sent!")

    # sends location as a float
    def send_temperature(self,inp:float):
        """
             Set the internal temperature reading

             Parameters:
                inp (String): New temperature Value
        """
        print("[*] Sending temperature...")
        print("[!] Temperature sent!")

    # send a custom command
    def send_command(self,inp:str):
        """
            ***Intended for use within the class and special cases***
             Sets a new value of a command being

             Parameters:
                inp (String): New Command Value
        """
        print("[*] Sending command...")
        print("[!] Command sent!")
