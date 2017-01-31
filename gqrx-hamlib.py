# gqrx-hamlib - a gqrx to Hamlib interface to keep frequency
# between gqrx and a radio in sync when using gqrx as a panadaptor
# using Hamlib to control the radio
#
# The Hamlib daemon (rigctld) must be running, gqrx started with
# the 'Remote Control via TCP' button clicked and
# comms to the radio working otherwise an error will occur when
# starting this program. Ports used are the defaults for gqrx and Hamlib.
#
# Return codes from gqrx and Hamlib are printed to stderr
#
# This program is written in Python 2.7
# To run it type the following on the command line in the directory where
# you have placed this file:
#   python ./gqrx-hamlib.py
#
# Copyright 2017 Simon Kennedy, G0FCU, g0fcu at g0fcu.com
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import socket
import sys
import time

TCP_IP = "localhost"
RIG_PORT = 4532
GQRX_PORT = 7356

MESSAGE = "f\n"

forever = 1
rig_freq = 0
gqrx_freq = 0
old_rig_freq = 0
old_gqrx_freq = 0

def getfreq(PORT):
    sock = socket.socket(socket.AF_INET, 
                     socket.SOCK_STREAM) 
    # Bind the socket to the port
    server_address = (TCP_IP, PORT)
    sock.connect(server_address)
    sock.sendall(MESSAGE)
    # Look for the response
    amount_received = 0
    amount_expected = 8 #len(message)
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
    sock.close()
    return data

def setfreq(PORT, freq):
    sock = socket.socket(socket.AF_INET, 
                     socket.SOCK_STREAM) 
    # Bind the socket to the port
    server_address = (TCP_IP, PORT)
    sock.connect(server_address)
    sock.sendall("F " + freq + '\n')
    # Look for the response
    amount_received = 0
    amount_expected = 7 #len(message)
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
    sock.close()
    return data

while forever:
    time.sleep(0.2)
    rig_freq = getfreq(RIG_PORT)
    if rig_freq != old_rig_freq:
        rc = setfreq(GQRX_PORT, rig_freq)
        print >>sys.stderr, 'Return Code from GQRX: "%s"' % rc
        old_rig_freq = rig_freq
        old_gqrx_freq = rig_freq
        
    gqrx_freq = getfreq(GQRX_PORT)
    if gqrx_freq != old_gqrx_freq:
        rc = setfreq(RIG_PORT, gqrx_freq)
        print >>sys.stderr, 'Return Code from Hamlib: "%s"' % rc
        old_gqrx_freq = gqrx_freq
        old_rig_freq = gqrx_freq





