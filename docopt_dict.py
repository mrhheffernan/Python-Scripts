"""Usage: docopt_dict.py [--entry1=N] [--entry2=N] [--entry3=N] [--entry4=N] 

Options:
    --entry1=N Optional argument, replaces value of entry1
    --entry2=N Optional argument, replaces value of entry2
    --entry3=N Optional argument, replaces value of entry3
    --entry4=N Optional argument, replaces value of entry4
"""

from docopt import docopt

arguments = docopt(__doc__,version='version')
# We could also update simple variables from defaults using an analogous method

entry1 = 600.0
entry2 = 150.0
entry3 = 1.0
entry4 = 1e-03

if arguments['--entry1'] is not None:
    entry1 = arguments['--entry1']
    print('variable entry1 updated!')

if arguments['--entry2'] is not None:
    entry2 = arguments['--entry2']
    print('variable entry2 updated!')
    
if arguments['--entry3'] is not None:
    entry3 = arguments['--entry3']
    print('variable entry3 updated!')
    
if arguments['--entry4'] is not None:
    entry4 = arguments['--entry4']
    print('variable entry4 updated!')

print('entry1 = ',entry1,'entry2 = ',entry2,'entry3 = ',entry3,'entry4 = ',entry4)



# Using a dictionary is often advantageous for string replacements.
# Now, with a wrapper script, variables in a non-Python script can be updated

dictionary = {'entry1':600.0,'entry2':150.0,'entry3':1,'entry4':1e-03}

if arguments['--entry1'] is not None:
    dictionary['entry1'] = arguments['--entry1']
    print('dictionary entry1 updated!')

if arguments['--entry2'] is not None:
    dictionary['entry2'] = arguments['--entry2']
    print('dictionary entry2 updated!')
    
if arguments['--entry3'] is not None:
    dictionary['entry3'] = arguments['--entry3']
    print('dictionary entry3 updated!')
    
if arguments['--entry4'] is not None:
    dictionary['entry4'] = arguments['--entry4']
    print('dictionary entry4 updated!')

print('dictionary: ',dictionary)

# Here, I demonstrate string replacement in a queue submission script

import os

# First, we have to rename some variables so they make steps
nsteps = entry1
Tmin = entry2
cores = entry3
step = entry4

for i in range(nsteps+1):
    T = int(Tmin + i*step)
    filename = 'etaT'+str(T)+'c'+str(cores)
    qsubname = 'qsub_'+filename+'.pbs'
    outputfilename = 'RT_'+filename
    errorfilename = 'RT_'+filename
    params_update = {'Temp':T,'cores':cores,'output':outputfilename,'error':errorfilename,'name':filename}

    f_in = open('qsub_parent.pbs').read()
    f_out = open(qsubname,'w')
    f_out.write(f_in % params_update)
    f_out.close()
    os.system('qsub '+ qsubname)