from Genome import genome
from translate import translation
import json

corona = genome()
corona_1ab = {} #dictionary for the first protein "orf1ab"
corona_all_proteins = {} #dictionary for the entire corona

corona_1ab['orf1a'] = translation(corona[265:13468].upper())
corona_1ab['orf1b'] = translation(corona[13468-1:21555-3].upper()) # -3 because the last codon is "%" 

corona_all_proteins['orf1ab'] = corona_1ab['orf1a'] + corona_1ab['orf1b']
corona_all_proteins['S'] = translation(corona[21563-1:25384-3].upper())
corona_all_proteins['orf3a'] = translation(corona[25393-1:26220-3].upper())
corona_all_proteins['E'] = translation(corona[26245-1:26472-3].upper())
corona_all_proteins['M'] = translation(corona[26523-1:27191-3].upper())
corona_all_proteins['orf6'] = translation(corona[27202-1:27387-3].upper())
corona_all_proteins['orf7a'] = translation(corona[27394-1:27759-3].upper())
corona_all_proteins['orf8'] = translation(corona[27894-1:28259-3].upper())
corona_all_proteins['N'] = translation(corona[28274-1:29533-3].upper())
corona_all_proteins['orf10'] = translation(corona[29558-1:29674-3].upper())

#print(corona_all_proteins)

f = json.dumps(corona_all_proteins)
