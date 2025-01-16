During the lesson we can have physical contact, and we have to prepare stuff before the lesson.

We are also supposed to actually look through stuff ourselves.

3rd year study. Topic quite different from others

It is not really mathematics, but looks like it.

You need to know what you are doing when you apply cryptography

Course material is usually a video and you can learn it yourself.

Exam:
- 50% theory exam + 50% exercises (2 part exam)
- Quizzes are not valued for score

Make sure to put more power into exercises (Prioritize)

The theory is closed book (no open question, multiple choice), exercises are open book (everything on the laptop, no communication, also can be multiple choice solutions)

For the exercises - if you do not have the right solution but you have the python, you can get at least part of the score

Also modules can have additional information that does not need to be studied.

The idea is that we have courses every 2 weeks.

Questions in the exam are always in 2 languages.

# Exercises
For the Python, we are going to use **cryptocourse** library with the pip install

The purpose is just to make python calculations (you use it as a calculator)

for example converting hexadecimal ABCDEF1234567890, you can simply type 0x in front, to get the int. or do `int("ABCDEF1234567890",16)` and get the value

XOR = if the values are different - it is 1. If they are the same - it is 0.

K,P XOR

C = P XOR K
D = C XOR K

D = P XOR K XOR K
D = P XOR 0 => P (why? because in XOR if they are the same, then it is 0)
So overall, if you try to encrypt a message with a key, then the decryption will be equal to the initial message

If you only know the cyphertext, the initial plain text can be ANYTHING

The doubling issues are interesting, as for example:
you have flowers that double every night in a pond. On day 30 the pond is full. Then on day 29 the pond will be half full.

While doing exercises, we are going to encrypt bite strings (b'This is a text'), or numbers.

To do XOR with numbers, you do not only need the binary representation.

^ is the sign for XOR.

NOTE: any binary is preceded by 0s
# Symetric ecnryption
Uses the same key, and the asymetric uses private and public key for encryption.

# Modulo
Modulo is the remainder of division
10x4%17 = 6
because 10x4 = 40
17 + 17 = 34
40 - 34 = 6

2x3%8 = 6 because the value of 8 can not be included in the other value
2x1%8 = 2

Multiplicative inverse is when you invert the numbers you multiply are changed vice versa 

Euclidian most common divisor is to find the divisor that works for 2 numbers (or maybe more)

The whole idea about modulo is to find finite fields

Modulo does not change the order of the operations (if you have addition)

