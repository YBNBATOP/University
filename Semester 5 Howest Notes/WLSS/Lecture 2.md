# Shells and more
Shell != terminal

Terminal - is the window where you type your commands and etc.
it is just a screen that allows to talk to your computer
Terminal is only the look and feel

Also we have the tty which are pseudo terminals. They are hardcoded in the linux.

Tools (mostly for multiplexers):
- screen
- tmux
- zellij

Shells are fun
Because the shells can manipulate commands:
- find / -name "res*"
- find / -name res*

In the case above, the top command is what you want, because the find command will see the **res** will be seen properly

In the second case, it first expands the res* and then it does the initial command.

Errors are not pipped by default to the other command
You can save errors as primary output, by doing **2>&1** - but this will be regular and error output
The order of the redirects is also a very interesting thing
for example 2>&1 1>/dev/null is the right way to redirect errors to main, and then the main to dev null, so you are left with errors only.

## Different shells
You have different shells and can easily change between them, or those can be not used

## SSH
### SSH tunneling
This can be used to tunnel the traffic somewhere else. Like you can revert any traffic on a port to go anywhere else, or even show information that needs to be exported.

So creating tunnels can be super super useful.

You can change the setting for the ssh, while having an ssh session logged in, and you can do it in a very specific way.