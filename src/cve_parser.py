import requests
import json
from datetime import datetime

def fetch_recent_cves(limit=10):
    url = f"https://cve.circl.lu/api/last/{limit}"
    response = requests.get(url)   # ← this line must be indented exactly under the function
    if response.status_code != 200:
        raise Exception("Failed to fetch CVEs")

    cves = response.json()
    parsed_cves = []

    for cve in cves:
        parsed = {
            "id": cve.get("id"),
            "summary": cve.get("summary"),
            "cvss": cve.get("cvss"),
            "published": cve.get("Published"),
            "references": cve.get("references")
        }
        parsed_cves.append(parsed)

    return parsed_cves

def save_to_file(data, filename="data/cves.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    print("[*] Fetching recent CVEs...")
    cve_data = fetch_recent_cves(limit=10)
    save_to_file(cve_data)
    print("[+] Saved CVEs to data/cves.json")