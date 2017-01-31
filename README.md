# gqrx-hamlib
A gqrx to Hamlib interface to keep frequency between gqrx and a radio in sync when using gqrx as a panadaptor using Hamlib to control the radio

The Hamlib daemon (rigctld) must be running, gqrx started with the 'Remote Control via TCP' button clicked and comms to the radio working otherwise an error will occur when starting this program. Ports used are the defaults for gqrx and Hamlib.

Return codes from gqrx and Hamlib are printed to stderr

This program is written in Python 2.7

To run it type the following on the command line in the directory where
you have placed this file:
   python ./gqrx-hamlib.py

Only frequency is synchronised, synchronisation of e.g. mode could be added easily

Copyright 2017 Simon Kennedy, G0FCU, g0fcu at g0fcu.com
