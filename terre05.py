#Créez un programme qui affiche le résultat et le reste d’une division entre deux nombres.

import sys

numerateur = sys.argv[1]
denominateur = sys.argv[2]

numerateur = int(numerateur)
denominateur = int(denominateur)
resultat = numerateur / denominateur
reste = numerateur % denominateur
resultat = str(resultat).split(".")

print("resultat:", resultat[0])
print("reste:", reste)

 