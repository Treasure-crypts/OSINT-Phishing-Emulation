# MITRE ATT&CK Mapping

## Objective
To map the activities explored in the OSINT Footprinting
and Targeted Phishing Emulation project to the MITRE
ATT&CK Enterprise Framework.

## 1. Reconnaissance

### Technique: Gather Victim Network Information
ID: T1590

Description:
Collecting information about a target organization's
network and infrastructure.

Project Connection:
SpiderFoot and DNS investigation were used to explore
domain-related information.

### Sub-technique: DNS
ID: T1590.002

Description:
Gathering DNS information such as nameservers,
mail servers and DNS records.

Project Connection:
Used dig commands to investigate NS, MX, TXT and
DMARC records.

## 2. Technical Information Gathering

### Technique: Search Open Technical Databases
ID: T1596

Description:
Searching publicly accessible technical databases
for information about a target.

Project Connection:
Relevant to the broader OSINT reconnaissance stage.
No separate technical database investigation was
performed in this exercise.

## 3. Phishing Emulation

### Technique: Phishing
ID: T1566

Description:
Using electronically delivered social engineering
messages to target individuals or organizations.

Project Connection:
Created a fictional HR phishing email and examined
its suspicious indicators.

Note:
This was an offline simulation. No email was sent.

## Conclusion

The project demonstrates basic reconnaissance,
DNS investigation, phishing email analysis and
MITRE ATT&CK technique mapping.

The mapping describes relevant attacker behaviours
for educational purposes and does not claim that
real attacks were conducted.
