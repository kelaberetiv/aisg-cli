# AISG CLI Tool - https://www.aisingapore.org #

# import required modules
import sys
import subprocess

# get arguments from shell entry point
arguments = sys.argv
arguments.pop(0)

# parse arguments into commands
# WIP - depend on use cases
commands = arguments

# run commands and get output
commands_output = subprocess.check_output(arguments)

# parse output accordingly
# WIP - depend on use cases
parsed_output = commands_output

# print parsed output
print(parsed_output)
