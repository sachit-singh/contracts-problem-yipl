contracts-problem-yipl
======================

First, create a virtualenv using mkvirtualenv env_name command, where env_name is the name of the virtual environment.

Then run the following command:

	pip install -r requirements.txt

which will install all the required modules (only 1 in this case)

After the installation is complete run "python metal.py" command to run the script.

A file named 'final.csv' will be created containing all data combined from 'awards.csv' and 'contracts.csv'.

The result:
	The total amount of closed awarded contracts is 700000

will displayed on the terminal, which is the required value of the Total amount of closed awarded contracts.



Note
====

Sometimes a 'GeocoderTimeOut' error is raised, due to no response from the server. But I think it also occurs due to a slow connection.
It is not a problem with the script. It is caused due to the internet connection. So, if you encounter such errors or any other error, try running "python metal.py" a few times.