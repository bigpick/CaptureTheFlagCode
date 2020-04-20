from pwn import *
import os
import socket

# Set up stuff for Stage 5
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "\xde\xad\xbe\xef"

# We need argc to be 100
arglist = ["A"] * 99
# we need argv['A'] and 'B' to have a certain value
# but also need to account for the file name itself being the first arg
arglist[ord("A")-1] = "\x00"
arglist[ord("B")-1] = "\x20\x0a\x0d"
arglist[ord("C")-1] = "5005"

# For stage 2, we need a file for stderr
stderr_file = open("stderr_file", "w")
stderr_file.write("\x00\x0a\x02\xff")
stderr_file.close()
# For stage 4, we need a file to read from:
with open('\x0a', 'w') as outfile:
  outfile.write("\x00\x00\x00\x00")


# ./input arglist[1] arglist[2] ...
process = process(["/home/input2/input"]+arglist, stderr = open("stderr_file"), env={"\xde\xad\xbe\xef":"\xca\xfe\xba\xbe"})

# Stage 1
print(process.recvuntil(b'Stage 1 clear!\n').decode('utf-8'))

# Stage 2
process.sendline("\x00\x0a\x00\xff")
# We already set up the stderr pipe+file
print(process.recvuntil(b'Stage 2 clear!\n').decode('utf-8'))

# Stage 3
# We already set up the env variable
print(process.recvuntil(b'Stage 3 clear!\n').decode('utf-8'))

# Stage 4
# We already set up the \x0a file and contents
print(process.recvuntil(b'Stage 4 clear!\n').decode('utf-8'))

# Stage 5
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
print(process.recvuntil(b'Stage 5 clear!\n').decode('utf-8'))
s.close()
print(process.recvline().decode('utf-8'))
