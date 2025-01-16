# Introduction and Analogue signals
## Frequency spectrum and radio bands

### What is software defined radio?
Software-defined radio means that there is a system that looks more like a computer, and hence it is not fully hardware defined radio. It is a part of a system. Like instead of using hardware, some parts are implemented by means of software.
This implementation allow for easier security assessment of radio communication.
Radio signals are used in a bunch of places.
### Electromagnetic spectrum
There are certain frequencies that can be sent via air. Others - they loose a lot of power via the air, hence less probable to use it. This is particularly working for very low frequencies.

Every frequency yet have other bands that vary from Hz values.

Every country has certain allowance to send AM radio signals for example, same works for FM.

Years ago you could create your own radio "station" in order to create something useful (ham radio), however nowadays it is much smaller. That is because most equipment

Ham radio frequency allocation is done by some **International Telecommunication Union (ITU)** in combination with local authorities. 

There is also supposed to be bands and whether they are allowed. Most countries probably have that. To use some bands - you need a certification, so as not to disturb something else. Some thing like this exists in Belgium - BIPT.
### Radio waves
This are created while moving energy inside the antenna. It is overall a combination of electricity and waves variation.
The waves are then sent depending on the antenna itself, depending on its shape and geometry.

Waves have parameters, and in their case we have various parameters that define the difference of waves.
Any signal can be represented as a combination of frequencies.

Sometimes there is a need to modify the frequencies of the waves, in order for the carrier and input to work properly.

Also waves are not that far away from decibels, however decibels are much more scalable in fact.
### Demodulation
This is where you want to modify the way you view the waves, in order to make it more complex.
## DSP (Digital Signal Processing)

# Assignment

Objective: Get to listen to various FM stations from the file. After that, have 2 different radios playing at the same time and being able to listen to both of them at the same time.

What do I have: I have an AM example, and I have the values that change at the same time. I have a test I can then run to understand if the thing will work.
I work with GRC (GNU Radio Companion), and there we have variables, which then can be used all around. QT GUI blocks are all for the visual representation of the thing.

Blocks:
- File source - the file from which we play things
- Throttle - like an amplifier??? This is where the variable is being used and it ups the values to it.
- Signal source - this thing is supposed to create actual frequencies, like a generator?
- Multiply - get both throttle and signal source to work together.
- QT GUI Freq Sink and Time Sink - things that are supposed to change the values on the scale???
- Low Pass Filter - gets rid of smaller values???
- AM Demod - demodulation for audio
- Rational Resampler - resample the sound/frequencies as we did a lot of changes for it???
- 