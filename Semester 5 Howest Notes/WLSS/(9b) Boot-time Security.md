The moment the PC boots, there are already some things that are put to work (security wise)
# BIOS vs UEFI
Windows 11 was the  first one to have requirements for the OS, which is Trusted Platform Module (which is a place, hardware wise, that can store some keys)

BIOS (or UEFI) is like a hardware initialization. UEFI is more security enhanced than BIOS.
With UEFI we also started to have GPT. On Linux you can have more compatibility.
BIOS reads boot code from the MBR.
With GPT we have a dedicated partition for boot code (bootmanager files). Typically the 100mb reserved EFI partition.
Fun fact with Windows 11, the last partition (like 700mb) is the recovery partition, which is a lightweight Windows Recovery Edition (RE) installed, to then fix your shit.

# Secure boot process
Secure boot is used for authenticity. I.e. you can boot only things that have been signed
UEFI ensures secure boot (only signed boot loaders)
Secure boot checks the kernel already, so things that various components are not tampered with.

Security Processor is essentially your TPM module on the motherboard.
# TPM - Implementations
There is different type of TPMs:
- Dedicated chip on the hardware
- Firmware TPM (motherboard hardware, UEFI+CPU)
- Integrated TPM (built into the CPU)

You can also have virtual TPMs with the 