gqrx-hamlib
A gqrx to Hamlib interface to keep frequency between gqrx and a radio in sync when using gqrx as a panadaptor using Hamlib to control the radio

The Hamlib daemon (rigctld) must be running, gqrx started with the 'Remote Control via TCP' button clicked and comms to the radio working otherwise an error will occur when starting this program. Ports used are the defaults for gqrx and Hamlib.

Return codes from gqrx and Hamlib are printed to stderr

This program is written in Python 2.7

To run it type the following on the command line in the directory where
you have placed this file:
   python ./gqrx-hamlib.py

Only frequency is synchronised, synchronisation of e.g. mode could be added easily

I have also added a version called gqrx-hamlib-fldigi, this version is written in Python 3.5 and supports tuning of frequency on fldigi

Additional Python libraries required are:
  - getopt
  - xmlrpc.client

fldigi should also have been compiled with xmlrpc support
HINT: when running configure for fldigi use the command ' ./configure --with-flxmlrpc' then you will probably find you have to install a couple of fltk dev libraries before the install will complete successfully.

To run it type the following on the command line in the directory where
you have placed this file:
  python3.5 ./gqrx-hamlib-fldigi.py [-f]

The -f option will cause the program to tune fldigi to the gqrx frequency.
In my case Python v3.5 has to be called by the command 'python3.5'

Copyright 2017 Simon Kennedy, G0FCU, g0fcu at g0fcu.com
