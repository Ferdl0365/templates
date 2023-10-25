## How to name files
'function'_server.py
'function'_server.service

## Where to put files

server.py: .../usr/bin/python /programs/xmlrpc_server/remote_functions/server.py

server.service: .../lib/systemd/system/server.service

### How to start service remote
4. Terminal öffnen und folgenden Befehl eingeben  ```shh root@<ROBOTER_IP>```
1. Service neu starten ```systemctl restart server.service```
2. Trick: STRG+R in Terminal drücken (öffnet die Kommandosuche) und "restart" eingeben (der richtige Befehl sollte erscheinen)
3. Service Status überprüfen: ```systemctl status server.service```