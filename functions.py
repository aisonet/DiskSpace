import os

from subprocess import PIPE, Popen

def space_call():
    summary= os.system("df -h")
    print type(summary)
    print('----------------------------------------------------')
    print summary
    #print 'Space'

def cmdline(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]



def another():
    out=cmdline('df -h')
    print out.split(' ', -1)