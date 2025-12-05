# PKI-Based 2FA Microservice

This project implements a PKI-based Two-Factor Authentication (2FA) microservice using RSA 4096-bit Public Key Infrastructure for secure seed exchange and TOTP for authentication. The microservice follows an end-to-end cryptographic workflow: generate RSA keys, request encrypted TOTP seed from the instructor service, decrypt it using the private key, store it persistently, generate TOTP codes using a cron job inside Docker, and verify submitted TOTP codes via API. All required scripts, key files, Docker configuration, and cron automation are included.
