#!/usr/bin/python3

import os
from sys import argv

if "--dev" in argv:
    # Update the image to the latest dev version
    print('Retrieves latest version of TuxML scritps...')
    os.system('cd /TuxML/')
    os.system('git pull')
    os.system('git checkout dev')

# Run tuxml.py and retrieves the output converted in a log file.
print('Starting tuxml.py ...')
<<<<<<< HEAD
os.system('/TuxML/core/tuxml.py /TuxML/linux-4.13.3 -v 2')
=======
os.system('/TuxML/tuxml.py /TuxML/linux-4.13.3 -v 2')
>>>>>>> fa8962cb04cf83707371adef1d28c0bb7745389a
