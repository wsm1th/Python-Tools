# ACCOUNT TAKEOVER RUNBOOK
---

## Utilize this runbook when a suspected Account Takeover has taken place in Office365. The steps in place and information recorded in the flow of the initial investigation of suspicious activity will prove beneficial as the incident response process evolves. 
---

- Account Takeovers can quickly evolve into Business Email Compromises, which are defined by Microsoft as:
  > a social engineering attack, where the attacker looks to dupe the target into believing that they are interacting with a trusted entity. Once they have deceived their target, the attacker proceeds to coax them to share valuable information or process a payment.

- This runbook will specifically address Account Takeovers stemming from Adversary in the Middle (AitM) attacks. These attacks are becoming increasingly popular among attackers as they can essentially bypass MFA. AitM attacks typically follow a defined flow:

  1. Phishing email is delivered to an end user
  2. End user clicks the link contained within the email
  3. The traffic is routed from the end user THROUGH an adversary's proxy server to a LEGITIMATE Microsoft sign in page
  4. End user inputs credentials OR if the user has a valid session, the token is communicated to Microsoft, and authentication is achieved
  5. The traffic contianing the token is routed through the adversary's proxy server
  6. Adversary steals the token
  7. Token is replayed to achieve unauthorized authentication

- These actions can be identified through a variety of tools and techniques. Following identification, a swift response is necessary. Following the below steps can assist in the identification and remediation of a business email compromise

  1. Receive Alert
     - View initial IP - use an IP information enumeration service such as [IPInfo.io](https://ipinfo.io/), [VirusTotal](https://www.virustotal.com/gui/home/search), or [AbuseIPDB](https://www.abuseipdb.com/)
       - Who manages the netblock (the IP address's ASN)?
          - Are they a hosting provider? (ex. Hostinger, HostRoyale Technologies, Hyonix, etc.)
          - Do they provide VPN services? (ex. Datacamp, Limestone Networks, etc.)
          - Is it a Tor node/Tor exit? (Flokinet, Zwiebelfreunde, Telia Company, etc.)
          - Is it a private, consumer level ISP? (AT&T, Charter, Spectrum, Verizon, etc.)
        - Does the IP make sense in context?
          - Check user properties:
            - Location?
            - Department?
        - Is the user traveling?
          - Do they have a valid access request on file with the helpdesk?
  2. Begin response process
     - Move to the EntraId portal -> sign ins (select user with evidenced suspicious activity)
     - Locate sign in that generated original alert and record relevant details:
       - Location information?
       - Device information?
       - UserAgent in use?
       - Time of first sign in?
       - Applications Accessed?
     - Search for and record common indicators of suspicious activity:
       - International failed sign ins
       - Unusual IP geolocation
       - 