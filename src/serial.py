#
#   This holds data about serial connecto and from the radio
#

# Soapy is the program we use for serial communication to and from the radio
import SoapySDR
from SoapySDR import *
import numpy

class serial(object):
    """serial is a wrapper for SoapySDR and makes it easy for sending of serialized data to and from the radio"""

    def __init__(self):
        super(serial, self).__init__()

    def get_radios(self):
        results = SoapySDR.Device.enumerate()
        for result in results:
            print(result)
