# introduction

This is a program composed of a set of Python scripts designted to run as a cron job to track the nodes health status. 

# settings.csv

As we know, the amount of resources that should trigger a notification varies in function of the services provided. A file server in a context where the users can freely save wherever they want requires more caution than a email server with a limited number of users, with limited inbox capacity.
For that, we thought it was a sactisfatory soluction provide the program a file to store settings. The CSV (Comma Separated Value) was chosen because it is a simple way to store key value pairs. Besides, Python has a simple support for working with CSV files - inside Python, these settings are readed as dictionaries. 
Besides, mantaining an separated file for settings (in spite of it's alternative: setting variables inside scripts) is crucial to implement the following project: a web application to work as interface will allow to display and change this settings.

# log_generator.py

The script "log_generator.py" is a simple program with only two funcions designed to register in files the infomations passed. 
The "generate_log" funcion is flexible. It takes a service name, a pid (process identification), a message and the name of the file. 
This function is highly reusable, "generate_csv", on the other hand, is more specific. Although it also creates a file, this file is a CSV file. It's also more binded to the app, because it takes as arguments elements that belong to our "health check" project, creates specific keys to work as headers of a table, assign the values to these keys and saves it. 

# health_check.py

The "health_check.py" has only one funcion defined and is made to be executable. 
The function defined is "check_status" that calls functions of "psutil" module (of Pypi) and returns a set of values, in order: CPU usage (in percent, measured in 4 seconds), the root partition usage (in percent), the memory ysage (in percent) and a boolean value representing if the node is sending and receiving packages normally. 

# TO DO 

se logging package and/or ways to clear old logs.
unify the send_email to allow to write one email to all servers
