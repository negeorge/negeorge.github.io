Nisha's Twilio Client App

Steps to Run
1. Run capgen.py file w/ input of Twilio account auth token

python capgen.py {authtoken}

Output will be Client App Token, something similar to:
eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJpc3MiOiAiQUM3NTU5YjA2ZGUyYjdiYzUzY2M4NjE2ZjI0OGRlNGI3MyIsICJzY29wZSI6ICJzY29wZTpjbGllbnQ6b3V0Z29pbmc_YXBwU2lkPUFQMjI4OTAxMGQ2MjA3YmNhOTE1ZTkzYTFjNTU4MjQxOWUmY2xpZW50TmFtZT1uaXNoYSBzY29wZTpjbGllbnQ6aW5jb21pbmc_Y2xpZW50TmFtZT1uaXNoYSIsICJleHAiOiAxNDQzNDY5OTQ0fQ.06Q3peAxAHwjEe3Hyyfs_h9blXFP_Evsxe2JU_OQo1M

Tokens last for 1hr by default

2. load negeorge.github.io page to load client browser dialer (replace with current client token)

http://negeorge.github.io/#eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJpc3MiOiAiQUM3NTU5YjA2ZGUyYjdiYzUzY2M4NjE2ZjI0OGRlNGI3MyIsICJzY29wZSI6ICJzY29wZTpjbGllbnQ6b3V0Z29pbmc_YXBwU2lkPUFQMjI4OTAxMGQ2MjA3YmNhOTE1ZTkzYTFjNTU4MjQxOWUiLCAiZXhwIjogMTQ0MzE0NzkyMX0.l1fpzBNHSaHTNsaPiQE2TJjuP-Hl_4WsYbftXxI3T0o

3. Make a call or receive a call! Switch between Chrome/Firefox if there are issues loading in the one or the other. 