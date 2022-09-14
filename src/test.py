#
#   Description: This file is used for testing the orbital_coms library
#


#  Expected Output:
#
# -----------------------------------------------------------------------
# Getters/Setters Test
# -----------------------------------------------------------------------
# test
# 62
# 30.3480N, 95.7827W
# 21
# -----------------------------------------------------------------------
# Special Functions Test
# -----------------------------------------------------------------------
# Transmited!
# ABORT
# Transmited!
# CUT




import orbital_coms

test = orbital_coms.coms()
#-------------------------------------------------------------------------------
# test setters
#-------------------------------------------------------------------------------

test.set_temperature("62")
test.set_command("test")
test.set_location("30.3480N, 95.7827W")
test.set_pressure("21")

#-------------------------------------------------------------------------------
# test getters
#-------------------------------------------------------------------------------
print("-----------------------------------------------------------------------")
print("Getters/Setters Test")
print("-----------------------------------------------------------------------")

print(test.get_command())
print(test.get_temperature())
print(test.get_location())
print(test.get_pressure())

#-------------------------------------------------------------------------------
# test special functrions
#-------------------------------------------------------------------------------
print("-----------------------------------------------------------------------")
print("Special Functions Test")
print("-----------------------------------------------------------------------")

test.abort()
print(test.get_command())


test.cut()
print(test.get_command())