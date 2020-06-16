# Various Capture The Flag competitions' worth of exploits
Also, a listing of some of the tools and resources I've found especially useful.

**[See this page for nice list of tool binaries](https://github.com/zardus/ctf-tools)**.

 * It's [Docker instructions...](https://github.com/zardus/ctf-tools#docker-version-17)

    <details><summary>Show</summary>
    <br>

    ```bash
    git clone https://github.com/zardus/ctf-tools
    cd ctf-tools
    docker build -t ctf-tools .
    docker run --rm -i -d --name ctftools ctf-tools
    docker exec -it ctftools /bin/bash
    ```

    Then once inside, switch to Python3 by default:

    ```bash
    # Drop out of default Python2.7 venv
    deactivate

    # Source Python3 dir
    source $HOME/.virtualenvs/ctftools3/bin/activate

    # set up the path
    /home/ctf/tools/bin/manage-tools setup
    source ~/.bashrc
    ```

    ### Useful baseline build

    ```bash
    manage-tools -s install pwntools
    ```

    ##### `manage-tools` commands

    ```bash
    manage-tools list

    # install gdb, allowing it to try to sudo install dependencies
    manage-tools -s install gdb

    # install pwntools, but don't let it sudo install dependencies
    manage-tools install pwntools

    # install qemu, but use "nice" to avoid degrading performance during compilation
    manage-tools -n install qemu

    # uninstall gdb
    manage-tools uninstall gdb

    # uninstall all tools
    manage-tools uninstall all

    # search for a tool
    manage-tools search preload
    ```

    </details>

# Crypto
### Online
* [CyberChef](https://gchq.github.io/CyberChef/) -- "The Cyber Swiss Army Knife", analysing and decoding data.
* [ROT5, ROT13, ROT18, and ROT47 cipher re/unshift](https://www.qqxiuzi.cn/bianma/ROT5-13-18-47.php).
* [QuipQuip](https://quipqiup.com/) -- Automated substitution/vigenere cipher solver w/out key.
* [Automated cipher identifier attempt](https://www.boxentriq.com/code-breaking/cipher-identifier).
* [Walkthrough of cryptanalysis methods](http://practicalcryptography.com/cryptanalysis/).
* [FactorDB](http://factordb.com/) -- Pretty much handles/factors any entry level RSA problem.
* [WolframAlpha Factorizer](https://www.wolframalpha.com/input/?i=factorize) -- Not as great as FactorDB, but will sometimes handle/factor entry level RSA problems.
* [Vigenere Solver (auto)](https://www.guballa.de/vigenere-solver) -- Automated vigenere key cracker.
* [Substition Solver (auto)](https://www.guballa.de/substitution-solver) -- Automated substitution cipher cracker.
* [Rumkin Cryptogram Solver](http://rumkin.com/tools/cipher/cryptogram-solver.php) -- quipquip cryptogram alternative.
* [Hash type identifier (MD4 vs MD5 vs SHA256 vs etc...](https://www.tunnelsup.com/hash-analyzer/) -- good for identifying password hash types for feeding to haschat/john.

### Local Applications
* [CyberChef (docker container)](https://hub.docker.com/r/remnux/cyberchef/)

    ```
    docker pull remnux/cyberchef
    sudo docker run -d -p 8080:8080 remnux/cyberchef
    # docker ps | grep cyberchef then docker stop/rm
    ```

* [xortool](./tools/xortool) -- brute force XOR against strings or documents.
* [RsaCtfTool](./tools/RsaCtfTool) -- _Lots_ of options for RSA things.
* [jwt_tool](./tools/jwt_tool) -- Interactive tool for forging and fiddling with JWT tokens.
  * Another option for JWT fiddlingin python - [PyJWT](https://pypi.org/project/PyJWT/1.4.0/) - install via pip.
* [FactorDB python library](https://pypi.org/project/factordb-pycli/) -- Same as online factorDB, but from Python!

    ```python
    from factordb.factordb import FactorDB

    def check_factordb(N):
      factorized = FactorDB(N)
      factorized.connect()
      factor_list = factorized.get_factor_list()
      print(factor_list)
      return factor_list

    p, q = check_factordb(N)
    ```
* [Simple RSA Java Template](./tools/crypto/SimpleJavaRsaTemplate.java) -- Stub in your factored `p` and `q` and remaining values and then compile with `javac` and run with `java`.
* [RSA Java Multi-prime template](./tools/crypto/MultiPrimeJavaRsaTemplate.java) -- Stub in your factored primes and remaining values and then compile with `javac` and run with `java`.
* [Simple XOR server with predictable key brute forcer](./tools/crypto/pwntoolsRemoteXorBrute.py)
   * Usage: `python3.8 pwntoolsRemoteXorBrute.py --key_prefix <flag{> --endpoint some.host.here --port 6969`
     * Brute forces one char at a time against a remote endpoint that is a service that takes input and just returns the input XOR'ed against the static key. Easy to crack as just send a char until you get nothing back, append to key_so_far, and then proceed to next.
* [hashcat](https://hashcat.net/hashcat/) -- Awesome password cracking/recovery.
* [johntheripper](https://www.openwall.com/john/) -- Another awesome password cracking tool -- has additional tools to parse files and extract password hashes in particular format for cracking
   * E.g. `zip2john`, `keepass2john`, etc...
   * Once pulled out with `...2john`, can be fed to either `haschat` or `john`.
      * [hashcat attack mode type cheatsheet (1)](https://github.com/frizb/Hashcat-Cheatsheet)
      * [hashcat attack mode type cheatsheet (2)](https://hashcat.net/wiki/doku.php?id=example_hashes)
      * [john attack mode type cheatsheet](http://pentestmonkey.net/cheat-sheet/john-the-ripper-hash-formats)
  * [Running hashcat on Google Colab GPUs](https://github.com/someshkar/colabcat) -- 1. Free GPUs; 2. hashcat; 3. Profit?



---

# Forensics
### Online
* [DTMF decoder](http://dialabc.com/sound/detect/) -- takes audio file as input and gives numbers from DTMF.
