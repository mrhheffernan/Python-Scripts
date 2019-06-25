# A simple way to count the number of running jobs in slurm

import os
username = ''
print('Number of jobs running: ',os.popen('squeue -u %s').read().count('\n') % (username)) # don't need to add 1 for the last line with no \n since the first line returned isn't a job, therefore compensating for this

