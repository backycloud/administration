#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os, sys; #Импортирование os, sys

print ('For Server connection type number of server, more information type: L')


if len(sys.argv) < 2:
 x = raw_input('Enter server number: ');
else:
 x = (sys.argv[1])
if x == 'worker' :
 os.system('rdesktop worker.test.ru -g 1830x1000 2>/dev/null &')
# print('Connecting to worker.2000.strat.ru server.')
# print('>>>')
# print('>>>')
# os.system ('python server/worker.py');
elif x == 'weber' :
 os.system('rdesktop weber.test.ru -g 1830x1000 2>/dev/null &')
# print('Connecting to weber.2000.strat.ru server.')
# print('>>>')
# print('>>>')
# os.system ('python server/weber.py');
else:
     	print('Error information')
