# Main
PAM stands for Pluggable Authentication Method.
NSS - Name Service Solution
## NSS
This has a configuration in cat /etc/nsswitch.conf
This defines databases and sources for those databases. This is more like a router towards files that should be handled in terms of users, hosts, and etc.
Systemd can have users on the fly.
You just look for certain resources.
## PAM
Pluggable Authentication Method
Before, there was **/etc/login.defs**
PAM defines the authentication for whatever uses the authentication.

### Configuration
type + control flags  + module
#### Control Flags
4 control flags:
- Sufficient - if you have success then you succeed
- Requisite - if you fail, you stop immediately
- Required - if failed, then will not fail immediately
### Architecture
Applications use PAM, and PAM talks to /etc/pam.d and config files, then PAM Modules, and gets back to application.
Remember nologin files? Now you can just add a PAM module, which restricts everyone except **root**. Just by being present there - it will do that.