# UTILISATION
dans main.py,
l1 : current_map correspond à la map, qui parse un txt de votre choix
puis on applique une méthode de résolution au choix sur current map
Dans la boucle main, la grille résolu va s'appliquer

# Différences des algorithmes

Brute force simple : Dans chaque case vide, mettre un nombre aléatoire
- Efficacité : 9 ^ n_case_vides

Brute force advance : Un auto complete simple, puis un brute force avec les valeurs potentiel aléatoire des cases

Backtracking : simple backtracking, qui résout toute les grilles