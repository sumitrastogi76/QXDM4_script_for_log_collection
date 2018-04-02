###########################################################
#		Author : Sumit Rastogi							  #
#		Python Script for QXDM4 log capturing			  #
###########################################################

import time
import sys
import os
from win32com.client import Dispatch

#getting the current location where this script is called

path = os.getcwd()
port = sys.argv[1]

#initializing QXDM application
qxdm_instance = Dispatch("QXDM.QXDMAutoApplication")

if not bool(qxdm_instance):
    print("Unable to obtain ISF interface")
else:
    autoWindow = window=qxdm_instance.GetAutomationWindow()

print("Initialize QXDM instance succeed...")

# setting the window to visible mode
window.setVisible(True) # Set is false for invisible logging

# Get the QXDM version
appVer = autoWindow.APPVersion

print("QXDM version : %s"%appVer.strip())
time.sleep(5)

#Setting com port
retVal = autoWindow.SetComPort(port)

if(retVal == False):
    print("Fail to connect port : %s"%port)
else:
    print("Connected to port comm : %s"%port)

#Optional line : I am using it for holding logging session
raw_input("Press Enter to stop capturing logs..........")

#Setting filename of .ISF file
filename = r"\QXDM.isf"

#Saving QXDM Items in .ISF file at same location where this script is called
res = autoWindow.SaveItemStore("%s%s"%(path,filename))

if res == 1:
    print("QXDM item store at : %s%s "%(path,filename))

time.sleep(5)

#Closing QXDM application
autoWindow.QuitApplication()
print("Quiting QXDM application")