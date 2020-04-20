# [Single-byte XOR cipher](https://cryptopals.com/sets/1/challenges/3)

The hex encoded string:

```
1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
```

... has been XOR'd against a single character. Find the key, decrypt the message.

You can do this by hand. But don't: write code to do it for you.

How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. Evaluate each output and choose the one with the best score.

> Achievement Unlocked:
>
> You now have our permission to make "ETAOIN SHRDLU" jokes on Twitter.

# Solve

```
./chall3.py 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
Possible entries, sorted by least-likely-gibberish to most-likely-gibberish:
cOOKINGmcSLIKEAPOUNDOFBACON
Cooking MC's like a pound of bacon
iEEACDM
Yi
FCAO
K
ZE_DN
EL
HKIED
Ieeacdm*GI-y*fcao*k*zedn*el*hkied
oCCGEBK
       ao
         _
          @EGI
              M
               \CYBH
                    CJ
                      NMOCB
Occgebk,AO+,`egi,m,|cybh,cj,nmocb
SSWUR[qPUWY]LSIRXSZ^]_SR
```
