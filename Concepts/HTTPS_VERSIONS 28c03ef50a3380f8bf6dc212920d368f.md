# HTTPS_VERSIONS

## 💡 What Is **HTTP Version**?

When your **browser (client)** talks to a **server**, both need to agree *which version of HTTP protocol* to use.

This is written in the **request line**:

Example:

```
GET /index.html HTTP/1.1

```

Here:

- `HTTP/1.1` means the client and server are using **version 1.1** of the HTTP protocol.

Every new version of HTTP improves **speed**, **security**, and **efficiency**.

---

## 🧩 Versions Explained One by One

---

### 🔹 **HTTP/0.9 (1991)** — The Stone Age

- The **first and simplest** version of HTTP.
- Only supported **GET** requests.
- No headers, no status codes, no metadata — just raw data.

📄 **Example Request:**

```
GET /page.html

```

📄 **Example Response:**

```
<html><body>Hello Abbas!</body></html>

```

That’s it.

No `HTTP/0.9 200 OK`, no content type, nothing — just the page.

⚠️ It was very limited. No POST, no cookies, no images, no JSON. Just plain HTML.

---

### 🔹 **HTTP/1.0 (1996)** — The Foundation

This version made the **web actually usable**.

✅ Added:

- **Headers** (like `Content-Type`, `User-Agent`, etc.)
- **Different content types** (images, audio, etc.)
- **Status codes** (like 200 OK, 404 Not Found)
- **Basic caching**

📄 **Example Request:**

```
GET /index.html HTTP/1.0
Host: example.com

```

📄 **Example Response:**

```
HTTP/1.0 200 OK
Content-Type: text/html
Content-Length: 50

<html>Hello Abbas!</html>

```

⚠️ Problem: It opened a new **TCP connection** for every request — which made it **slow**.

---

### 🔹 **HTTP/1.1 (1997)** — The Long Reign 👑

This version **fixed** most of HTTP/1.0’s issues and became the **most widely used version** even today.

✅ Added:

- **Persistent Connections** → The same connection can be reused for multiple requests (faster)
- **Chunked Transfer Encoding** → Server can send data in parts (useful for large files)
- **Better caching & compression**
- **Host header required** (helps with virtual hosting)

📄 **Example Request:**

```
GET /home HTTP/1.1
Host: example.com
Connection: keep-alive

```

📄 **Example Response:**

```
HTTP/1.1 200 OK
Content-Type: text/html
Transfer-Encoding: chunked

<html>Welcome Abbas</html>

```

⚠️ Still uses **one request per stream**, meaning one file (CSS, image, etc.) at a time — slower for modern web pages with many resources.

---

### 🔹 **HTTP/2 (2015)** — The Speed Booster ⚡

Now things get exciting.

✅ Added:

- **Multiplexing** → Multiple requests in one single connection (faster)
- **Header Compression** → Reduces size of repeated headers
- **Prioritization** → Important files load first (like CSS before images)
- **Binary Protocol** → Faster for machines to read

📄 **Example Difference:**

In HTTP/1.1 — browser loads:

```
GET /index.html
GET /style.css
GET /image.png

```

➡ These happen one by one (or a few at a time).

In HTTP/2 — all requests happen **together** in one stream — blazing fast 🚀

**Use case:** When you open YouTube, hundreds of requests load in milliseconds — that’s HTTP/2 power.

---

### 🔹 **HTTP/3 (2022)** — The Modern Beast 🔐

This is the **latest** and **fastest** version.

✅ Built on a **new transport protocol called QUIC** (based on UDP instead of TCP).

✅ Reduces delay (latency) drastically.

✅ Stronger **encryption** and **error recovery**.

✅ Designed for **mobile and unstable networks** (less packet loss).

📄 **Example:**

Still looks the same to you:

```
GET /video.mp4 HTTP/3
Host: youtube.com

```

But inside, it uses QUIC — faster, more reliable, encrypted from the start.

**Use case:** Google, YouTube, Facebook, and Cloudflare already use HTTP/3.

---

## ⚙️ Summary Table

| Version | Year | Key Features | Speed | Security | Still Used? |
| --- | --- | --- | --- | --- | --- |
| HTTP/0.9 | 1991 | Only GET, no headers | 🐢 Very slow | ❌ None | ❌ No |
| HTTP/1.0 | 1996 | Headers, caching | 🐢 Slow | ⚠️ Basic | ⚠️ Rare |
| HTTP/1.1 | 1997 | Persistent connections | 🚗 Medium | ✅ Good | ✅ Yes |
| HTTP/2 | 2015 | Multiplexing, compression | 🚀 Fast | ✅ Strong | ✅ Yes |
| HTTP/3 | 2022 | QUIC, encryption | ⚡ Super fast | 🔒 Excellent | 🌍 Growing |

---

## 🔐 In Cybersecurity Terms

You must **check which HTTP version a site uses** because:

- Older versions (like 1.0) may lack **TLS encryption**, **authentication**, or **security headers**.
- Modern versions (2 & 3) are **faster** and **more secure**, reducing risk from attacks like **MITM (Man-in-the-Middle)**.

You can check it using:

```
curl -I -v https://example.com

```

This command shows:

```
> GET / HTTP/2

```

That means the site supports HTTP/2.