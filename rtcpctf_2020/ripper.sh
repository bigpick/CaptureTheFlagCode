#!/usr/bin/env bash

# gunzip -c foo.tar.gz | tar xopf -
# unzip -a 1811.zip
# tar xopf 1814.tar
# $HOME/Downloads/john-1.8.0.9-jumbo-macosx_sse4/run/zip2john 1810.gz > ziphash
# $HOME/Downloads/john-1.8.0.9-jumbo-macosx_sse4/run/john ziphash --wordlist $HOME/Downloads/rtcp_ctf/zipadeedoda/100passwords.txt

# Start: 1819.gz

tounzip="1819.gz"
passwords=($(cat 100passwords.txt | tr '\n' ' '))
# passwords[2] .. passwords[99]
export PATH=$HOME/Downloads/unarMac/:$PATH

while [[ "$(ls | awk '{print $NF}' | grep '^1\.')" == "" ]]; do
    tounzip=$(ls | awk '{print $NF}' | grep -v '100passwords\|ripper')

    if [[ $tounzip == 1.* ]]; then
        break
    fi

    if ! unar -f -p fake $tounzip; then
        for i in {2..99}; do
            unar -f -p ${passwords[${i}]} $tounzip && echo "found it! ${passwords[${i}]}" && break
        done
    fi
    rm $tounzip

    # if [[ $tounzip == *.gz ]]; then
    #     echo "Found .gz"
    #     gunzip -c $tounzip | tar xopf -
    #     rm $tounzip
    # elif [[ $tounzip == *.tar ]] && [[ $tounzip != *.tar.gz ]]; then
    #     echo "Found .tar"
    #     tar xopf $tounzip
    #     rm $tounzip
    # else
    #     # .zip
    #     if ! unzip -P fake -a $tounzip; then
    #         for i in {2..99}; do
    #             unzip -P ${passwords[${i}]} -a $tounzip && echo "found it! ${passwords[${i}]}" && break
    #         done
    #     fi
    #     rm $tounzip
    # fi
done
