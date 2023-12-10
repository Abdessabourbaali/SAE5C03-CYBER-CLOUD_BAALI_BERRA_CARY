# SAE5C03-CYBER-CLOUD_BAALI_BERRA_CARY

## Synthèse

### Organisation et répartition des tâches qui ont été effectués au terme de cette SAE

Nous nous sommes divisé les tâches selon ce que nous préférions faire. Nous avons d'abord déployé un GOAD sur virtualbox en attendant de pouvoir le faire sur proxmox. Nous avons aussi fait une PoC de l'automatisation de l'installation pour qu'une fois que le proxmox est disponible on ai juste nos script ansible à lancer.

#### Paul

- Reconnaissance Infra avec BloodHound (VirtualBox)
- Attaque / exploitation de vulnérabilités (VirtualBox)
- Mise en place du SIEM / IDS (VirtualBox)
- Automatisation du déploiement des agents (Elastic / Wazuh) (VirtualBox)
- Mise en place de Chainsaw et Hayabusa (VirtualBox)
- Mise en place d'Elastic-Security (VirtualBox)
- Test du SIEM (VirtualBox)

#### Abdessabour

- Mise en place de l’Honeypot (VirtualBox)
- Mise en place du serveur de logs OpenWEC et configuration de la collecte des logs Windows (Virtualbox)
- Analyse des logs récupérer sur le serveur OpenWEC avec chainsaw (Virtualbox)
- Schéma Virtualbox
- Installation de Sysmon sur Windows (Virtualbox)
- Configuration de l’audit selon l’ANSSI (Virtualbox)

#### Théo

- Installation et configuration de l'environnement GOAD sur Proxmox
- Mise en place du SIEM / IDS (Proxmox)
- Automatisation du déploiement des agents (Elastic / Wazuh) (Proxmox)
- Schéma Proxmox
- Test du SIEM (Proxmox)

### Blocages pendant le projet

#### Paul

- 

#### Abdessabour

- Configuration d'OpenWEC sur l'environnement Virtualbox
- Difficulté dans la compréhension de l'authentification Kerberos entre Windows et Linux

#### Théo

- Difficulté dans l'automatisation de l'installation de GOAD sur Proxmox

### Ce que nous avons appris au terme de cette SAE

#### Paul

- 

#### Abdessabour

- Compréhension d'openwec et Kerberos
- Meilleur maîtrise d'Active Directory sur Windows (Domaines, arbres et forêts)

#### Théo

- Meilleur compréhension de l'utilité des SIEM (Wazuh et Elastic)

## Annexes

- [x] [GOAD Proxmox](CR/goad_proxmox.pdf)(Manuel)
- [x] [Accès VPN](CR/vpn.md) (Automatisé)
- [x] Suricata (Manuel)
- [x] [Sysmon](CR/sysmon.md) (Automatisé)
- [x] [Audit](CR/audit.md) (Automatisé)
- [x] [open-wec](CR/openwec.md) (Automatisé)
	- [x] [WEF](CR/wef.md) (Automatisé)
- [x] [Wazuh](CR/wazuh.md) (Automatisé)
	- [x] [Installation agent par groupe DC/Servers](CR/wazuh-agent.md) (Automatisé)
- [x] [Elastic (Automatisé)](CR/deploiement_elastic.md)
- [x] [Splunk (Manuel)](CR/install_splunk.md)
- [x] [Versioning Git](CR/git.md)
- [x] [Attaques](CR/Pentest_GOAD.md) (Manuel)
- [x] [Chainsaw/Hayabusa](CR/log-analyze.md)
