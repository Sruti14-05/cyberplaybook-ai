import os
import json
import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_playbook(cve):
    base_summary = f"""CVE ID: {cve['id']}
Summary: {cve['summary']}
CVSS Score: {cve['cvss']}
Published: {cve['published']}
References:
{chr(10).join(ref['url'] for ref in cve['references'])}
"""

    prompt = f"""
You are a cybersecurity expert. Read the following CVE information and generate a human-readable incident response playbook that includes:

1. Impact Assessment
2. Detection Strategy
3. Mitigation Steps
4. Recovery Plan

CVE Information:
{base_summary}
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or gpt-4 if your key supports it
            messages=[
                {"role": "system", "content": "You are a helpful cybersecurity assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=800,
        )

        ai_analysis = response['choices'][0]['message']['content']
    except Exception as e:
        ai_analysis = f"[!] Error calling OpenAI API: {e}"

    return f"{base_summary}\n\nAI Analysis:\n{ai_analysis}"
def main():
    os.makedirs("playbooks", exist_ok=True)

    with open("data/cves.json", "r", encoding="utf-8") as f:
        cves = json.load(f)

    for cve in cves:
        if not cve.get("id"):
            continue  # skip if ID is missing

        playbook = generate_playbook(cve)
        filename = f"playbooks/{cve['id'].replace('/', '-')}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(playbook)
        print(f"[+] Playbook generated: {filename}")
if __name__ == "__main__":
    main()