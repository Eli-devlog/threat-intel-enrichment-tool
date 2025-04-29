# Passive Enrichment Script v1.0
# Author: Eli Cheng
# Purpose: Enrich a list of domains/IPs with basic metadata using public APIs

import requests
import json

# 1. Hardcoded sample input list
targets = [
    '8.8.8.8',          
    'google.com',       
    '208.67.222.222',   
    'facebook.com',     
    'github.com'        
]

# 2. Function to enrich a single domain or IP
import socket

def enrich_target(target):
    # If target is a domain, resolve to IP first
    try:
        resolved_ip = socket.gethostbyname(target)
    except socket.gaierror:
        return {'error': f'Unable to resolve domain: {target}'}
    
    url = f"https://ipinfo.io/{resolved_ip}/json"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}

# 3. Loop through all targets and call enrichment
def main():
    print("=== Passive Enrichment Report ===\n")
    all_results = {}  # Store results by target name

    for target in targets:
        print(f"[+] Enriching: {target}")
        data = enrich_target(target)
        all_results[target] = data  # Save result in dictionary

        # Pretty print to terminal
        for key, value in data.items():
            print(f"    {key}: {value}")
        print("-" * 40)

    # Save to JSON file
    with open("enrichment_results.json", "w") as f:
        json.dump(all_results, f, indent=4)
    print("\n[+] All results saved to enrichment_results.json")

# 4. Standard Python execution guard
if __name__ == "__main__":
    main()

    import csv  # Add this at the top with imports

# ...

    # Save to CSV
    with open("enrichment_results.csv", "w", newline='') as csvfile:
        fieldnames = set()  # Gather all possible fields
        for data in all_results.values():
            fieldnames.update(data.keys())

        fieldnames = list(fieldnames)

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for target, data in all_results.items():
            row = {'target': target}
            row.update(data)
            writer.writerow(row)

    print("[+] All results saved to enrichment_results.csv")