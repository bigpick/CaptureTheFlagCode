# Various Capture The Flag competitions' worth of exploits
Also, a listing of some of the tools and resources I've found especially useful.

**[See this page for nice list of tool binaries](https://github.com/zardus/ctf-tools)**.

It's [Docker instructions...](https://github.com/zardus/ctf-tools#docker-version-17):

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

# Online
## Crypto
* [CyberChef](https://gchq.github.io/CyberChef/) -- "The Cyber Swiss Army Knife", analysing and decoding data
* [ROT5, ROT13, ROT18, and ROT47 cipher re/unshift](https://www.qqxiuzi.cn/bianma/ROT5-13-18-47.php)
* [QuipQuip](https://quipqiup.com/) -- Automated substitution/vigenere cipher solver w/out key.
* [Automated cipher identifier attempt](https://www.boxentriq.com/code-breaking/cipher-identifier).
* [Walkthrough of cryptanalysis methods](http://practicalcryptography.com/cryptanalysis/).

# Local Applications
## Crypto
* [CyberChef (docker container)](https://hub.docker.com/r/remnux/cyberchef/)

```
docker pull remnux/cyberchef
sudo docker run -d -p 8080:8080 remnux/cyberchef
# docker ps | grep cyberchef then docker stop/rm
```

# Forensics
## Online
* [DTMF decoder](http://dialabc.com/sound/detect/) -- takes audio file as input and gives numbers from DTMF.
