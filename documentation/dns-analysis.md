# DNS and Email Security Analysis

## Target Domain
example.com

Note: This is a reserved example domain used for learning and testing.

## 1. Nameserver (NS) Records

Command:
dig example.com NS

Findings:
- elliott.ns.cloudflare.com
- hera.ns.cloudflare.com

Observation:
The domain uses Cloudflare nameservers.

## 2. Mail Exchange (MX) Records

Command:
dig example.com MX

Finding:
- 0 .

Observation:
This is a Null MX record. The domain explicitly indicates
that it does not accept email.

## 3. SPF Records

Command:
dig example.com TXT

Finding:
- v=spf1 -all

Observation:
The SPF policy authorizes no sending sources.

## 4. DMARC Records

Command:
dig _dmarc.example.com TXT

Finding:
- v=DMARC1
- p=reject
- sp=reject
- adkim=s
- aspf=s

Observation:
The domain publishes a DMARC reject policy with strict
SPF and DKIM alignment.

## 5. Overall Assessment

The DNS records show that example.com uses Cloudflare
nameservers and has email-related protective policies.

The Null MX and SPF -all records indicate that the domain
is not configured to receive or authorize email sending.

This investigation was performed for educational purposes.
