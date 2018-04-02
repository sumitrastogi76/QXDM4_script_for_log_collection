This is a python script which opens your QXDM application and connect the COM port and start logging
Also this captures QXDM logs with .iSF extension in the same location where it is called.

Steps to use this script:

Step 1. Run this script with COM port as a argument

example,
C:\Users\asiahyd\original $ python qxdm_logger.py 70

Output:
............................................................................................................
Initialize QXDM instance succeed...
QXDM version : QXDM04.00.203
Connected to port comm : 70
Press Enter to stop capturing logs..........
QXDM item store at : C:\Users\sumit\original\QXDM.isf
Quiting QXDM application

Step 2 : Check the log file at specified location.


Note : Let me know if this does not work.
