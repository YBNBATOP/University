# Cryptography in the real world
Indy Van Mol - our guest lecturer
He is a part of Cronos group, Piros company
OpenShift - Red Hat version of the Kubernetes.
TPM - chip on motherboard which you can generate asymetric keys with it.
If you do automated stuff - put a check for SHA hashes inside.

Quantum computers are still to be developed, in order to crack RSA hashes.
RSA hashes can be converted to ECC.
In Linux we can find Yescrypt. But mostly we can just use Argon2 for a better hashing, as it does a good job against bruteforcing.

SHA1 is interesting due to the fact, that the files can be different, but the hash of the file can be same.
The famous ed25519 is one of the most optimised ways to actually be generated, and then moved to servers.

As a security guy, you want to make sure that your websites/servers always have the most secure encryptions set
Here is a [good website](https://www.ssllabs.com/ssltest/) to check the level of SSL security.
You need certificates so that people know you are the real one. It is a kind of verification.