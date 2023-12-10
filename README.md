# SAE5C03-CYBER-CLOUD_BAALI_BERRA_CARY

## Synthèse

### Organisation et répartition des tâches qui ont été effectués au terme de cette SAE

L'équipe s'est organisée de manière à tirer parti des préférences individuelles et des compétences de chaque membre. Voici un résumé de l'organisation et de la répartition des tâches :

### Organisation de l'équipe

- Les membres se sont répartis les tâches en fonction de leurs préférences et compétences.
- La première étape consistait à déployer un GOAD sur VirtualBox en attendant de pouvoir le faire sur Proxmox.

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

- Effacement du SIEM car le script n'était pas automatique

#### Abdessabour

- Difficulté dans la configuration d'OpenWEC sur l'environnement Virtualbox
- Difficulté dans la compréhension de l'authentification Kerberos entre Windows et Linux

#### Théo

- Difficulté dans l'automatisation de l'installation de GOAD sur Proxmox

### Ce que nous avons appris au terme de cette

#### Paul

- Découverte du fonctionnement de Sharphound

#### Abdessabour

- Meilleur compréhension d'openwec et Kerberos
- Meilleur maîtrise d'Active Directory sur Windows (Domaines, arbres et forêts)

#### Théo

- Meilleur compréhension de l'utilité des SIEM (Wazuh et Elastic)

## Conclusion

Au terme de cette SAE, notre équipe a réussi à mettre en place un environnement propice à la détection d'alerte avec notamment la mise en place des SIEM, d'un serveur de log centralisé. Par manque de temps notre approche collaborative, basée sur la répartition des tâches en fonction des compétences et des préférences individuelles, n'a pas été parfaite.

Nous avons rencontré des difficultés liées à la limitation de la mémoire de certains PC, ce qui a entraîné des problèmes de performance et des bugs. Pour assurer la garantie de fonctionnement, nous avons pris la décision jouer la carte de rester dans un environnement virtuel sur Virtualbos, évitant ainsi de partir dans l'inconnu.

La plupart des difficultés, y compris celles liées à l'automatisation, ont été identifiées et analysées pendant la période de préparation. Bien que ces défis aient été abordés de manière proactive, certains problèmes logistiques ont persisté, mettant en évidence l'importance de la planification minutieuse même en phase préparatoire.

Malgré la mise en place des outils demandés nous avons identifié un axe d'amélioration important qui est l'automatisation des différents outils déployés. Les blocages rencontrés ont ralenti le processus d'automatisation, ce qui représente une zone clé où nous devrons concentrer nos efforts futurs.

Pour finir, même si nous avons rencontrés quelques difficultés, chaque membre a acquis des compétences et des connaissances précieuses. Ces apprentissages serviront de base solide pour notre développement futur.

## Annexes

- [GOAD sur Proxmox](Compte-Rendu/goad_proxmox.pdf) (Manuel)
- [GOAD sur Virtualbox](Compte-Rendu/goad_proxmox.pdf) (Automatisé)
- [Configuration d'OpenWEC et la centralisation des logs](Compte-Rendu/manual_install_openwec.md) (Manuel)
- [Installation de Sysmon](Compte-Rendu/manual_install_sysmon.md) (Manuel)
- [Configuration des règles d'audit](Compte-Rendu/manual_install_openwec.md) (Manuel)
- [Wazuh](Compte-Rendu/wazuh.pdf) (Automatisé)
- [Elastic](Compte-Rendu/deploiement_elastic.pdf) (Automatisé)
- [Attaques](Compte-Rendu/Pentest_GOAD.md) (Manuel)
- [Mise en place de Chainsaw/Hayabusa](Compte-Rendu/log-analyze.pdf) (Manuel)
