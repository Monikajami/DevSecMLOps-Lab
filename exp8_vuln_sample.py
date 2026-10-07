import pickle
import subprocess
import hashlib

def load_model(path):
    # VULNERABLE: pickle.load on untrusted data
    with open(path, "rb") as f:
        return pickle.load(f)

def run_cmd(user_input):
    # VULNERABLE: shell=True with user input
    return subprocess.call(user_input, shell=True)

def checksum(data):
    # VULNERABLE: MD5
    return hashlib.md5(data.encode()).hexdigest()

# VULNERABLE: hard-coded secret
DB_PASSWORD = "admin123"