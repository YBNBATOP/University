On the course main information, there is a section that says what I need to know. Some of the things I need to know and recognize. Some of the things I do not need to know really deep. (Introduction)

There is also sample exams.
We do not have guess penalty. However in multiple answers, we get penalized for wrong ones.

Theory exam is in Lockdown browser, while the exercises are being in Python

Exercises are more important than theory

```python
>>> plain = 0xAABBCCDDEEF11223344556677889900AABBCCDDEEF11223344556677889900
>>> str   = 0xbcc72b89b2bdd4e521e40b52346e6155de4263b52c2f286fbc31068d594417
>>> cipher = plain^str
>>> hex(cipher)
'0x167ce7545c4cc6c615a15d354ce7f15f75feae6bc33e0a5cf86460fad1dd17'
>>> from operator import xor
>>> cipher2 = xor(plain,str)
>>> cipher2==cipher
True
>>>
# The amount of characters should be the same for the stream and plain
```


```python
>>> masterkey = 0x1234567890ABCDEFFEDCBA09876543211234567890ABCDEFFEDCBA0987654321
>>> subkey1 = 0x1234567890ABCDEF
>>> subkey2 = 0xFEDCBA0987654321
>>> subkey3 = 0x1234567890ABCDEF
>>> subkey4 = 0xFEDCBA0987654321
>>> from cryptocourse import permute
>>> plain  = 0x11223344556677888877665544332211
>>> p1 = 0x1122334455667788
>>> p2 = 0x8877665544332211
>>> p2.bit_length()
64
>>> cipher1 = 0x8293c31bfc33f5c4
>>> cipher1 = xor(cipher1, subkey1)
>>> cipher1 = permute.permute(cipher1,[2,3,1,4,6,7,0,5])
>>> cipher1 = xor(cipher1, subkey2)
>>> cipher2 = 0xc4f533fc1bc39382
>>> cipher2 = xor(cipher2, subkey1)
>>> cipher2 = permute.permute(cipher2, [2,3,1,4,6,7,0,5])
>>> cipher2 = xor(cipher2, subkey2)
>>> input3  = xor(p2, cipher1)
>>> hex(input3)
'0xeec7f73f64c6f408'
>>> input3  = 0xeec7f73f64c6f408
>>> cipher3 = 0x28c6687543b4bf30
>>> cipher3 = xor(cipher3,subkey1)
>>> cipher3 = permute.permute(cipher3, [2,3,1,4,6,7,0,5])
>>> cipher3 = xor(cipher3, subkey2)
>>> hex(cipher1), hex(cipher2), hex(cipher3)
('0x66b0916a20f5d619', '0x9657d78d46b3267f', '0xe10f6504755f7d53')
>>>
# Inverse S-Box is needed when decryting. Normal one - when encrypting.
```

#rsa
```python
>>> p = 182353
>>> q = 112771
>>> n = p*q
>>> totient = (p-1)*(q-1)
>>> e = 63557
>>> d = euclidean.mulinv(e,totient)
>>> encrypt = pow(12345678,e,n)
>>> decrypt = pow(87654321,d,n)
>>> encrypt, decrypt
(4932240471, 2180591901)
>>>
```

#rsa
```python
>>> p = 37752007
>>> q = 40770133
>>> n = p*q
>>> totient = (p-1)*(q-1)
>>> e = 65537
>>> d = euclidean.mulinv(e,totient)
>>> encrypt = pow(123456,e,n)
>>> decrypt = pow(654321,d,n)
>>> encrypt, decrypt
(1530737875555856, 234522041167010)
>>>
```

#stream-cipher
```python
>>> plain = 0x100200300400500600700800900A00B00C00D00E00F00000
>>> str   = 0x55abc1105990a326f9828613112d41abc7cd80f8bb2410c6
>>> cipher= xor(plain,str) # OR plain^cipher
>>> cipher
1708134318441455519036260981760054765789455217027880063174
>>> hex(cipher)
'0x45a9c1205d90f320f9f28e138127411bcbcd50f6bbd410c6'
>>>
```

#secret-sharing
```python
>>> sercret = 98342
>>> n = 5
>>> t =3
>>> sharess = shamir.generateShares(n,t,sercret)
>>> sharess
[[498143506, 450553415], [61693611, 774706504], [1297431244, 1488464262], [1299290816, 1160229502], [831130533, 42520358]]
>>> sharesx = [[498143506, 450553415], [61693611, 774706504], [1297431244, 1488464262]]
>>> reconstructed_secret = shamir.reconstructSecret(sharesx)
>>> reconstructed_secret
98342
>>>

# YOU CAN ALSO ADD A PRIME

>>> p = primes.findAPrime(100000,150000)
>>> p
127703
>>> shares = shamir.generateShares(n,t,sercret,p) # THE PRIME IS IMPORTANT
>>> shares
[[11605, 84186], [17282, 58458], [121394, 44416], [121753, 13732], [76261, 82995]]
>>> shamir.reconstructSecret(shares,p) # THE PRIME IS IMPORTANT
98342
>>>
```

#transactions/mining
```python
>>> from cryptocourse import basic_bc
>>> joe = basic_bc.MyIdentity("Joe")
>>> donald = basic_bc.MyIdentity("Donald")
>>> tr = basic_bc.MyTransaction(donald,joe,100)
>>> tr.sign()
>>> bl = basic_bc.Block(1000, [tr], '0'*64)
>>> bl.mine()
>>> bl.nonce
1899883
```