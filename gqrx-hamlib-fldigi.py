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
# This program is written in Python 3.5
# Python libraries required are:
#   - socket
#   - sys
#   - getopt
#   - time
#   - xmlrpc.client
#
# To run it type the following on the command line in the directory where
# you have placed this file:
#   python ./gqrx-hamlib-fldigi.py [-f]
#
# The -f option will cause the program to tune fldigi to the gqrx frequency.
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
import sys, getopt
import time
fldigi_option_set = 0

if len(sys.argv) > 0:
    try:
        opts, args = getopt.getopt(sys.argv, 'f',)
    except getopt.GetoptError:
        print('gqrx-hamlib.py [-f]')
        sys.exit(2)
    for index in range(len(args)):
        if args[index] == '-f':
           fldigi_option_set = 1

if fldigi_option_set == 1:
   import xmlrpc.client

TCP_IP = "localhost"
RIG_PORT = 4532
GQRX_PORT = 7356
FLDIGI_PORT = 7362

MESSAGE = ""

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
    sock.sendall(b'f\n')
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
    build_msg = 'F ' + str(freq) + '\n'
    MESSAGE = bytes(build_msg, 'utf-8')
    sock.sendall(MESSAGE)
    # Look for the response
    amount_received = 0
    amount_expected = 7 #len(message)
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
    sock.close()
    return data

if fldigi_option_set == 1:
    server = xmlrpc.client.ServerProxy('http://{}:{}/'.format(TCP_IP, FLDIGI_PORT))

while forever:
    time.sleep(0.2)
    rig_freq = getfreq(RIG_PORT)
    if rig_freq != old_rig_freq:
        # set gqrx to Hamlib frequency
        rc = setfreq(GQRX_PORT, float(rig_freq))
        print('Return Code from GQRX: {0}'.format(rc))
        old_rig_freq = rig_freq
        old_gqrx_freq = rig_freq
        
    gqrx_freq = getfreq(GQRX_PORT)
    if gqrx_freq != old_gqrx_freq:
        # set Hamlib to gqrx frequency
        rc = setfreq(RIG_PORT, float(gqrx_freq))
        print('Return Code from Hamlib: {0}'.format(rc))
        # Set fldigi to gqrx frequency
        if fldigi_option_set == 1:
            server.main.set_frequency(float(gqrx_freq))
        old_gqrx_freq = gqrx_freq
        old_rig_freq = gqrx_freq





