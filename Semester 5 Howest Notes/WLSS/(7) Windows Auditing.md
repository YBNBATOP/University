# General
Auditing is tracing actions that happened on the machine.
You can do forensic analysis, regulatory compliance, and user activity
# Audit policies
You can have group policies, and hence manage and configure Windows for end users. (gpedit)
You can then have security policies, which is a subset. (secpol)
Or you can have even a smaller subset, called audit policies.

To enforce the policies, we have LSASS.

 There is local audit policies, and advanced audit policies.
 The second one is much better, as it is more system wide, and with a whole set of policies. There are only 9 policies, and in there we have more "subcategories". It is more finegrained
 With advanced policies it can also happen that you can have default values, that will work no matter what. By default, the advanced policies are working.

# What to audit
Microsoft has a whole online page that says a baseline for various things, and what you should do.
## Windows Security Baseline
It is in general some rules that Microsoft recommends turning on. Like a whole lot of rules to be turned on at the same time.
# Event viewer
It is a tool where you can see "logs" of various things. Like user activity for example.
Funny thing is that new events need to be manually refreshed.
# Sysmon
It is a tool for sysinternals suite
It is supported on Linux
# File access auditing
Audit file system is the starting point for such things, and then you can go deeper into various things.

Global Object Access Auditing (GOAA) is related to the file system auditing (from the Advanced security policies). It also works for more than one specific file, it works for multiple ones.
# Active Directory auditing
You can also have various levels of logging, for events, because that is favorable for us.

