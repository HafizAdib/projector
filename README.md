<<<<<<< HEAD
# 📂 Projector : Application Web de Gestion de Projets (NoSQL)

### 🎓 Projet d'École - Développement NoSQL
**Développé par : ABDOUL HALIM HAFIZ ADIB**

Ce projet a été réalisé dans le cadre d'un cursus informatique pour apprendre à manipuler les **bases de données non-relationnelles (NoSQL)** et les intégrer dans des applications web réelles.

---

## 🚀 Présentation du Projet
L'objectif de cette application est de fournir une interface simple et efficace pour gérer des projets et leurs tâches associées. Contrairement aux bases SQL classiques, ce projet utilise une structure de **documents flexibles** (JSON-like) pour stocker les données.

### Fonctionnalités principales :
*   **Gestion des Projets :** Création, modification, consultation et suppression de projets.
*   **Gestion des Tâches :** Ajout de tâches spécifiques à chaque projet avec :
    *   Nom de la tâche
    *   État d'avancement
    *   Niveau de priorité
    *   Date d'échéance
*   **Stockage Cloud :** Connexion distante à un cluster MongoDB Atlas.

---

## 🛠️ Stack Technique
*   **Langage :** [Python 3.9+](https://www.python.org)
*   **Framework Web :** [Flask](https://flask.palletsprojects.com)
*   **Base de données :** [MongoDB Atlas](https://www.mongodb.com) (NoSQL)
*   **Bibliothèques Python :** 
    *   `Flask-PyMongo` (Lien entre Flask et MongoDB)
    *   `dnspython` (Pour la résolution DNS du cluster Cloud)
    *   `bson` (Pour la gestion des identifiants uniques MongoDB)

---

## 📦 Installation et Configuration Locale

### 1. Pré-requis
Avoir Python installé sur votre machine.

### 2. Installation des dépendances
Ouvrez votre terminal et exécutez la commande suivante :
```bash
pip install Flask Flask-PyMongo dnspython gunicorn
=======
# projector
>>>>>>> de513e6e16e5a94f42644e56a35a767d3d02566b
