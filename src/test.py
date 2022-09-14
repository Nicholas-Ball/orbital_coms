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
# [*] Transmitting values...
# [!] Transmited!
# ABORT
# [*] Transmitting values...
# [!] Transmited!
# CUT
# -----------------------------------------------------------------------
# On-Call Functions Test
# -----------------------------------------------------------------------
# I have been summoned!


# This function is for testing command calls
def summon():
    print("I have been summoned!")


import ls
import gs

g = gs.gs()
l = ls.ls()

#-------------------------------------------------------------------------------
# test ls
#-------------------------------------------------------------------------------
print("-----------------------------------------------------------------------")
print("LS Test")
print("-----------------------------------------------------------------------")

l.send_temperature(62.0)
l.send_command("test")
l.send_location("30.3480N, 95.7827W")
l.send_pressure(21.0)

#-------------------------------------------------------------------------------
# test gs
#-------------------------------------------------------------------------------
print("-----------------------------------------------------------------------")
print("GS Test")
print("-----------------------------------------------------------------------")

print(g.get_command())
print(g.get_temperature())
print(g.get_location())
print(g.get_pressure())

#-------------------------------------------------------------------------------
# test special functrions
#-------------------------------------------------------------------------------
# print("-----------------------------------------------------------------------")
# print("Special Functions Test")
# print("-----------------------------------------------------------------------")

# test.abort()
# print(test.get_command())


# test.cut()
# print(test.get_command())

#-------------------------------------------------------------------------------
# test on-call functrions
#-------------------------------------------------------------------------------
# print("-----------------------------------------------------------------------")
# print("On-Call Functions Test")
# print("-----------------------------------------------------------------------")

# test.force_abort()
