# Hardware attacks
The first things that can be/want to be tampered with, is the transistors.
There is always present a certain system of random number generation, which can be vulnerable, because you can predict it sometimes.

Every piece of hardware has some delay, and it can be used to make some special timing tampering (jitter)

You can have True and Pseudo random number generation (TRNG, PRNG)
The hard thing about this kind of generation, is the hardware, for which we want to generate the values.

We can also make the machine work slower, by doing under-powering

# Side-channel attacks
This is more related towards the chips itself.
The methods are similar to Hardware, but slightly different:
- Power
- Timing
- Radiation (EM)
- Peripherals 

Side-channel is usually possible because of the way hardware works, and not bugs themselves.
## Power
Lets see how much power we are consuming, and check

# Cracking RSA keys
```python
>>> from cryptocourse import primes
>>> from cryptocourse import rsa_square_attack
>>> p = primes.findAPrime(100,120)
>>> q = primes.findAPrime(100,120)
>>> p, q
(101, 113)
>>> n = p*q
>>> n
11413
>>> pow(11413, 0.5)
106.83164325236227
>>> pow(107,2)
11449
>>> 11449-n
36
>>>
```
If the value, at the end, is a square - then you crack the system. This problem is known as common RSA.
```python
>>> from cryptocourse import primes
>>> from cryptocourse import rsa_square_attack
>>> p = primes.findAPrime(10000000,50000000)
>>> q = primes.findAPrime(10000000,50000000)
>>> n = p*q
>>> n
471682159907929
>>> factors = rsa_square_attack.factor(n)
>>> factors
(18171779, 25956851)
>>> p, q
(18171779, 25956851)
>>> q = primes.findAPrime(100000000,500000000)
>>> p = primes.findAPrime(100000000,500000000)
>>> factors = rsa_square_attack.factor(p*q)
>>> factors
(272867953, 374594587)
>>> p = primes.findAPrime(pow(2,1020), pow(2,1025))
>>> q = primes.findAPrime(p, p+pow(2,520))
>>> (p-q).bit_legth()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'int' object has no attribute 'bit_legth'. Did you mean: 'bit_length'?
>>> (p-q).bit_length()
520
>>> pow(2,520)
3432398830065304857490950399540696608634717650071652704697231729592771591698828026061279820330727277488648155695740429018560993999858321906287014145557528576
>>> p
286794630529361816869926309384982431188009431973958402341794968203229957055947708961108195713364626207829923779848919990495770315750623978474119514395667175030440636186402643071076514657386338612914324561412831213290662432223986473743542552160204720661940394520750551330433034140772541923502465105244413034737
>>> q
286794630529361816869926309384982431188009431973958402341794968203229957055947708961108195713364626207829923779848919990495770315750623978474119514395669051876086397570340500528424949347024598227845903623621918102584607085267667336329288179073432168926722420401450929808156428022652543803765840341557880204297
>>>
```
The difference between p and q should be more than half of the bits.
**rsa_square_attack** is meant to find the values of the squares itself.
```python
>>> n = p*q
>>> rsa_square_attack.factor(n)
(286794630529361816869926309384982431188009431973958402341794968203229957055947708961108195713364626207829923779848919990495770315750623978474119514395667175030440636186402643071076514657386338612914324561412831213290662432223986473743542552160204720661940394520750551330433034140772541923502465105244413034737, 286794630529361816869926309384982431188009431973958402341794968203229957055947708961108195713364626207829923779848919990495770315750623978474119514395669051876086397570340500528424949347024598227845903623621918102584607085267667336329288179073432168926722420401450929808156428022652543803765840341557880204297)
>>>
```
The difference should not be too small.



