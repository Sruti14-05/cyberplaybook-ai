# cyberplaybook-ai
LLM-powered tool that generates cybersecurity incident response playbooks from threat data.
# AI-Generated Cybersecurity Playbook
This project uses OpenAI’s GPT model to automatically generate incident response playbooks from real-world CVEs (Common Vulnerabilities and Exposures). This project calls GPT to analyze CVEs, but AI output is disabled due to API quota.
## Features
- Parses CVE vulnerability data from JSON
- Automatically generates a `.txt` playbook for each CVE
- Adds GPT-powered **AI Analysis** to each file
- Clean `.env` setup to keep API keys secure
## Folder Structure
- data/ # CVE input JSON
─ playbooks/ # Output: AI-enhanced playbooks
─ src/ # Python source code
─ .env # (Your OpenAI API key - ignored by Git)
─ README.md # This file
## Setup
1. Clone this repo  
   `git clone https://github.com/Sruti14-05/cyberplaybook-ai.git`
2. Install requirements  
   `pip install -r requirements.txt`
3. Add your OpenAI API key  
   Create a `.env` file and write:
OPENAI_API_KEY=your-key-here
4. Run the generator  
`python src/generator.py`
### Example Output
Files are saved in the `playbooks/` folder like:
playbooks/
- GHSA-5mxq-jrf7-jcwr.txt
─ GHSA-vc8x-jcfq-84g7.txt
─ GHSA-46j9-975h-6c59.txt
Each file includes:
- CVE ID and metadata
- Links to references
- AI-generated **"AI Analysis"** (disabled due to API quota)
### Tech Stack
- Python 3.11
- `openai` library
- `dotenv` for secure key handling
- GPT-4 (via OpenAI API)
