# Email Phishing Indicator Analysis Report

## Objective
To identify suspicious indicators in a synthetic email
using a Python-based email header analyser.

## Tools Used
- Kali Linux
- Python 3
- Python email library

## Findings

### 1. Sender and Reply-To
The sender claims to represent ABC Technologies HR.
However, the Reply-To address belongs to a different domain.

Finding: Suspicious indicator detected.

### 2. Subject Analysis
Subject: Urgent: Employee Policy Update

The subject contains urgency-related language.

Finding: Urgency keyword detected.

### 3. Authentication Analysis
Authentication-Results header was unavailable.

Finding: Authentication status cannot be determined
from this synthetic email.

## Conclusion
The Python analyser identified two suspicious indicators:
- Sender and Reply-To mismatch.
- Urgency-related subject.

These indicators require further investigation and do
not independently confirm phishing.

## Safety
This was an offline simulation using fictional identities.
No emails were delivered and no credentials were collected.
