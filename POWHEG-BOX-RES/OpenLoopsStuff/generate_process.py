#! /usr/bin/env python


import os,sys,argparse,shutil,fileinput
from subprocess import call

template = 'ProcessTemplate'
olpath = 'OpenLoops'

##############

parser = argparse.ArgumentParser(description='Generate new POWHEG-BOX+OpenLoops process')
parser.add_argument("process", action="store", help="OpenLoops amplitude library")
parser.add_argument("-order_ew", action="store", default=-1, dest="order_ew", help="perturbative order of EW coupling")
parser.add_argument("-order_qcd", action="store", default=-1, dest="order_qcd", help="perturbative order of QCD coupling")
parser.add_argument("-name", action="store", default="NewProcess", dest="name", help="name of new process")
arg = parser.parse_args()

##############

def replace(infile,old_word,new_word):
    if not os.path.isfile(infile):
        print ("Error on replace(), not a regular file: "+infile)
        sys.exit(1)

    f1=open(infile,'r').read()
    f2=open(infile,'w')
    m=f1.replace(old_word,new_word)
    f2.write(m)

##############

#Copy Template to new directory
this_path=os.path.split(os.path.realpath(__file__))[0]
process_path=this_path[:this_path.rfind('/')]+"/"+arg.name

try:
  shutil.copytree(this_path+"/"+template,process_path)
  print "Setting up a new POWHEG-BOX+OpenLoops process in: ", process_path
  print ""
except:
  print "Error! path not empty: ", process_path
  sys.exit()

# download OpenLoops amplitudes
os.chdir(this_path+"/"+olpath)
call(["./openloops", "libinstall", arg.process, "compile=0", "process_src_dir="+process_path+"/OL_process_src"])
os.chdir(this_path)

#replace <OLLIBS> in Makefile template
replace(process_path+"/Makefile","<OLLIBS>",arg.process)

#set coupling powers in init_processes.f
replace(process_path+"/init_processes.f","<ORDEREW>",str(arg.order_ew))
replace(process_path+"/init_processes.f","<ORDERQCD>",str(arg.order_qcd))

#set number of external particles in nlegborn.h
nlegbornexternal=int(arg.order_ew)+int(arg.order_qcd)+2
replace(process_path+"/nlegborn.h","<NLEGBORNEXTERNAL>",str(nlegbornexternal))

print "done."

