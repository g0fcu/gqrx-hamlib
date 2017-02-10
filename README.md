gqrx-hamlib
A gqrx to Hamlib interface to keep frequency between gqrx and a radio in sync when using gqrx as a panadaptor using Hamlib to control the radio

Currently there are three version of this program.
- gqrx-hamlib - written in Python 2.7, this is the basis version that synchronises frequency between gqrx and Hamlib
To run it type the following on the command line in the directory where you have placed this file:
                  python ./gqrx-hamlib.py
- gqrx-hamlib-fldigi - this version written in Python 3.5 add the functionality to synchronise frequency with fldigi when run with the '-f' option. This version will be deprecated when the new GUI version has this function added (see below).
Additional Python libraries required are:
	- getopt
	- xmlrpc.client

fldigi should also have been compiled with xmlrpc support

HINT: when running configure for fldigi use the command ' ./configure --with-flxmlrpc' then you will probably 
find you have to install a couple of fltk dev libraries before the install will complete successfully.

To run it type the following on the command line in the directory whereyou have placed this file:
	
	python3.5 ./gqrx-hamlib-fldigi.py [-f]

The -f option will cause the program to tune fldigi to the gqrx frequency.
In my case Python v3.5 has to be called by the command 'python3.5'

- gqrxHamlib - this is the new GUI version, written in Python 3.5 with various options:
	- continuous bi-directional sync between gqrx & Hamlib
	- continuous sync from gqrx to Hamlib
	- one-time sync from gqrx to Hamlib
	- one-time sync from Hamlib to gqrx.
      
To build the GUI version from source you will need the following files and dependent libraries:
	
	- main.py
	- display.py
	- SIP
	- PyQt4
With the dependencies installed and the files main.py and display.py downloaded it should be possible to run the program with this command:
	
	python3.5 ./main.py
In this case my install of Python v3.5 is called python3.5
         
The Hamlib daemon (rigctld) must be running, gqrx started with the 'Remote Control via TCP' button clicked and comms to the radio working otherwise an error will occur when starting this program. Ports used are the defaults for gqrx and Hamlib.

Return codes from gqrx and Hamlib are printed to stderr, and on the GUI window.


Copyright 2017 Simon Kennedy, G0FCU, g0fcu at g0fcu.com
