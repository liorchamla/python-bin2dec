from utils import ask_binary, bin2dec

# Notre but est le suivant :
# 1. Demander à l'utilisateur d'entrer un nombre binaire (composé max de 8 bits)
binary = ask_binary();

# 2. Calculer l'équivalent en base 10 (décimal)
decimal = bin2dec(binary)

# 3. Afficher le résultat
print("Le résultat en décimal est : " + str(decimal));