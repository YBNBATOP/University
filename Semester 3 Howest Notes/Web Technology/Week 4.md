Autherntication & WAF

# Authentication
## General idea

Authentication is a security process that ensures and confirms a user's idientity, typically username/password verification by the server

## How it works
- User enters his login credentials
- Server verifies the credentials of the user, creates a session and stores it in the database
- A cookie with the sessionID is placed in the user's browser
- Every request will contain this sessionID cookie and is veified against the database. If the sessionID client varies from the ID in the database, the request will be blocked
- Once a user logs out of the app, the session is destroyed on both client and server

## Authentication vs Authorization

### Authentication
- Who is the user?
- Confirmation of identity
- Usually done using username and password

### Authorization
- What is the user allowed to do
- Access granted, based on identity
- Done after authentication



## Ways to authenticate
### Knowledge
- Something the user knows
- Password, PIN code, ...
	- Vulnerable to phishing

### Possession
- Something the user has
- ID card, token
	- Vulnerable to theft

### Inherence
- Something the user is
- Fingerprint, retina scan
	- Vulnerable to replication (impersonation)
# Basic authentication
HTTP Basic Authentication is the simplest technique for enforcing access controls to web resources

- No cookies
- No session identifiers
- No login pages

HTTP Basic Authentication uses standard fields in the HTTP header

A request contains a header field 

The credentials are base64 encoded and contain an id and password joined by a single colon:

If a server receives valid credentials that are not adequate to gain access for a given resource, the server should respond with the 403 Forbidden status code
## Basic Authentication in NGINX
Install apache2-utils

Create a .htpasswd file with htpasswd
``` bash
$ sudo htpasswd -c /etc/apache2/.htpasswd user1
```
For other users, leave out the -c
```bash
$ sudo htpasswd /etc/apache2/.htpasswd user2
```
Output is the username with hashed passwords
```bash
$ cat /etc/apache2/.htpasswd
user1:$apr1$/woC1jnP$KAh0SsVn5qeSMjTtn0E9Q0
user2:$apr1$QdR8fNLT$vbCEEzDj7LyqCMyNpSoBh/
user3:$apr1$Mr5A0e.U$0j39Hp5FfxRkneklXaMrr/
```

Configuration view:
``` bash
location /protected {  
	auth_basic “Administrator’s Area”;  
	auth_basic_usefile /etc/apache2/.htpasswd;  
}
```

# Digest Authentication

Provides an alternative to Basic Authentication where the password  is not transmitted as clear-text

No significant security advantage over Basic Authentication. The password storage on the server is much less secure with Digest Authentication than with Basic Authentication (only MD5)

Using Basic Authentication and encrypting the whole connection with TLS is a much better alternative

Digest Authentication is not installed in NGINX by default




# oAuth
oAuth is an authorization framework that enable applications - such as Facebook, GitHub, X,... - to obtain limited access to user accounts  on an HTTP service. It works by delegating user authentication to the service that hosts a user account and authorizing third-party applications to access that user account.

oAuth provides authorization flows for web and desktop applications, as well as mobile devices

## oAuth terms

**Client** - An application which accesses protected resources on behalf of the resource owner (such as a user). The client could be hosts on a server, desktop, mobile, or other device

**Grant** - A grant is a method of acquiring an access token

**Resource server** - A server which sits in front of protected resources (for example "tweets", user's photos, or personal data) and is capable of accepting and responding to protected resource requests using access tokens

**Resource owner** - The user who authorizes an application to access their account. The application's access to the user's account is limited to the "scope" of the authorization granted (e.g. read or write access)

**Scope** - A permission

**JWT** - A JSON Web Token is a method for representing claims securely between two parties as defined in RFC 7519

## oAuth flows
There are 2 most common flows in oAuth
- oAuth authentication
- oAuth resources

### oAuth authentication
Using a third party to handle authentication

For example:
Logging in with your Google Account at Epic Games

### oAuth resources
Using a third party to handle authentication and access resources from the platform.

For example:
Logging in with your Google Account and give WhatsApp access to backup to Google Drive

### oAuth roles
OAuth defines four roles:
- Resource Owner: The resource owner is the user who authorizes an application to access their account. The application's access to the user's account is limited  to the scope of the authorization granted
- Client: The client is the application that wants to access te user's account. Before it may do so, it must be authorized  by the user, and the authorization must be validated  by the API
- Resource server: The resource server hosts the protected user accounts
- Authorization Server: The authorization server verifies the identity of the user then issues  access tokens to the application

Example with Google:
- Resource owner: you
- Client: WhatsApp
- Resource Server: Google Drive server
- Authorization Server: Google authentication server

### Steps
The application requests authorization to access service resources form the user

If the user authorized the request, the application receives an authorization grant

The application requests an access token from the authorization server (API) by presetting  
authentication of its own identity, and the authorization grant

If the application identity is authenticated and the authrorization grant is valid, the  
authorization server (API) issues an access token to the application. Authorization is  
complete

Now the application can request resources from the resource server and presents the  
access token



# WAF
## What is a WAF
A WAF or Web Application Firewall helps protect web application by filtering and  monitoring HTTP traffic between  a web application and the internet

It typically protects web application from attacks such as cross-site forgery, cross-site-scripting (XSS), file inclusion and SQL injection,...

A WAF is a protocol layer 7 defence and it is not designed to defend against all types of attacks

A WAF operates through a set of rules often called policies. These policies aim to protect against vulnerabilities in the application by filtering out malicious traffic.

The value of a WAF comes in part from the speed and ease with which policy modification can be implemented, allowing for faster response to varying attack vectors; during a DDoS attack, rate limiting can be quickly implemented by modifying WAF policies