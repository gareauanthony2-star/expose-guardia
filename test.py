test.py

from collections import Counter

import re

 

# --- Saisie du texte ---

texte = input("Entrez votre texte : ")

 

# --- Nettoyage et préparation ---

# On considère qu'une phrase se termine par . ! ou ?

phrases = re.split(r'[.!?]+', texte)

phrases = [p.strip() for p in phrases if p.strip()]

 

# On enlève la ponctuation pour compter les mots

mots = re.findall(r'\b\w+\b', texte.lower())

 

# --- Comptages ---

nb_mots = len(mots)

nb_lettres = sum(c.isalpha() for c in texte)

nb_phrases = len(phrases)

 

# --- Comptage des mots fréquents ---

compteur_mots = Counter(mots)

mots_frequents = compteur_mots.most_common(5)

 

# --- Affichage des résultats ---

print("\n--- Résultats de l'analyse ---")

print(f"Nombre de mots     : {nb_mots}")

print(f"Nombre de lettres  : {nb_lettres}")

print(f"Nombre de phrases  : {nb_phrases}")

print("\nLes 5 mots les plus fréquents :")

for mot, freq in mots_frequents:

    print(f"  {mot} : {freq}")