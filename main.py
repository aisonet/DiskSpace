import os
import platform
import functions
from functions import space_call, another

if platform.system()=='Linux':
    print '------System Space Summary------'
    #space_call()
    another()

else:
    print 'Not Linux'

