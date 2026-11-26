# OSINT Investigation Report

## 1. Objective

To understand how Open-Source Intelligence (OSINT)
tools collect publicly available information about
a domain and its associated infrastructure.

## 2. Target

Domain: example.com

Note: example.com is a reserved example domain used
for educational and testing purposes.

## 3. Tools Used

- SpiderFoot
- Kali Linux
- dig
- DNS investigation commands

## 4. SpiderFoot Investigation

A passive OSINT scan was performed using SpiderFoot.

Scan Results:
- Total Elements: 124
- Unique Elements: 103
- Errors: 71

Observed information:
- Domain-related information
- Associated DNS information
- Nameserver information
- Related IP addresses

The scan also returned Cloudflare-related information.

## 5. DNS Findings

Nameservers:
- elliott.ns.cloudflare.com
- hera.ns.cloudflare.com

MX Record:
- 0 . (Null MX)

SPF Record:
- v=spf1 -all

DMARC Record:
- v=DMARC1
- p=reject
- sp=reject
- adkim=s
- aspf=s

## 6. Analysis

The DNS investigation identified Cloudflare nameservers.

The Null MX record indicates that the domain does not
accept email. The SPF record authorizes no email
sending sources.

The DMARC record publishes a reject policy with
strict SPF and DKIM alignment.

SpiderFoot also identified related infrastructure
information. These associations should not be treated
as proof of domain ownership or hosting relationships.

## 7. Limitations

- The target was a reserved example domain.
- Some SpiderFoot modules returned errors.
- The scan findings are limited to the available
  passive information.
- No real organization or employee information
  was investigated.

## 8. Conclusion

This investigation provided practical experience
with OSINT reconnaissance, SpiderFoot and DNS
record analysis.

The activity demonstrates basic information-gathering
and infrastructure-investigation techniques.
