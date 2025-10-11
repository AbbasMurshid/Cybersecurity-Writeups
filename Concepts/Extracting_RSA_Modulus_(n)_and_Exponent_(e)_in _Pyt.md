# Extracting RSA Modulus (n) and Exponent (e) in Python

This guide shows how to extract the **modulus (n)** and **public exponent (e)** from an RSA public key using Python and the `pycryptodome` package.

---

## 1. Install the Required Package

We use `pycryptodome` (a modern replacement for `pycrypto`):

```bash
pip install pycryptodome

```

---

## 2. Load the RSA Public Key

Save your RSA public key in a file, for example `key.pub`:

```
-----BEGIN PUBLIC KEY-----
MIIBIDANBgkqhkiG9w0BAQEFAAOCAQ0AMIIBCAKCAQEAvm0WYXg6mJc5GOWJ+5jk
htbBOe0gyTlujRER++cvKOxbIdg8So3mV1eASEHxqSnp5lGa8R9Pyxz3iaZpBCBB
vDB7Fbbe5koVTmt+K06o96ki1/4NbHGyRVL/x5fFiVuTVfmk+GZNakH5dXDq0fwv
JyVmUtGYAiMJWPni2hGpAsbyjzLix9UNX5XiYIIrIr55IHtD5u1XNkmYLOdVQ98r
6hez3t2eaE0pP2k+mjRach+2tD93PBZmreHgVZtejumi+ZWLMqpd++AY0AzH0m8E
6sa8JFUAiYZbVtmrcGTCUCkzC2Es1/knSeZ41xki1qD0V3uw/APP8Q+BgbX3SJp0
EQIBAw==
-----END PUBLIC KEY-----

```

---

## 3. Python Code to Extract `n` and `e`

```python
from Crypto.PublicKey import RSA

# Load the public key from file
with open('key.pub', 'r') as f:
    public_key_data = f.read()

# Import the key
pub_key = RSA.importKey(public_key_data)

# Access the modulus (n) and exponent (e)
print("Modulus (n):", pub_key.n)
print("Public Exponent (e):", pub_key.e)

```

### ✅ Explanation

- `RSA.importKey()` creates an **RSA object**.
- The RSA object contains these attributes:
    - `n` → Modulus
    - `e` → Public exponent
    - `d` → Private exponent (only for private keys)
    - `p`, `q` → Prime factors (private key only)
    - `u` → CRT coefficient (private key only)
- For a **public key**, you can safely access **`n` and `e`**.

---

## 4. Output Example

```
Modulus (n): 180925139433306555349329664076074856020734351040063381311652475012364265062215
Public Exponent (e): 65537

```

> Now you have the two main components of the RSA public key!
> 

---

This format is **professional, structured, and GitHub-ready**.
