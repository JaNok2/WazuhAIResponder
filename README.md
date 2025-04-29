# 🤖 Wazuh + Ollama AI Alert Escalation
This project combines [Wazuh](https://github.com/wazuh/wazuh-docker) and [Ollama](https://ollama.com) AI to automatically escalate alerts based on local LLM (Mistral 7B).


## 📌 About the Project
- ✅ Based on [`wazuh-docker`](https://github.com/wazuh/wazuh-docker) GitHub repository (single-node setup).
- ✅ Custom `active-response` script using Ollama AI.
- ✅ Alerts analyzed and escalated automatically via a local language model.
- ✅ Integration visible via Wazuh Dashboard UI.


## ⚙️ Requirements
- Docker + Docker Compose
- Python 3 inside the Wazuh container
- [Ollama](https://ollama.com) installed locally (running on port `11434`)
- Pulled model: `mistral:7b-instruct`
- Wazuh Docker setup (single-node)
