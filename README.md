Passive Enrichment Script 

**Author:** Eli Cheng  
**Built with:** Python 3, `requests`, `socket`, `csv`, `json`  
**Date:** 29 April 2025  

---

Purpose

This script performs **passive enrichment** on a list of domains or IP addresses by:
- Resolving domains to IPs
- Using the `ipinfo.io` API to gather metadata
- Saving the results as both `.json` and `.csv`

---

How to Use

1. Install dependencies

bash
pip install requests

2. Run the script
python enrich_targets.py

3. Output

enrichment_results.json — structured JSON output
enrichment_results.csv — tabular CSV for Excel or SIEM

Example Output 
[+] Enriching: 8.8.8.8
    ip: 8.8.8.8
    city: Mountain View
    region: California
    country: US
    org: AS15169 Google LLC

Notes 

IPs work directly.
Domains are first resolved to IPs.
All lookups use the free tier of ipinfo.io (rate limits may apply)
