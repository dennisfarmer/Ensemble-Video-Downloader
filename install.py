#!/usr/bin/env python3

import sys
import subprocess
subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyperclip'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'PyQt5'])

# reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
# installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
# print(installed_packages)
