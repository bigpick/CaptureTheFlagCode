def printalpha(word):
  for entry in word:
    print(alpha[int(str(entry), 2) % 26], end=' ')
  print()

with open('encoded.txt', 'r') as infile:
    given=infile.read()

zeros=given.replace("-","1").replace(".","0")
ones=given.replace("-","0").replace(".","1")
print("test1: ", ''.join(zeros.split()))
print("test2: ", ''.join(ones.split()))
