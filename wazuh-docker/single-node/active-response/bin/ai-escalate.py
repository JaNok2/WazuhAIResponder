#!/usr/bin/env python3

import sys
import json
import subprocess

try:
    event = json.loads(sys.stdin.read())
except json.JSONDecodeError as e:
    sys.exit(f"Invalid JSON from Wazuh: {e}")

alert = event["parameters"]["alert"]
msg = alert.get("full_log") or alert.get("log", "") or json.dumps(alert)

prompt = (
    "Answer yes or no: is this event critical and needs escalation?\n"
    f"{msg}"
)

try:
    response = subprocess.check_output([
        "curl", "-s", "-X", "POST",
        "http://host.docker.internal:11434/api/generate",
        "-d", json.dumps({
            "model": "mistral:latest",
            "prompt": prompt,
            "stream": False
        })
    ])
    data = json.loads(response)
    answer = data.get("response", "").strip().lower()

    if "yes" in answer:
        with open("/var/ossec/logs/active-responses.log", "a") as f:
            f.write("Escalate\n")
        print("Escalate")
except Exception as e:
    print(f"Error contacting Ollama: {e}")


