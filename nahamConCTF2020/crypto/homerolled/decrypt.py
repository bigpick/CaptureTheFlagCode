import base64
count = 0
cipher_b64 = b"MTAwLDExMSwxMDAsOTYsMTEyLDIxLDIwOSwxNjYsMjE2LDE0MCwzMzAsMzE4LDMyMSw3MDIyMSw3MDQxNCw3MDU0NCw3MTQxNCw3MTgxMCw3MjIxMSw3MjgyNyw3MzAwMCw3MzMxOSw3MzcyMiw3NDA4OCw3NDY0Myw3NTU0MiwxMDAyOTAzLDEwMDgwOTQsMTAyMjA4OSwxMDI4MTA0LDEwMzUzMzcsMTA0MzQ0OCwxMDU1NTg3LDEwNjI1NDEsMTA2NTcxNSwxMDc0NzQ5LDEwODI4NDQsMTA4NTY5NiwxMDkyOTY2LDEwOTQwMDA="

def a(num):
    if (num > 1):
        for i in range(2,num):
            if (num % i) == 0:
                return False
                break
        return True
    else:
        return False

def b(num):
    my_str = str(num)
    rev_str = reversed(my_str)
    if list(my_str) == list(rev_str):
       return True
    else:
       return False


cipher = base64.b64decode(cipher_b64).decode().split(",")

with open('b002385.txt', 'r') as infile:
    palindrome_primes = infile.readlines()
    palindrome_primes = [int(x.strip().split()[1]) for x in palindrome_primes]

prime_idx = 0
primes = []
done = False
while(count < len(cipher)):
    #if (a(num)):
    for num in palindrome_primes[prime_idx:]:
        if count >=13 and count < 26:
            if num < 50000: continue
        elif count >= 26:
            if num < 500000: continue

        if (b(num)):
            print(chr(int(cipher[count]) ^ num), end='', flush=True)
            primes.append(num)
            if chr(int(cipher[count]) ^ num) == "}": done = True
            count += 1
            #if (count == 13):
            #    num = 50000
            #if (count == 26):
            #    num = 500000
        else:
            prime_idx += 1

        if done: break

print()
print(f"Primes used: {' '.join(map(str, primes))}")
