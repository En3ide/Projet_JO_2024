import re

chaine = "Ceci est [un exemple] de [chaine] avec des [parties] entre crochets."
chaine_sans_crochets = re.sub(r'\[.*?\]', '', chaine)

print(chaine_sans_crochets)