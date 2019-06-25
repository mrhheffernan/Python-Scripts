# A simple way to count the number of running jobs in slurm

import os
username = ''
print('Number of jobs running and in queue: ',int(os.popen('squeue -u %s').read().count('\n')-1) % (username)) 

print('Checking by another means: ',os.system('squeue -u heff1693 | wc -l'))

