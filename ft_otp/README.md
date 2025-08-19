# ft_otp – One-Time Password Generator (HOTP)

## 📝 Project Overview
This project implements a **One-Time Password (OTP) generator** based on the **HOTP algorithm (RFC 4226)**. The program allows storing a hexadecimal key securely in an encrypted file and generating OTP tokens on demand.


## ⚙️ Features
- Encrypts and stores a 64-character hexadecimal key in `ft_otp.key`
- Generates 6-digit one-time passwords using the stored key
- Uses **HOTP** algorithm without relying on external TOTP libraries
- Provides compatibility for verification with tools like `oathtool`


## 📂 Usage

### 1. Store a new key
```sh
python hotp.py -g <keyfile>
```
- `<keyfile>` contains a 64-character hexadecimal key.
- Example:
```sh
echo -n "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef" > key.hex
python hotp.py -g key.hex
```
- Output:
```
Key successfully saved to 'ft_otp.key'.
```

### 2. Generate a one-time password
```sh
python hotp.py -k ft_otp.key
```
- Outputs a 6-digit OTP(OTP changes every 30 seconds, similar to TOTP behavior):
```
OATHTOOL 32 key : XXXXXX
MY OTP : XXXXXX
```
- Use the Base32 key printed by the script `OATHTOOL 32 key : XXXXXX` to verify the OTP:
```sh
oathtool --totp -b <OATHTOOL 32 key>
```

### Notes
- If the key is invalid (not 64 hex characters), an error will be printed.
- The program prints a base32-encoded key for verification with tools like `oathtool`.


## 🎯 Purpose
The goal of this project is to:
- Implement the **HOTP algorithm** manually
- Work with **file encryption** using Python's `cryptography` library
- Gain experience with **one-time password generation** and security practices

