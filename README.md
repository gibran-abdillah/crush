<h2 align="center"> Crush (Crack Your Hash) </h2>

![Build Status](https://travis-ci.com/relarizky/crush.svg?branch=main)
![Code Size](https://img.shields.io/github/languages/code-size/relarizky/crush?color=brightgreen)
![Github Star](https://img.shields.io/github/stars/relarizky/crush?style=social)
![Github Fork](https://img.shields.io/github/forks/relarizky/crush?style=social)
![Github Watch](https://img.shields.io/github/watchers/relarizky/crush?style=social)

<i>Crush</i> is a simple python script for cracking hash

## Supported hash
|Hash|Status|
|----|------|
|MD5|✔|
|SHA1|✔|
|SHA256|✔|
|SHA512|✔|

## Instalation

```
$ git clone https://github.com/relarizky/crush.git
$ cd crush
$ python3 crush.py
```

## Usage

```
$ python3 crush.py
  _____                _
 / ____|              | |
| |     _ __ _   _ ___| |__
| |    | '__| | | / __| '_ \
| |____| |  | |_| \__ \ | | |
 \_____|_|   \__,_|___/_| |_|
            [Crack Your Hash]

usage: crush.py -s <hash> [-d | -b] [-w <file> | -l <length number>]

Simple Tool For Hash Cracking

optional arguments:
  -h, --help            show this help message and exit
  -s STRING, --string STRING
                        hash string you'd like to crack
  -b, --brute-attack    perform brute-force attack
  -d, --dict-attack     perform dictionary attack
  -l LENGTH, --length LENGTH
                        max length of string for brute-forcing (default=3)
  -w WORDLIST, --wordlist WORDLIST
                        wordlist file for dictionary attack

Happy Cracking:)
```
