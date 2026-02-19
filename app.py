### CETTE APPLICTION WEB A ETE 
### DEVELOPPE PAR --- ABDOUL HALIM HAFIZ ADIB ---
### LORS D'UN PROJET D'ECOLE SUR LES NoSQL
### DANS D'APPRENDRE A UTILISER LES BASES DE DONNEES NON RELATIONNELLES
### (NoSQL) POUR DEVELOPPER DES APPLICATIONS.

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = "gest_projets_secret"

# Config MongoDB : Pour se connecter à la base de données MongoDB
# app.config["MONGO_URI"] = "mongodb://localhost:27017/gest_projets" # En loal
app.config["MONGO_URI"] = "mongodb+srv://hafiz_adib:hafiz_adib@cluster0.iadzdmo.mongodb.net/gest_projets?appName=Cluster0" # En ligne
mongo = PyMongo(app)

# --- Routes ---

# --- Gestion du projet ---
# /Accueil
@app.route("/")
def index():
    projets = list(mongo.db.projets.find())
    return render_template("index.html", projets=projets)

# /Ajouter un projet
@app.route("/project/add", methods=["GET", "POST"])
def add_project():
    if request.method == "POST":
        nom = request.form.get("nom")
        description = request.form.get("description")
        mongo.db.projets.insert_one({
            "nom": nom,
            "description": description,
            "taches": []
        })
        flash("Projet ajouté avec succès !", "success")
        return redirect(url_for("index"))
    return render_template("add_project.html")

# /Afficher les details d'un projet
@app.route("/project/<id>")
def project_detail(id):
    projet = mongo.db.projets.find_one({"_id": ObjectId(id)})
    return render_template("project_detail.html", projet=projet)

# Modifier un projet
@app.route("/project/edit/<id>", methods=["GET", "POST"])
def edit_project(id):
    projet = mongo.db.projets.find_one({"_id": ObjectId(id)})
    if request.method == "POST":
        nom = request.form.get("nom")
        description = request.form.get("description")
        mongo.db.projets.update_one(
            {"_id": ObjectId(id)},
            {"$set": {"nom": nom, "description": description}}
        )
        flash("Projet modifié avec succès !", "success")
        return redirect(url_for("index"))
    return render_template("edit_project.html", projet=projet)

# Supprimer un projet
@app.route("/project/delete/<id>")
def delete_project(id):
    mongo.db.projets.delete_one({"_id": ObjectId(id)})
    flash("Projet supprimé avec succès !", "danger")
    return redirect(url_for("index"))

# --- Gestion des tâches ---
# Ajout d'une tâche
@app.route("/project/<project_id>/task/add", methods=["POST"])
def add_task(project_id):
    nom = request.form.get("nom")
    etat = request.form.get("etat")
    priorite = request.form.get("priorite")
    echeance = request.form.get("echeance")  # YYYY-MM-DD
    mongo.db.projets.update_one(
        {"_id": ObjectId(project_id)},
        {"$push": {"taches": {
            "nom": nom,
            "etat": etat,
            "priorite": priorite,
            "echeance": echeance
        }}}
    )
    flash("Tâche ajoutée !", "success")
    return redirect(url_for("project_detail", id=project_id))


# Modifier une tache
@app.route("/project/<project_id>/task/update/<int:task_index>", methods=["POST"])
def update_task(project_id, task_index):
    nom = request.form.get("nom")
    etat = request.form.get("etat")
    priorite = request.form.get("priorite")
    echeance = request.form.get("echeance")
    projet = mongo.db.projets.find_one({"_id": ObjectId(project_id)})
    projet["taches"][task_index]["nom"] = nom
    projet["taches"][task_index]["etat"] = etat
    projet["taches"][task_index]["priorite"] = priorite
    projet["taches"][task_index]["echeance"] = echeance
    mongo.db.projets.update_one(
        {"_id": ObjectId(project_id)},
        {"$set": {"taches": projet["taches"]}}
    )
    flash("Tâche mise à jour !", "success")
    return redirect(url_for("project_detail", id=project_id))

# Supprimer une tache
@app.route("/project/<project_id>/task/delete/<int:task_index>")
def delete_task(project_id, task_index):
    projet = mongo.db.projets.find_one({"_id": ObjectId(project_id)})
    projet["taches"].pop(task_index)
    mongo.db.projets.update_one(
        {"_id": ObjectId(project_id)},
        {"$set": {"taches": projet["taches"]}}
    )
    flash("Tâche supprimée !", "danger")
    return redirect(url_for("project_detail", id=project_id))


# Lancer l'application
if __name__ == "__main__":
    # app.run(debug=True)
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
