# cipherctl
A cipher tool that encodes and decodes Atbash, ROT-13, Caesar Cipher and Vigenere Cipher.

## Installation

### Linux Distro's
You can install `cipherctl` by simply doing the following:
```bash
$ wget https://github.com/jbmcfarlin31/cipherctl/releases/download/1.0.0/cipherctl
$ chmod +x cipherctl

$ ./cipherctl
```

### MacOSx
```bash
$ wget https://github.com/jbmcfarlin31/cipherctl/releases/download/1.0.0/cipherctl.app.zip
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
usage: cipherctl.py [-h] [--debug] {atbash,caesar,rot13,vigenere} ...

The cipherctl utility allows you to encode or decode in various ciphers

positional arguments:
  {atbash,caesar,rot13,vigenere}
                        ciphers
    atbash              Atbash cipher actions
    caesar              Caesar cipher actions
    rot13               ROT-13 cipher actions
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
- ROT-13
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

### ROT-13
```bash
# For encrypting, you can do:
./cipherctl rot13 -m "hello world"
URYYB JBEYQ

# For decrypting
./cipherctl rot13 -m "URYYB JBEYQ"
HELLO WORLD
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
