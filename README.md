# cyberplaybook-ai
LLM-powered tool that generates cybersecurity incident response playbooks from threat data.
# AI-Generated Cybersecurity Playbook
This project uses OpenAI’s GPT model to automatically generate incident response playbooks from real-world CVEs (Common Vulnerabilities and Exposures).
### How It Works
1. Parses CVE data from JSON
2. Extracts key fields like CVSS score, references, summary
3. Uses an LLM (GPT) to generate a readable playbook
4. Saves results as `.txt` files for each CVE
### Why It’s Impressive
- Integrates **OpenAI GPT-4** (via API)
- Automates **incident response documentation**
- Real-time CVE analysis pipeline
- Shows practical use of **LLMs in cybersecurity**
> Note: AI generation is disabled temporarily due to OpenAI API quota limits, but code and architecture are fully implemented.
### Example Output
Files are saved in the `playbooks/` folder like:
playbooks/
├── GHSA-5mxq-jrf7-jcwr.txt
├── GHSA-vc8x-jcfq-84g7.txt
└── GHSA-46j9-975h-6c59.txt
Each file includes:
- CVE ID and metadata
- Links to references
- AI-generated **"AI Analysis"** (disabled due to API quota)
### Tech Stack
- Python 3.11
- `openai` library
- `dotenv` for secure key handling
- GPT-4 (via OpenAI API)
### 🔐 Environment Setup
Create a `.env` file:
```env
OPENAI_API_KEY=your-api-key-here