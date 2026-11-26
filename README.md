# OSINT Footprinting to Targeted Phishing Emulation

## Project Overview

This project demonstrates how Open-Source Intelligence (OSINT), DNS investigation, email security analysis, and phishing indicators can be studied through a controlled cybersecurity simulation.

The project follows a simulated organizational scenario using fictional identities and synthetic email data to understand how attackers may gather information and how security analysts can identify suspicious email characteristics.

## Objectives

- Understand OSINT footprinting techniques.
- Explore domain and DNS information.
- Examine email security configurations such as SPF and DMARC.
- Create a synthetic phishing email for offline analysis.
- Develop a Python-based email header analysis script.
- Identify suspicious email indicators.
- Map relevant activities to MITRE ATT&CK.

## Tools and Technologies

| Tool         | Purpose                           |
| ------------ | --------------------------------- |
| Kali Linux   | Cybersecurity testing environment |
| SpiderFoot   | OSINT information gathering       |
| DIG          | DNS record investigation          |
| Python 3     | Email header analysis             |
| MITRE ATT&CK | Threat technique mapping          |

## Project Workflow

1. **OSINT Footprinting:** Used SpiderFoot to explore domain-related information.
2. **DNS Investigation:** Examined NS, MX, TXT, SPF, and DMARC records.
3. **Phishing Simulation:** Created a synthetic HR-themed email for offline analysis.
4. **Email Header Analysis:** Developed a Python script to identify suspicious email indicators.
5. **MITRE ATT&CK Mapping:** Related selected project activities to relevant ATT&CK techniques.
6. **Documentation:** Recorded findings, observations, and screenshots.

## Key Findings

- Identified domain nameserver information using DNS queries.
- Observed a Null MX record for the test domain.
- Examined SPF configuration (`v=spf1 -all`).
- Examined DMARC policy (`p=reject`).
- Identified a Reply-To mismatch in the synthetic email.
- Detected urgency-related language in the email subject.
- Observed that Authentication-Results was unavailable in the offline email sample.

**Note:** `example.com` is a reserved example domain used for testing. The findings are not an assessment of a real organization.

## Python Email Analysis

The project includes a Python script that parses a synthetic email and checks for selected suspicious indicators.

Run the script using:

```bash
python3 scripts/header_analyzer.py
```

## Project Structure

```text
OSINT-Phishing-Project/
│
├── documentation/
│   ├── project-overview.md
│   ├── dns-analysis.md
│   └── mitre-mapping.md
│
├── scripts/
│   └── header_analyzer.py
│
├── email-samples/
│   └── sample.eml
│
├── screenshots/
│   ├── 01_spiderfoot_dashboard.png
│   ├── 02_spiderfoot_results.png
│   ├── 03_dns_nameservers.png
│   ├── 04_mx_record.png
│   ├── 05_spf_record.png
│   ├── 06_dmarc_record.png
│   ├── 07_email_analysis.png
│   └── 08_mitre_mapping.png
│
└── reports/
    ├── osint-investigation-report.md
    ├── email-analysis-report.md
    └── phishing-simulation.md
```

## Ethical Considerations

- Used fictional organizational identities.
- Used a reserved example domain for DNS testing.
- Created synthetic email samples.
- No phishing emails were delivered to real users.
- No real credentials were collected.
- Activities were performed for educational purposes.

## Learning Outcomes

This project provided practical exposure to OSINT tools, DNS investigation, email security concepts, Python-based email analysis, and basic threat intelligence mapping.

## Disclaimer

This project is intended strictly for educational and defensive cybersecurity learning. All simulations were conducted in a controlled environment using synthetic data.

