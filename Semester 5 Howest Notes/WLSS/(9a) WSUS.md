WSUS is here to avoid possible breaches. This is Windows Updates, that actually have to be constantly pushed (or allowed to be pushed by the administration) onto the systems.

WSUS is like an update orchestration, that can show you a database of the updates that can be pushed onto the various machines.

WSUS = Windows Server Update Services
Instead of having direct updates from cloud to the machines, you need a **WSUS server** in between to have update sources. So you always go through it.
You can also have load balancing of this WSUS servers (so have more than 1 of them)

A Windows server can have the WSUS role just by installing it. The moment the server becomes WSUS, it actually dumps uploads via HTTP. So it automatically becomes a webserver (IIS)

After you install it, you need to configure it (where to get the updates from).
There is also different classifications of the update (types)

WSUS groups are not the same as AD directories. WSUS also have GPOs, and then we can specify that things can be linked to certain computers.

WSUS can also (kind of) provide software updates. However, for that you need **Configuration Manager** to be also configured.

