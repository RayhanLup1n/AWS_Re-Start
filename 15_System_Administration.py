# Testing komunikasi dengan os menggunakan module 'os'
import os

print("Hasil syntax menggunakan module 'os': ")
os.system('ls')
print("======================================================")

# Testing komunikasi dengan os menggunakan module 'subprocess'
import subprocess
print("Hasil syntax menggunakan module 'subprocess': ")
subprocess.run(['ls', '-l', 'AsamAmino/'])
print("======================================================")


command = 'ls'
arguments = '-a'
subprocess.run([command, arguments])
print("======================================================")


command = 'ps'
arguments = '-x'
subprocess.run([command, arguments])
print("======================================================")

command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])