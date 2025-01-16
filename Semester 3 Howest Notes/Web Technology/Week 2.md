# Web application security
## IDOR
IDOR = Insecure Direct Object Reference
Access control vulnerability
Fix: check if user is allowed to acces the resource/content

## SQLi
Inject malicious SQL
Fix: use prepared statements

## XSS
XSS = Cross-Site Scripting
Inject malicious JavaScript
Three types:
- Reflected XSS
- Stored XSS
- DOM-based XSS
Fix: validate user input

## Brute Force attacks
Guess data in an automated way
Which data:
- Credentials
- Domain names
- Websites
Fix: limit amount of login attempts

# Web server security
## Web server version
Version of the web server is publicly available
On error pages
Fix: 
- Custom error pages
- Disable it (server_tokens off;)

## Unused HTTP methods
Can be abused:
- Unintended actions
Reduce attack surface
Fix:
- Most disabled methods:
	- TRACE
	- DELETE
	- PUT
	- CONNECT
	- OPTIONS

``` 
location / {
	limit_except GET POST { deny all; }
}
```

## Use SSL/TLS + HTTP2
HTTP traffic is cleartext
Can be sniffed by attackers:
- Get your credentials
Fix: encrypt traffic with SSL
Extra's:
- Disable older SSL methods 
- Enable HTTP2 if possible 

## Directory listing
Shows content of folders on your server
Can contain sensitive information
Fix: Disable directory listing
```
autoindex off;
```

# Security headers
## X-Frame-Options
Protects against clickjacking
This HTTP response header can be used to indicate whether a browser should be allowed to render a page in ``` <frame>, <iframe>, <embed> or <object>

```
add_header X-Frame-Options "deny";
```

## X-Content-Type-Options
Defense against fake filetypes
Prevents the browser from guessing the file type and executing the guessed file type. Example: an executable named as a stvlesheet.

``` 
add_header X-Content-Type-Options "nosniff";
```

## HTTP Strict Transport Security
Tells the browser to access a website only through HTTPS.
A normal https redirect: Vulnerable for MIM attacks
Browser makes use of an interanl super-cookie.

## Content Security Policy
A HTTP response header Content-Security-Policy. The policy tells the website what it is allowed to do and not to do.
- The only location to load the images from
- Which scripts are allowed to run
- What will be the location of the form post data
- Report incidents
