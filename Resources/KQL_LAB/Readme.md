
# 🔍 KQL LAB — Learn KQL the Real Way

> Built by [@AbbasMurshid](https://github.com/AbbasMurshid) | SOC Analyst | SC-200 Candidate  
> A self-built KQL learning ecosystem with a real ADX log environment, a personal handbook, and CTF-style challenges.

---

## 📦 What's Inside

| Resource | Description |
|----------|-------------|
| 📘 KQL Handbook | Personal reference guide covering operators, functions & patterns |
| 🗄️ ADX Log Environment | Realistic noisy logs hosted on Azure Data Explorer (free to query) |
| 🎯 KQL Challenges | CTF-style challenge UI with AI-powered answer validation |

---

## 🌐 Live Resources

| Resource | Link |
|----------|------|
| 📘 KQL Handbook (Live) | [Open Handbook](https://abbasmurshid.github.io/Cybersecurity-Writeups/Resources/KQL_LAB/index.html) |
| 🎯 KQL Challenges (Download) | [Download HTML](https://github.com/AbbasMurshid/Cybersecurity-Writeups/blob/main/Resources/KQL_LAB/KQL_CHALLANGES.html) |

---

## 🗄️ Connect to the ADX Log Environment

The logs are hosted on **Azure Data Explorer (ADX)** — free to query, no sign-up required beyond a Microsoft account.

### ADX Cluster URI (for querying)
```
https://kvc-0x665wr0tsbfqb9aez.australiaeast.kusto.windows.net
```
> ⚠️ This is the only URI you need to query the logs.  
> The Data Ingestion URI is for loading data — ignore it as a learner.

### How to Connect — Step by Step

1. Go to **[dataexplorer.azure.com](https://dataexplorer.azure.com)**
2. Sign in with any **Microsoft account** (free Outlook/Hotmail works)
3. Click **"Add cluster"** (top left)
4. Paste the Cluster URI:
   ```
   https://kvc-0x665wr0tsbfqb9aez.australiaeast.kusto.windows.net
   ```
5. Click **Connect**
6. You'll see the **SOC LAB** database appear in the left panel
7. Expand it — you'll find tables like:
   - `SecurityEvent`
   - `SigninLogs`
   - `DeviceLogonEvents`
   - `DnsEvents`
   - `AzureActivity`
   - `OfficeActivity`
   - and more...

8. Open a **new query tab**, select the `SOC LAB` database, and start writing KQL!

### Quick Test Query
```kql
SecurityEvent
| take 10
```

---

## 🎯 How to Use the KQL Challenges

The challenge file is a standalone HTML app — no installation needed.

1. Download `KQL_CHALLANGES.html` from the link above
2. Open it in any browser (Chrome / Edge recommended)
3. Each challenge gives you:
   - A **scenario** describing what to hunt for
   - A **query editor** to write your KQL
   - **AI validation** (Groq API) that checks your logic and gives feedback
4. Run your queries in the ADX environment above, then validate your answer in the challenge UI

---

## 📘 How to Use the KQL Handbook

The handbook is a live reference site — use it alongside the challenges.

- **[Open Handbook →](https://abbasmurshid.github.io/Cybersecurity-Writeups/Resources/KQL_LAB/index.html)**
- Covers: filtering, aggregation, joins, time functions, string operators, and more
- Written from scratch — not a copy of Microsoft docs

---

## 🗺️ Recommended Learning Path

```
1. Open the Handbook → read the operators section
2. Connect to ADX → run the quick test query
3. Explore the tables → understand the log schema
4. Open the Challenges → start from Challenge 1
5. Use the Handbook as reference while solving challenges
6. Validate answers in the challenge UI
```

---

## 🛠️ Built With

- **Azure Data Explorer (ADX)** — log hosting & querying
- **KQL (Kusto Query Language)** — query language
- **Groq API** — AI answer validation in the challenge UI
- **GitHub Pages** — handbook hosting

---

## 🙋 About

I'm Abbas, an entry-level SOC Analyst preparing for the **SC-200** exam.  
I built this entire lab from scratch because I couldn't find a realistic, free KQL practice environment.

📎 Portfolio: [abbas-portfolio-ecru.vercel.app](https://abbas-portfolio-ecru.vercel.app)  
🔗 LinkedIn: [linkedin.com/in/abbas-murshid-m](https://linkedin.com/in/abbas-murshid-m)

---

⭐ If this helped you, consider starring the repo — it helps others find it!
