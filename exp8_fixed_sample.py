import json
import subprocess
import hashlib
import os

def load_model(path):
    # FIXED: load from JSON instead of pickle
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def run_cmd(args_list):
    # FIXED: do not use shell=True
    return subprocess.call(args_list, shell=False)

def checksum(data):
    # FIXED: use SHA-256 instead of MD5
    return hashlib.sha256(data.encode()).hexdigest()

# FIXED: read secret from environment
DB_PASSWORD = os.environ.get("DB_PASSWORD")