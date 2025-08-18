# OWASP

## Overview

The **O**pen **W**orldwide **A**pplication **S**ecurity **P**roject (OWASP) is a nonprofit foundation dedicated to improving software security.

OWASP has a set of security standards that we need to follow to have a secure application.

## Important Rules

### Broken Access Control 🔓

When someone shouldn't have access to something, but they can snoop around.

Example: In an online store, you shouldn't be able to see other people's orders. But if you have the link to someone's order and it opens without a password, that's an access control issue.

### Cryptographic Failures 🔐

When sensitive information is not properly secured.

Example: A website storing your banking information plainly (e.g., 1234 5678 9012 3456) or using HTTP instead of HTTPS.

### Injection 💉

When an attacker can send their own code into your application and execute it.
Such as SQL injection or shell injection attacks.

### Insecure Design 🏗️

When the system is designed incorrectly from the start and security is not considered.

Example: An app that accepts user passwords without length or complexity limitations, like letting someone set their password as "1234".

### Security Misconfiguration ⚙️

When the website or server is not configured correctly.

Example: A website that allows everyone to view its server files (e.g., opening `/config/settings` and seeing sensitive information).

### Vulnerable and Outdated Components 🧩

When you use outdated software or libraries that have known security vulnerabilities.

### Identification and Authentication Failures 🔑

When the system fails to properly identify the user or its login method isn't secure.

Example: A website that doesn't lock an account after several failed login attempts, allowing an attacker to try countless times to guess the password.

### Software and Data Integrity Failures 🛠️

When data or updates are not secure and can be tampered with.

Example: An app that gets its updates from untrusted sources, allowing an attacker to inject malicious code into the updates.

### Security Logging and Monitoring Failures 📋

When the system cannot log or track suspicious events.

Example: An attacker breaks into a website and no one notices because the system has no event logging.

### SSRF (Server-Side Request Forgery) 🕵️

When an attacker forces the server to send a request on their behalf.

Example: A user is asked to enter an image URL, e.g., `https://example.com/image.jpg`.
An attacker could enter an internal address instead: `http://localhost/admin`.
Since the request comes from the server, it may access sensitive information like the admin panel.
