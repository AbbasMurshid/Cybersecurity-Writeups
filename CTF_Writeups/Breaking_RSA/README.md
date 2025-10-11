# My First Write-Ups 

Challenge Description
Exploit a poorly implemented RSA cryptosystem to recover the private key by factorizing the modulus n into its prime factors p and q. The vulnerability stems from the two prime numbers being too close to each other, making them susceptible to Fermat's Factorization attack.

Tools Used

nmap - Network enumeration

gobuster - Directory brute-forcing

ssh-keygen - SSH key analysis

Python 3 with libraries:

pycryptodome - Cryptographic operations

gmpy2 - Large number handling

