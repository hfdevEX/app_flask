# import os
# import json
# import feedparser
# from datetime import datetime
# from flask import Flask, render_template, flash, redirect, url_for, request
# import requests
# from flask_sqlalchemy import SQLAlchemy
# from flask_swagger_ui import get_swaggerui_blueprint


# app = Flask(__name__)

# # Configuration de l'URI de la base de données et désactivation du suivi des modifications
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fluxrss.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['UPLOAD_FOLDER'] = 'uploads'
# #Oui je sais...
# app.secret_key = '07671C8CA4CC9D8A660B9DDD23F0D75C7260ED385A10267074569F1C452B8441'




# swaggerui_blueprint = get_swaggerui_blueprint(
#     SWAGGER_URL,
#     API_URL,
#     config={
#         'app_name': "app_flask"
#     }
# )


# db = SQLAlchemy(app)


# class RssFeed(db.Model):
#     """
# Class RssFeed hérite de db.Model pour modeler un flux RSS.

# Attributs:
#     id (int): id pour chaque flux RSS (primary_key).
#     name (str): Nom du flux RSS, ne peut pas être nul.
#     url (str): URL du flux RSS, ne peut pas être nul.
#     image (str): URL de l'image associée au flux RSS (optionnel).

#         -aucune relation



# @app.route('/show/<int:id>', methods=['GET'])
# def show(id):
#     """
#     Fonction show() pour afficher un flux RSS spécifique et ses articles.

#     Args:
#         id (int): Identifiant du flux RSS.
#     """


# @app.route('/delete/<int:id>')
# def delete(id):

#     """
#         Fonction delete() pour supprimer un flux RSS.

#         Args:
#             id (int): Identifiant du flux RSS à supprimer.
# """

