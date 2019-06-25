# PythonApps: A collection of scripts in development

## VEGAS adaptive Monte Carlo add ons

###### vegas_tests.py
This script demonstrates the different ways of performing multidimensional integration in VEGAS and shows the advantages over SciPy for naive nesting.

###### vegas_returns.py
In large-volume applications, sometimes VEGAS objects are returned in two different data types, making this hard to handle directly. This script provides functions for calling the mean result and the estimated error for both types, solving this issue.

## General python add ons

###### docopt_dict.py
Passing arguments from the command line can be extremely useful, especially when a python "master" is being used to write string replacements to a script in another language, such as C or Fortran. This example shows a quick way to implement this.

###### quadsum.py
Absolute errors on quantities with uncertainty add in quadrature. A short, but useful function can be written to handle this rather than adding it in every script.

###### umat_mean.py
Taking the element-wise mean of umatricies from the uncertainties.unumpy package is not a built in functionality. This rectifies that by using numpy to calculate the mean and then recompiles the result into a umatrix.

###### queuelength.py
This is a simple way to count the current number of running jobs for a particular user in a SLURM queue
