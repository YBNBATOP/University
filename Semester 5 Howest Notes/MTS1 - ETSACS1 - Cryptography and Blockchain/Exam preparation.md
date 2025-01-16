## Intro
Goals of crypto:
- Confidentiality
- Integrity
- non-repudiation
- authentication
### Symmetric encryption
It means the same key is used for encrypting and decrypting by both users
#### Block cipher
It takes a block of plaintext, and produces the same amount of ciphertext.
It does the cipher with a key.

In this case you get multiple blocks -> into multiple ciphers.
So P1 (plain) will become C1 (cipher)
#### Stream cipher
It takes data bit by bit or byte by byte and XORs it with a random bit stream. This bit stream generation should be a "known" algorithm so it can be replicated.
### Asymmetric encryption
It means everybody has a private key, but a public key of the user is used to encrypt somethingz that only the user will be able to decrypt.
Public - to encrypt a message for the user.
Private - to decrypt the message for the user.
> The private key is only known by Bob. So, Bob is the only party capable of decrypting ciphertexts that were encrypted with Bob's public key.

Both keys are linked and are a part of a key pair generation algorithm.
### Encryption
Encryption - process of creating ciphertext from plaintext
Decryption - process of re creating the original plaintext from ciphertext
### Digital signature
It is the same principal of asymmetric encryption. You have a document, with a private key.
It is typically created through the use of a hash function and a private signing function (algorithms that create encypyted characters containing 
Typically, not the complete document's content is signed but the hash of the document content
### Passkey
The passkey is actually a key pair of a matching public and private key. The server has obtained the public key part during the initial account setup and the private key remains on the user's device. When logging in the account, the server sends a random challenge that is then digitally signed by the user using the private key part of the passkey.
This all refers to the authenticator keys that I usually use. It can be used instead of passwords overall.
### WhatsApp Encryption
Elliptic Curve Diffie Hellman algorithm helps two communicating entities to agree up on a shared secret without actually sending the actual keys to each other.
These guys use a combination of symmetric and asymmetric encryption, basically to achieve confidentiality and integrity + authentication and non-repudiation
### Bitcoin
It uses ECDSA (eliptical curve cryptography) to sign transactions.
The Bitcoin protocol allows pieces of bitcoin to be sent to a public key, such that only a valid signature from the corresponding private key can unlock it. This signature is published to the blockchain so that any member of the Bitcoin network can verify all the things and "decide" if it is for his account.
### Belgian e-id
The card holds three diﬀerent 1024-bit RSA private signing keys: one to authenticate the citizen, one for non-repudiation signatures, and one to identify the card itself towards the Belgian government.
## A Module
### Main parts:
- Number systems and XOR
- Modulo calculation
- Galois finite fields
- Euclidean greatest common divisor
- Extended Euclidean algorithm
- Polynomial arithmetic
- Polynomial multiplication
### Basic arithmetic
XOR calculation
```python
>>> import cryptocourse
>>> from operator import xor
>>> a = 73
>>> b = 87
>>> bin(a)
'0b1001001'
>>> bin(b)
'0b1010111'
>>> c = a^b
>>> bin(c)
'0b11110'
>>> c
30
>>> xor(1,2)
3
>>> c = xor(a,b)
>>> bin(a), bin(b), bin(c)
('0b100010', '0b111000', '0b11010')
```

Different number representations
```python
>>> a = 34
>>> b = 56
>>> c = a+b
>>> c
90
>>> bin(a), bin(b), bin(c)
('0b100010', '0b111000', '0b1011010')
>>> hex(a), hex(b), hex(c)
('0x22', '0x38', '0x5a')
>>> a, b, c
(34, 56, 90)
>>> c = 0x22 + 0b111000
>>> c
90
```

### Modulo arithmetic
#### Modulo
The goal of module - to have the result in specific boundaries.
If we have 4+3 in modulo 5, then it is not 7 but 2.
"Working in modulo 5 means that you take the initial result (7) and you subtract 5 as many times as required in order to obtain a result 0, 1, 2, 3 or 4.  If you work in modulo 5, then 4 * 3 is no longer equal to 12, but it is equal to 2."

Modulo calculation
```python
# Plain modulo calculation
>>> (23+8)%29
2

# This is meant to be simple to the power
>>> pow(2,100)
1267650600228229401496703205376
# This is meant to be the to power in modulo x
>>> pow(2,100,29)
25
>>> pow(2,100)%29
25
```

Greatest common divisors
```python
>>> from cryptocourse import euclidean
>>> euclidean.gcd(35,85)
5
```

Prime calculation
```python
>>> from cryptocourse import primes
>>> p1 = primes.findAPrime(100,200)
>>> p1
173
```

Multiplicative inverse
```python
>>> euclidean.mulinv(1759,550)
439
>>> euclidean.mulinv(550,1759)
355
```

## B Module
- Symmetric encryption
- Confusion/diffusion
- Substitution/permutation
- Feistel cipher
- DES
- AES design:
	- Overall
	- S-box substitution
	- Shift rows
	- Mix columns
	- Add round key
	- S-box construction
	- Key schedule algorithm
	- AES parameters
- Meet in the middle attack
- Modes of operation
- Stream ciphers

# Exercises

## Sample quiz

>Given two prime numbers P = 16049261, Q =11253433. Perform the RSA textbook algorithm. We look for the ciphertext corresponding to the plaintext 123456. We also look for the plaintext corresponding to the ciphertext 654321. As the encryption key e, we choose 65537.
>All numbers are (as always in the course and the exercises with RSA) in decimal.

```python
>>> from cryptocourse import euclidean
>>> p = 16049261
>>> q = 11253433
>>> n = p * q
>>> totient = (p-1)*(q-1)
>>> e = 65537
>>> d = euclidean.mulinv(e,totient)
>>> plain = 123456
>>> cipher= 654321
>>> enc = pow(plain,e,n)
>>> dec = pow(cipher,d,n)
>>> enc, dec
(143940847401441, 42149430044349)
>>>
```

>We use a stream cipher with a pseudo random number generator based on the standard Python function random. We generate 1000 random bits (see function call). Do not use any number other than 1000. The key in this example (and which must be known by both sender and receiver) is 123456. 
>Import random  
>key = 123456  
>random.seed(key)  
>stream = random.getrandbits(1000)
>Asked: the ciphertext belonging to the stream cipher based on this stream, with plain (in hex) 100200300400500600700800900A00B00C00D00E00F00000

```python
>>> import random
>>> from operator import xor
>>> key = 123456
>>> random.seed(key)
>>> stream = random.getrandbits(1000)
>>> hex(stream)
'0xc8a5921cf1decf64ab6099e45d210358d0e9dff5cf877b36f60636ad23ebd992662fa49213e6b293247cc7661da39301133aa1651beeba32751dcc13320745c34b44bdf3160d0f1ece13b980dddf09ffbea9f43d86e9732cfa0092231af456188c2cb647dacce31fd1078872414a27a1e3cb477398d804530bce3d9460'
>>> plain = 0x100200300400500600700800900A00B00C00D00E00F00000
>>> #This value should be the same lengths 
>>> stream= 0xc8a5921cf1decf64ab6099e45d210358d0e9dff5cf877b36
>>> cipher = xor(plain,stream)
>>> hex(cipher)
'0xd8a7922cf5de9f62ab1091e4cd2b03e8dce90ffbcf777b36'
>>>
```

>THIS QUESTION IS ONLY FOR THE 5 STUDY POINT VERSION (CRYPTOGRAPHY AND BLOCKCHAIN)
>Suppose p = 19. We are dealing with a Shamir secret sharing scheme with threshold = 4 and 6 parties P1, P2, P3, P4, P5, P6. P1 corresponds with x=1, P2 corresponds with x=2, … The four parties P1, P2, P5, P6 put their shares together (respective values 8, 18, 11, 6). Calculate the secret K. This is an integer, called secret_K.
>We will now use the basic_bc module to make a transaction between Joe and Donald with this hash value and place this single transaction on the first block b0 (index = 0). Afterwards we are going to mine this block, and I ask for the nonce. The previous hash for the first block consists of 64 hexadecimal zeros, the miner of this first block is called "SampleExam" , and the timestamp of the block is 100010.
>joe = basic_bc.MyIdentity("Joe",1)
>donald = basic_bc.MyIdentity("Donald",2)
>t = basic_bc.MyTransaction(joe, donald, secret_K, timestamp=100000)
>For all parameters not listed, use the defaults as defined in the Python modules "shamir.py" and "basic_bc.py".

```python
>>> from cryptocourse import shamir, basic_bc
>>> p = 19
>>> shares = [[1,8],[2,18],[5,11],[6,6]]
>>> joe = basic_bc.MyIdentity("Joe",1)
>>> donald = basic_bc.MyIdentity("Donald",2)
>>> secret_K = shamir.reconstructSecret(shares,p)
>>> t = basic_bc.MyTransaction(joe, donald, secret_K, timestamp=100000)
>>> secret_K
6
>>> t.sign()
>>> b0 = basic_bc.Block(0,[t],'0'*64,"SampleExam",timestamp=100010)
>>> b0.mine()
>>> b0.nonce
1260785
>>>
```

Given this stream (in hex):
1cf1decf64ab6099e45d210358d0e9dff5cf877b36f60636ad23ebd992662fa49213e6b293247cc7661da39301133aa1651beeba32751dcc13320745c34b44bdf3160d0f1ece13b980dddf09ffbea9f43d86e9732cfa0092231af456188c2cb647dacce31fd1078872414a27a1e3cb477398d804530bce3d9460

You can easily copy the value of this stream into your Python code (remember: hex). 

This is the plaintext (in hex): 200300400500600700800900100A00B00C00D00E00F00000

Give the encryption (in hex) of this plaintext with the stream cipher defined according to this stream (with the XOR function).

```python
>>> plain = 0x200300400500600700800900100A00B00C00D00E00F00000
>>> stream= 0x1cf1decf64ab6099e45d210358d0e9dff5cf877b36f60636
>>> cipher = plain^stream
>>> hex(cipher)
'0x3cf2de8f61ab009ee4dd280348dae96ff9cf577536060636'
# in cipher we always have the same lengths
```

We are using a simplified (1 round) block cipher algorithm. The master key is (in hex):  
1234567890ABCDEFFEDCBA0987654321FEDCBA09876543211234567890ABCDEF.  
The block cipher algorithm uses blocks of 64 bits. The algorithm  
consists of (in this order):  
- S-box substitution according to S-box in attachment (per byte)  
- XOR operation with subkey 1  
- permute.permute function with sequence parameter [2,3,1,4,6,7,0,5]  
- XOR operation with subkey 2  
We need a key schedule algorithm to calculate the subkeys from the master key. The first subkeys are just the portions of the master key (in this order): subkey 1: first (leftmost) portion, subkey 2: second portion; etc.  

What is the ciphertext C1,C2 (in hex) of plaintext 11223344556677881021324354657687 using ECB mode of operation?

Some values in the S-box are in bold but this is not relevant. These are byte for byte substitutions. Do not forget leading zero's!

```python
>>> master = 0x1234567890ABCDEFFEDCBA0987654321FEDCBA09876543211234567890ABCDEF
>>> subkey1 = 0x1234567890ABCDEF # select 64 bits or 16 characters
>>> subkey2 = 0xFEDCBA0987654321 # select 64 bits or 16 characters
>>> plain   = 0x11223344556677881021324354657687
>>> P1      = 0x1122334455667788 # 16 characters because 64 bits / 4
>>> P2      = 0x1021324354657687
>>> S_BOX1  = 0x2d02bac141652027
>>> from operator import xor
>>> XOR1    = xor(S_BOX1, subkey1)
>>> from cryptocourse import permute
>>> PERM1 = permute.permute(XOR1, [2,3,1,4,6,7,0,5])
>>> C1    = xor(PERM1, subkey2)
>>> hex(C1)
'0x300d72b0b15aafcc'
>>> S_BOX2  = 0xc4340e0f3f068b43
>>> XOR2    = xor(S_BOX2,subkey1)
>>> PERM2   = permute.permute(XOR2, [2,3,1,4,6,7,0,5])
>>> C2   = xor(PERM2, subkey2)
>>> hex(C2)
'0x5373167e87b31b67'
>>>
```

# Theory questions
1) You have access to a small cluster of GPU cards evaluating MD5 10^9 = 2^30 times per second. MD5 produces a message digest of 128 bits length. How long is it expected to take to find a MD5 collusion using brute force? The notation 2^n stands for “2 to the power n”. The conversion from seconds to years is just to help you and does not contain any mistakes. Just consider the 2^n answers.
```
we have 2^128 possibilities, and normally it takes like 2^64 (so half the possibilities) to crack the hash or something. That is an assumption.
So we have 2^64 / 2^30 = 2^(64-30) and we get 2^34 seconds.
```

2) Which component of the AES algorithm is shown here?
![[Pasted image 20250105215310.png]]`
```
S-Box (because the values are just inverses, and not shifting, or nothing like a new key is not added
```

3) Calculate the Galois multiplication in GF(2^8) of 96x8B with prime polynomial (x8 + x4 + x3 + x2 + 1)
```
You transform everything into binary first of all
10010110

10001011

Then this 2 transform into polynomials

The value is going to  be too big, so I haveto do multiplication table, to the maximum xp power. For this I choose 1 of the 2 values.

Once you have an x^8 there, you need to add the polynom. 

Each time we just add one x to each element, like multiplying.

After the last value is done, we do the substitution for the second polynom that we did not use, with the values from our table.

In the end we get a value of polynom, which we transform to binary, and then we get the values we need.

The binary transforms to Hex.
The value is going to be
1011 1111 = 11 F = BF
```

4) If an "oracle" exists that leaks 1 bit of an RSA decryption, you can eventually determine the full decryption. This attack is called "least significant bit attack", but is also known by another name. Which one?
```
This one is known is a Parity side channel attack.
```

5) What is the problem that Galois fields solve in cryptography ? Why do we not just stick to the multiplication and addition operations that we all know? Why not stick to modulo calculation? (Indicate two answers)
```
Galois fields are finite, so it can be calculated.

Modulo arithmetic only works for prime numbers and prime numbers are not practical for fixed bit length domains.
```

6) You can use these algorithms ( indicate three answers) to find out if a number is a prime number: Whether the algorithm is efficient or not, is not issue to be taken into account.
```
AKS
Brute force factorisation
Miller-Rabin

Blum-blum is for random number generation, RC4 is encryption, Rivest-Shamir is for secret sharing and etc, linear-congruential generator also generates just numbers (DBRG = PRNG)
```

7) I want an asymmetric crypto that allows you to use a specific key (not a general decryption key that allows you to decrypt anything) to make the encrypted sum of two encrypted numbers.
```
Keyed homomorphic crypto
```

8) What are the two main categories of symmetric encryption algorithms used today?
```
Block ciphers and stream ciphers (because we do not have keys, and it is the only things that we have).
```

9) What is the value of the totient of 12?
```
List down the numbers from 1 to 11, without 12
1 2 3 4 5 6 7 8 9 10 11
Each of this number, or totient, needs to have itself and 1 as divisors.
For example 6 has 1,2,3,6
While 11 has 1,11 so it applies.
1, 5, 7, 11
```

10) The email configuration mechanism that establishes that only certain IP addresses may send mails on behalf of specified domains is called:
```
SPF - Sender Policy Framework (is a DNS based email aithentication method that specifies which mail servers are authorized to send emails on behalf of a domain)

DKIM - Domain Keys Identified Mail (verifies that the email has not been altered in transit)
DMARC - Domain-based Message Authentication, Reporting, and Conformance (ensures proper use of SPF and DKIM)
DNS-SEC - Domain Name System Security Extensions (it is meant for integrity and authenticity of DNS responses)
DANE - DNS-based Authentication of Named Entities (strengthens the trust model for TLS/SSL certificates by linking them to DNS-SEC)
```

11) Calculate the Galois multiplication 2x5 in GF(2^3) with prime polynomial (x^3 + x + 1). Result in decimal.
```
To solve this, we do pretty much the same things as in the other question. Just need to understand that now the limit is 2^3 so X can be like max or better less than 3

Transform it to binary.

Multiply them, and then add the polynomial that we have.

Get rid of the excess, and we get 1.
```

12) Given this elliptic curve. Determine the values of the points x, y, and z.
```
This is a bit tricky, as we get the value G.
That is 1G.
The moment we get through other points, being it only 2 or 3, the values should be equal to 0.
A + B + C = 0
So for example I have value G, then I need to make a line to another point, and overall I do not have other points of intesection. It will be G + x + x = 0. So I have 1 value known, so I can use it 2 times. So I get G + G + x = 0. Hence, I know that I need to do G + G + (-2G) = 0. So the other point will be -2G 

If the line goes straight down, then it just changes the sign, but not the value.
```
![[Pasted image 20250105232200.png]]

12) Are TRNG and DRBG synonyms?
```
Nope, PRNG are synonyms with DRBG. The TRNG is synonym to NDRBG
```

# More exercises
Given two prime numbers P = 37752007, Q = 40770133. Run the RSA algorithm. We seek the ciphertext corresponding to the plaintext 123456. We also look for the plaintext corresponding to the ciphertext 654321. As the encryptionkey e we choose 65537.
```python
>>> p = 37752007
>>> q = 40770133
>>> e = 65537
>>> plain = 123456
>>> cipher = 654321
>>> n = p * q
>>> from cryptocourse import euclidean
>>> totient = (p-1)*(q-1)
>>> d = euclidean.mulinv(e,totient)
>>> d
916301370459329
>>> enc = pow(plain,e,n)
>>> dec = pow(cipher,d,n)
>>> enc, dec
(1530737875555856, 234522041167010)
>>>
```

Given this stream (in hex):

55abc1105990a326f9828613112d41abc7cd80f8bb2410c67bab93ef7b9ae3ff0d5e11789e5fb23f210d836321024bc199dabb2246ce9c09c90073e3d17d1cb504ebe6feea498369713143fe29561d347fd9f65815ded26c80d61da0c854749cc7cfa7d29d0072f27bf4201c92c30fa9b79b89f152d67ddd7be0eec2d

This is the plaintext (in hex): 100200300400500600700800900A00B00C00D00E00F00000

You can copy the value of this stream into your Python code like this (remember: hex). Return the encryption (in hex) of this plaintext with the stream cipher defined according to this stream (with the XOR function). For the stream cipher, take the same length as the plaintext.

```python
>>> from operator import xor
>>> plain = 0x100200300400500600700800900A00B00C00D00E00F00000
>>> stream= 0x55abc1105990a326f9828613112d41abc7cd80f8bb2410c6
>>> cipher= xor(plain,stream)
>>> cipher
1708134318441455519036260981760054765789455217027880063174
>>> hex(cipher)
'0x45a9c1205d90f320f9f28e138127411bcbcd50f6bbd410c6'
>>>
```

(???) Given this S-box along with its inverse S-box. The S-box transformation defines a (simple, 1 round) block cipher with block size of 128 bits. This is the plaintext (in hex): 1000200030004000500060007000800010002000300040005000600070008001. Note that the two blocks of plaintext are not exactly the same!

The encryption operation is done in CBC mode and consists of the S-box substitution followed by a permutation and then followed by an XOR with the key = 88f38c0c8fd8712b8bc076f3787b9d17.

You can easily implement the permutation to be used with permute.py as follows:

output = permute.permute(input, [15,0,14,1,13,2,12,3,11,4,10,5,9,6,8,7]).  
Determine the encryption of the two blocks of plaintext, the first time in ECB which results in C1 and C2, the second time in CBC which results in C1 and C3. As a result, we want the three ciphertext blocks C1, C2, C3 (in hex). The IV for CBC is 0.
```python
>>> from operator import xor
>>> from cryptocourse import permute
>>> plain = 1000200030004000500060007000800010002000300040005000600070008001
>>> p1    = 0x10002000300040005000600070008000
>>>
>>> p2    = 0x10002000300040005000600070008001
>>> key   = 0x88f38c0c8fd8712b8bc076f3787b9d17
>>> sbox1 = 0x7c525452085272526c529052d0523a52
>>> sbox1 = permute.permute(sbox1, [15,0,14,1,13,2,12,3,11,4,10,5,9,6,8,7])
>>> res1  = xor(sbox1,key)
>>> hex(res1)
'0xf4a7847ee348a111d99224a12a29cf45'
>>> input2 = xor(p2,res1)
>>> hex(input2)
'0xe4a7a47ed348e111899244a15a294f44'
>>> res2 = 0x7c525452085272526c529052d0523a09
>>> res2 = permute.permute(res2,  [15,0,14,1,13,2,12,3,11,4,10,5,9,6,8,7])
>>> res2 = xor(res2, key)
>>> hex(res1), hex(res2)
('0xf4a7847ee348a111d99224a12a29cf45', '0xf4a7847ee348a111829224a12a29cf45')
>>>
```

Two parties use discrete-logarithm based Diffie-Hellman with the default group parameter (as defined in basic_dh.py) 6144 (group) and 02 (sequence). A sends the message 0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF to B by taking the common Diffie Hellman shared secret and XOR'ing it with the plaintext. Determine the ciphertext (in hex)? The private key of party B = 5 and the private key of party A = 7.

(Basic idea here is to create the asymmetric encryption method of Diffie Hellman, and have something encrypted with one of the keys)
```python
>>> from cryptocourse import basic_dh
>>> a = basic_dh.DiffieHellman(6144,2)
>>> b = basic_dh.DiffieHellman(6144,2)
>>> a.set_private_key(7)
>>> b.set_private_key(5)
>>> publica = a.gen_public_key()
>>> publicb = b.gen_public_key()
>>> secretba = b.gen_shared_key(publica)
>>> secretab = a.gen_shared_key(publicb)
>>> secretab == secretba
True
>>> secretab
b'\xbb^S\xeeZ\x05\xe6\x8e{\x9bb\xfcK\x1c\xad1qk<7+\x03V\x8ah/\xc9\x82\xd0o\xb6-'
>>> secretab.hex()
'bb5e53ee5a05e68e7b9b62fc4b1cad31716b3c372b03568a682fc982d06fb62d'
>>> key = 0xbb5e53ee5a05e68e7b9b62fc4b1cad31716b3c372b03568a682fc982d06fb62d # has to be the same length again
>>> plain=0x0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF
>>> from operator import xor
>>> cipher = xor(plain,key)
>>> hex(cipher)
'0xba7d1689d3ae2b617ab8279bc2b760de70487950a2a89b65690c8ce559c47bc2'
```

Two parties use elliptical Diffie-Hellman with the default group parameter (as defined in basic_ec.py) "secp256k1". A computes the common Diffie Hellman shared secret. The private key of party A = 7 and the private key of party B = 5. What is the shared secret (in coordinate form)?

(same principle, but now we use the eliptic curve to solve this)
```python
>>> from cryptocourse import basic_ec
>>> g = basic_ec.StandardBasePoints["secp256k1"]
>>> ec = basic_ec.StandardECS["secp256k1"]
>>> a = basic_ec.DiffieHellman(ec,g)
>>> b = basic_ec.DiffieHellman(ec,g)
>>> a.set_private_key(5)
>>> b.set_private_key(7)
>>> publica = a.gen_public_key()
>>> publicb = b.gen_public_key()
>>> secretab = a.gen_shared_key(publicb)
>>> secretba = b.gen_shared_key(publica)
>>> secretab == secretba
True
>>> secretab
Coord(x=43584328072464330665967763306297595761508151294385275883849271528835646125177, y=1171731419844835688478928898148416329180259014376715189840427072871218252873)
>>>
```

We manage to steal three shares from a (3,7) Shamir secret sharing scheme in GF(156941). The shares are [51329, 32289], [34906, 49516], [39948, 21571]. What is the secret?
```python
>>> from cryptocourse import shamir
>>> shares = [[51329, 32289], [34906, 49516], [39948, 21571]]
>>> shamir.reconstructSecret(shares,156941)
13579
```

Use basic_bc.py to create two identities ("Donald Trump", 14061946) and ("Joe Biden", 20111942). Now create a transaction where Donald pays 100 to Joe at the time with timestamp = 1000000 (1 million). Now create the block with index 1000 that consists of this one transaction , again with timestamp = 1000000, previous hash = '0'x128, miner = "Alexander". Use the hash function sha512 throughout. Give the value of the nonce when mining with default difficulty level.

(You create the identities, you create a transaction, you sign it, you create a mining "request", you mine it, and you get the nonce of it)
```python
>>> from cryptocourse import basic_bc
>>> donald = basic_bc.MyIdentity("Donald Trump", 14061946)
>>> joe    = basic_bc.MyIdentity("Joe Biden",20111942)
>>> t = basic_bc.MyTransaction(donald, joe, 100, timestamp=1000000, hash_function='sha512')
>>> t.sign()
>>> b = basic_bc.Block(1000,[t],'0'*128,"Alexander",timestamp=1000000,hash_function='sha512')
>>> b.mine()
>>> b.nonce
3096748
>>>
```

`I am working with a (3,3) Shamir sharing scheme; shares1 = [[1,2],[2,4],[3,10]] and shares2 = [[1,3],[2,9],[3,25]]. Prime number is 281. I also have a beaver triple [[[1, 188], [1, 224], [1, 29]], [[2, 219], [2, 240], [2, 48]], [[3, 214], [3, 140], [3, 230]]. I am looking for the multiplication of the secret behind shares1 and shares2 using the SPDZ protocol as implemented in basic_mpc (and using the specified beaver triple). What is the y-value of the share of multiplication belonging to x=3 ? What is the y-value of the polynomial belonging to the shares of multiplication for x = 0 ?`

```python
>>> from cryptocourse import basic_mpc
>>> from cryptocourse import shamir
>>> shares1 = [[1,2],[2,4],[3,10]]
>>> shares2 = [[1,3],[2,9],[3,25]]
>>> beaver  = [[[1, 188], [1, 224], [1, 29]], [[2, 219], [2, 240], [2, 48]], [[3, 214], [3, 140], [3, 230]]]
>>> sha, shb, shc = basic_mpc.splitBeaver(beaver)
>>> alphashares = shamir.subtractShares(shares1, sha,281)
>>> betashares  = shamir.subtractShares(shares2, shb,281)
>>> alpha = shamir.reconstructSecret(alphashares,281)
>>> beta  = shamir.reconstructSecret(betashares,281)
>>> resultShares = shamir.linearCombinationOfShares([shc,shb,sha],[1,alpha,beta],alpha*beta,281)
>>> resultShares
[[1, 101], [2, 109], [3, 52]]
>>> shamir.reconstructSecret(resultShares,281)
28
>>> shamir.reconstructSecret(shares1,281)
4
>>> shamir.reconstructSecret(shares2,281)
7
# the x=3 is 52, the x=0 is 28
```

# Images
The one that has MBR = **CMAC**

The one that has IV = **MBR**
 ![[Pasted image 20250106075542.png]]  

The one that has Counter = **CTR**
![[Pasted image 20250106075748.png]]

The one that does not have anything connected = **ECB**
![[Pasted image 20250106080344.png]]

The one that has Nonce = **OFB**
![[Pasted image 20250106080405.png]]

The one that has CMAC block in it = **CCM**
![[Pasted image 20250106080714.png]]

The one that has EDE = **X9.17**
![[Pasted image 20250106080745.png]]

**SHA-2**
![[Pasted image 20250106080807.png]]

**AES Shift Rows**
![[Pasted image 20250106082200.png]]

**AES Mix Columns**
![[Pasted image 20250106082228.png]]

**AES Add RoundKey**

# Exam
Given this pseudo random generator where the key and IV must be given:
import random
key = .....
IV = .....
random.seed(key+IV)
stream=random.getrandbits(1024)
We have a plaintext (in hex) 1234567890ABCDEF
Give the encryption (in hex) of this plaintext with the stream cipher defined according to this stream (using the XOR function). The key is 1A2B3C and the IV is 4D5E6F (both hexadecimal). The IV should normally also be passed to the receiver, but we omit this here for simplicity. Don't let the use of an IV in a stream cipher confuse you. Modern stream ciphers usually have an IV.

```python
>>> import random
>>> key = 0x1A2B3C
>>> IV = 0x4D5E6F
>>> plain = 0x1234567890ABCDEF
>>> from operator import xor
>>> random.seed(key+IV)
>>> stream=random.getrandbits(1024)
>>> stream
159901903333058570309758734397282788679004605777894135869522280792440631557043976297697387987602328940312705728186327622139794460928496969264064363927196548478890581803000011135053504525401289277390401435609262541969416175202167303616002330299423378359970099215074729333888165282281358853999519673660956773779
>>> hex(stream)
'0xe3b536e419a38295939731b3aab9d81c032c6dfd342dae3767570bd623c94bcf5128b112db7cc6fd4f89e3a1a53f2841c02766384e883434883ac3d25b08153063804bb9b8fc4bb7637f5900c7932ab438558d80e86cff199d06fd500421a68c6944568faab3fa1ea6d7492a3dfc9a4c065851245df91ce622091c7848d08d93'
>>> plain
1311768467294899695
>>> plain = 0x1234567890ABCDEF
>>> part  = 0xe3b536e419a38295
>>> enc = xor(plain,part)
>>> hex(enc)
'0xf181609c89084f7a'
>>>
```

Given two prime numbers P = 203657764564847, Q = 407315528995873. Execute the RSA textbook algorithm. We look for the ciphertext corresponding to the plaintext 123456. We also look for the plaintext corresponding to the ciphertext 654321. As the encryption key e, we choose 65537.
All numbers are (as always in the course and the exercises with RSA) in decimal.
```python
>>> from cryptocourse import euclidean
>>> p = 203657764564847
>>> q = 407315528995873
>>> plain = 123456
>>> cipher = 654321
>>> e = 65537
>>> n = p*q
>>> totient = (p-1)*(q-1)
>>> d = euclidean.mulinv(e,totient)
>>> enc = pow(plain,e,n)
>>> dec = pow(cipher,d,n)
>>> enc, dec
(55660375768347180642496884022, 18381316308388832753376270373)
>>>
```

Given this S-box along with its inverse S-box. The S-box transformation defines a (simple) block cipher with block size of 128 bits. This is the plaintext (in hex): 1000200030004000500060007000800010002000300040005000600070008001. As you notice (or count), these are two blocks of plaintext. Note that the values of the two blocks of plaintext are not exactly the same!

The encryption operation consists of the S-box substitution followed by an XOR with the key = 88f38c0c8fd8712b8bc076f3787b9d17

Determine the encryption of the two blocks of plaintext, in CTR mode. CTR1 = 00000000000000000000000000000001 and CTR2 = 00000000000000000000000000000002. Determine the two blocks of the encryption result (in hex).

(you have the ctr1, and 2, and the encryption is for them!
you go sbox for ctr1, then xor it with the key, and then do xor of p1 with the res of ctr1)
```python
>>> plain = 0x1000200030004000500060007000800010002000300040005000600070008001
>>> p1    = 0x10002000300040005000600070008000
>>> p2    = 0x10002000300040005000600070008001
>>> ctr1  = 0x00000000000000000000000000000001
>>> ctr2  = 0x00000000000000000000000000000002
>>> key_original = 0x88f38c0c8fd8712b8bc076f3787b9d17
>>> s_box1 = 0x7c525452085272526c529052d0523a52
>>> ctr1   = 0x00000000000000000000000000000001
>>> s_box1_ctr_1 = 0x52525252525252525252525252525209
>>> from operator import xor
>>> res_ctr_1 = xor(s_box1_ctr_1,key_original)
>>> cipher_1  = xor(p1,res_ctr_1)
>>> hex(cipher_1)
'0xcaa1fe5eed8a6379899244a15a294f1e'
>>> s_box1_ctr_2 = 0x5252525252525252525252525252526a
>>> res_ctr_2 = xor(s_box1_ctr_2,key_original)
>>> cipher_2 = xor(p2, res_ctr_2)
>>> hex(cipher_2)
'0xcaa1fe5eed8a6379899244a15a294f7c'
>>>
```

Assume we have a value n =
9922330246934353762754694244526642319833116592604770184866522695626311158070013022344495758217087406421147657566836305094724560721420497592104115791816651854076522508340077679127596209483114182218021828420314512938010419259881651694800420391606466269432947228027931160122974350935271108365745643056300340310303565128341440144607548220921034157
In a (vanilla textbook) RSA encryption, Bob has public key = 3 en Charlie has public key = 5.  The value of n is equal for both. Alice sends the same secret message, encrypted to Bob (cipher1) and to Charlie (cipher2).

>>> cipher1

9807381332535553141274492160524265053707348722913524137202242760648229446440119177113523963419365776917928923085563120206340569542222464798166834670231670932069906760354865343035674961413293896454386330478818458443290732834412394425487558215921722051619372323342920328385745895696881193155311279178538154761915243418296223849193599190572008580

>>> cipher2

1626476087708273512599080099772869895656490929067147172594508082309303030450397608312302379547121204525042752300374571003621811230166609367916272760993519211685938707185705702124002076994535485936098907299835210079315550535122216106768922644515518833580610975298366664372375787749204420980489176375344335896745887597816375241345084087105916143

What are the four last decimal digits of the plaintext of the secret message?
```
NO FUCKING CLUE

CORRECT ANSWER: 9479
```

Suppose p = 19. We are dealing with a Shamir secret sharing scheme with threshold = 4 and 6 parties P1, P2, P3, P4, P5, P6. But we always need P1 and P2 to be part of this scheme. We have solved this by using Shamir secret sharing twice. First, we have a (3,3) scheme with P1, P2 and all the others combined. This third share belonging to “all the others combined” is split again among P3, P4, P5, P6 in a (2,4) scheme.

In the first scheme, the 3 parties P1, P2, and “all the others combined” correspond to x=1, x=2 and x=3,. In the second scheme, the 4 parties **P3**, P4, P5, P6 correspond to **x=1**, x=2, x=3, x=4. The four parties P1, P2, P3, P6 put their shares together (respective values 8, 15, 10, 6). Calculate the secret K. This is an integer.

Convert this integer value K to a byte string as follows. Assume for a moment that the secret K = 25.  
secret_K = 25

secret_byte string = secret_K.to_bytes(2,'big')

Now calculate the sha-256 hash value of the secret byte string. From this byte string, we determine the hexdigest sha-256 value (this is a string of hexadecimal digits) and then convert it to a number (just put 0x in front of it).

We will now use the basic_bc module to make a transaction between Joe and Donald with this hash value and place this single transaction on the first block b0 (index = 0). Afterwards we are going to mine this block, and I ask for the nonce. The previous hash for the first block consists of 64 hexadecimal zeros, the miner of this first block is called "Exam" , and the timestamp of the block is 100010.

joe = basic_bc.MyIdentity("Joe",1)

donald = basic_bc.MyIdentity("Donald",2)

t = basic_bc.MyTransaction(joe, donald, hashvalue, timestamp=100000)

For all parameters not listed, use the defaults as defined in the Python modules "shamir.py" and "basic_bc.py".
```python
>>> from cryptocourse import shamir
>>> from cryptocourse import basic_bc
>>> p = 19
>>> shares = [[1,8],[2,15],[3,10],[6,6]]
>>> joe = basic_bc.MyIdentity("Joe",1)
>>> donald = basic_bc.MyIdentity("Donald",2)
>>> secret_K = shamir.reconstructShares(p,shares)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'cryptocourse.shamir' has no attribute 'reconstructShares'. Did you mean: 'reconstructSecret'?
>>> secret_K = shamir.reconstructSecret(shares,p)
>>> secret_K
13
>>> secret_byte_string = secret_K.to_bytes(2,'big')
>>> import hashlib
>>> hashlib.sha256(secret_byte_string).hexdigest()
'a1f386a0ecb061b3c46a038616212779858ba7258b2eccb818a64986c97282da'
>>> hash_of_secret =0xa1f386a0ecb061b3c46a038616212779858ba7258b2eccb818a64986c97282da
>>> t = basic_bc.MyTransaction(joe, donald, hash_of_secret, timestamp=100000)
>>> t.sign()
>>> b0 = basic_bc.Block(0,[t],'0'*64,"Exam",timestamp=100010)
>>> b0.mine()
>>> b.nonce
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'b' is not defined. Did you mean: 'b0'?
>>> b0.nonce
5119945

# NOT CORRECT SUKA BLYAT
# CORRECT ANSWER IS: 1416084
```