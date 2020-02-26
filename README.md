# cipherctl
A cipher tool that encodes and decodes in some of the most popular ciphers.

## Installation

You can install `cipherctl` by simply doing the following:

### Linux Distro's
```bash
$ release=$(curl -s https://api.github.com/repos/jbmcfarlin31/cipherctl/releases/latest | grep "browser_download_url.*zip" | cut -d '"' -f 4 | cut -d "/" -f 8)
$ wget https://github.com/jbmcfarlin31/cipherctl/releases/download/$release/cipherctl

# Or you can manually grab it
$ wget https://github.com/jbmcfarlin31/cipherctl/releases/download/1.1/cipherctl

$ chmod +x cipherctl

$ ./cipherctl
```

### MacOSx
```bash
$ release=$(curl -s https://api.github.com/repos/jbmcfarlin31/cipherctl/releases/latest | grep "browser_download_url.*zip" | cut -d '"' -f 4 | cut -d "/" -f 8)
$ wget https://github.com/jbmcfarlin31/cipherctl/releases/download/$release/cipherctl.app.zip

# Or manually grab it via
$ wget https://github.com/jbmcfarlin31/cipherctl/releases/download/1.1/cipherctl.app.zip

$ unzip cipherctl.app.zip
$ cd cipherctl.app/Contents/MacOS
$ chmod +x cipherctl
$ ./cipherctl
```

<!--### Windows - NOT TESTED YET
```
// using powershell
C:\Temp> wget https://github.com/jbmcfarlin31/cipherctl/releases/download/1.0.0/cipherctl
C:\Temp> python cipherctl
```
-->

## General Help Usage
```bash
cipherctl -h
usage: cipherctl.py [-h] [--debug]
                    {atbash,caesar,rot5,rot13,rot18,rot47,vigenere} ...

The cipherctl utility allows you to encode or decode in various ciphers

positional arguments:
  {atbash,caesar,rot5,rot13,rot18,rot47,vigenere}
                        ciphers
    atbash              Atbash cipher actions
    caesar              Caesar cipher actions
    rot5                ROT-5 cipher actions
    rot13               ROT-13 cipher actions
    rot18               ROT-18 cipher actions
    rot47               ROT-47 cipher actions
    vigenere            Vigenere cipher actions

optional arguments:
  -h, --help            show this help message and exit
  --debug               Enables verbose logging for cipherctl commands
```

Optional debugging can be enabled for verbose output:
```bash
./cipherctl --debug
```

## How to Use 
The cipherctl tool can be used to encode or decode in the following formats:
- Atbash
- ROT-5
- ROT-13
- ROT-18
- ROT-47 (beta)
- Caesar Cipher
- Vigenere Cipher

The usage for the utility is fairly simple, like so:
### Atbash
```bash
# For encrypting Atbash, you can do:
./cipherctl atbash -m "hello world"
SVOOL DLIOW

# For decrypting
cipherctl atbash -m "SVOOL DLIOW"
HELLO WORLD
```

### Caesar Cipher
```bash
# For encrypting Caesar Cipher
./cipherctl casesar -a encode -m "hello world" -s 7
OLSSV DVYSK

# For decrypting
./cipherctl caesar -a decode -m "OLSSV DVYSK" -s 7
HELLO WORLD
```

### ROT-5
```bash
# For encrypting, you can do:
./cipherctl rot5 -m "123 456"
678 901

# For decrypting
./cipherctl rot13 -m "678 901"
123 456
```

### ROT-13
```bash
# For encrypting, you can do:
./cipherctl rot13 -m "hello world"
URYYB JBEYQ

# For decrypting
./cipherctl rot13 -m "URYYB JBEYQ"
HELLO WORLD
```

### ROT-18
```bash
# For encrypting
./cipherctl rot18 -m "hello world123"
URYYB JBEYQ678

# For decrypting
./cipherctl rot18 -m "URYYB JBEYQ678"
HELLO WORLD123
```

### ROT-47 - BETA
```bash
# For encrypting, you can do:
./cipherctl rot47 -m "hello world123"
96==@ H@C=5`ab

# For decrypting
./cipherctl rot13 -m "96==@ H@C=5`a"
hello world123
```

### Vigenere Cipher
```bash
# For encrypting, you can do:
./cipherctl vigenere -a encode -m "hello world" -k "salts"
ZEWEG OOCEV

# For decrypting
./cipherctl vigenere -a decode -m "ZEWEG OOCEV" -k "salts"
HELLO WORLD
```

## Contributing
If you wish to contribute, please feel free to let me know. I'd be more than happy to let you.
