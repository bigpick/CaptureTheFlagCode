#!/usr/bin/env bash

passwords=($(cat 100passwords.txt | tr '\n' ' '))
export PATH=$HOME/Downloads/unarMac/:$PATH

#for i in {0..98}; do
#    echo "${passwords[${i}]}"
#done

while [[ "$(ls | awk '{print $NF}' | grep '^1\.')" == "" ]]; do
    tounzip=$(ls | awk '{print $NF}' | grep -v '100passwords\|ripper')

    if [[ $tounzip == 1.* ]]; then
        break
    fi

    if ! 7z -aoa -p"fake" e $tounzip; then
        for i in {0..98}; do
            7z -aoa -p"${passwords[${i}]}" e $tounzip && break
        done
    fi
    rm $tounzip
done
