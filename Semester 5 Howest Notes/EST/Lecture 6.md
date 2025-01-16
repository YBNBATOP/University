# RFID Part 1 - Introduction
If you ever need to test the equipment - you better have acceptance from the equipment company.
## Radio-Frequency Identification
This is like using electromagnetic fields to track and identify tags.
## Near-Field Communication
This is meant for data exchange, and is also like a better version. NFC though is more about a very specific type.

# RFID Part 2 - Hardware
## How does RFID works
### RFID system
A system at least has a tag (card), antenna, and reader.
There are a couple ways of tags:
- Passive Tag - they get energy from reader
- Active Tag - they have batteries
- BAP (Battery-Assisted) Tag - has a battery to power only some small part of it.

Tags are supposed to emit a electromagnetic field. This thing also has some type of modulation. 
Reader detects the field and decodes it.
Reader then responds with its own signal (usually).

For passive tags, the antenna just acts like a switch and constantly checks for tags.
### RFID spectrum
RFID has also various frequencies it operates with. Low, high and ultra-high frequency.
Low frequency cards are usually not encrypted because they are old.

LF (Low Frequency) Implementation can have a lot of usage. The big thing about it, is that it can be easily replicable.

Finding the values, or type of the "protocol", it is possible to just brute force or fuzzy finding of the type of card.

LF cards can also have various numbers written on them, which actually are meant for the data of the card.

Flipper zero is one of the most useful things that can be used for researching.

HF Implementation is essentially more useful for more communications. This things also have a bunch of standards.

NFC has its own format (but similar to networking) that it sends data like. It also has specific values it can/has send.

The similar part about this cards is that they have various types, and they both are more secure than the other older implementations.

MIFARE Cards are some of the most known ones, and this are typically strange, due to the fact that they are pseudorandomized and have other problems as well.
In terms of accessing, this cards can also have different blocks of data that it can store. So it has data blocks which are parts of sectors. In that case, you can multi-use your card for various zones.

Getting to hack cards is actually pretty easy, in most cases, and the way to get through them is not that bad.

MIFARE PLUS tried to solve most issues like UID reading or guessing keys, or anything else, but it is still possible

MIFARE DESfire - this one is the most secure version of MIFARE at least, hence it is the least informative for security audits.

MIFARE Ultralight - this one is speaking for itself, as first of all it does not contain too much data (only 512 bits = 64 bytes). It works by having a limited amount of usages for a card, if you have limited slots, and then you can just put values in the cells for the data, which already means how many you had.