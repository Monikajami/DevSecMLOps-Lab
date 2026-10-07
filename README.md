# DevSecMLOps Lab

This repository contains the DevSecMLOps experiments executed as part of the laboratory examination.

## Experiment 6: ML Pipeline Access Control

Implemented Role-Based Access Control (RBAC) for an ML pipeline using Python.

### Roles
- Data Engineer
- Data Scientist
- ML Engineer
- Admin
- Viewer

### Security Features
- Role-based permissions
- Authorization using decorators
- Access denial for unauthorized operations
- Audit logging

### Result
Authorized operations were allowed and unauthorized operations were denied.
All access decisions were recorded in the audit log.

---

## Experiment 8: Vulnerability Scanning

Implemented Static Application Security Testing (SAST) using Bandit.

### Vulnerabilities Detected
- Unsafe pickle deserialization
- Command injection through `shell=True`
- MD5 usage
- Hard-coded password

### Remediation
- Replaced pickle with JSON
- Removed `shell=True`
- Replaced MD5 with SHA-256
- Used environment variables for credentials

### Result

Initial scan:
- High: 2
- Medium: 1

After remediation:
- High: 0
- Medium: 0