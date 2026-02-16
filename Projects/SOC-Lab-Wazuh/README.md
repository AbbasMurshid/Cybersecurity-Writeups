# Home SOC Lab: Threat Detection, Attack Simulation & Incident Investigation

# Objectives

---

**This project involves deploying the SOC Lab (Wazuh environment) to monitor endpoint activity and simulate common real-world attack techniques on endpoints, generating alerts in Wazuh.  Finally, we investigate the alert as a SOC Analyst.**

*Now! lets see the System Architectures.*

## Lab Architecture & Tools

---

- **SIEM/EDR:** Wazuh (manager & indexer)
- **Host Machine:** Windows 11 (16GB RAM)
- **Virtualization:** Oracle VirtualBox
- **Endpoints:** *

```python
- 1x Ubuntu Server (Wazuh Manager)
- 1x Windows 10 (Victim / Wazuh Agent)
- 1x Kali Linux (Attacker
```

![ARCHI.png](attachment:7556333f-8351-488a-b7fb-a7a98b3d8377:ARCHI.png)

lets Dive into configuring the Wazuh environment. Follow my steps
