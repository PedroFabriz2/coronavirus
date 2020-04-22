import re


table = """Ala / A GCU, GCC, GCA, GCG
Ile / I AUU, AUC, AUA
Arg / R CGU, CGC, CGA, CGG; AGA, AGG
Leu / L CUU, CUC, CUA, CUG; UUA, UUG
Asn / N AAU, AAC
Lys / K AAA, AAG
Asp / D GAU, GAC
Met / M AUG
Phe / F UUU, UUC
Cys / C UGU, UGC
Pro / P CCU, CCC, CCA, CCG
Gln / Q CAA, CAG
Ser / S UCU, UCC, UCA, UCG; AGU, AGC
Glu / E GAA, GAG
Thr / T ACU, ACC, ACA, ACG
Trp / W UGG
Gly / G GGU, GGC, GGA, GGG
Tyr / Y UAU, UAC
His / H CAU, CAC
Val / V GUU, GUC, GUA, GUG
STOP    UAA, UGA, UAG
""".strip().split("\n")

#steps that result in a dict of codon table RNA
dec = {}
for z in table:
    first = z[:len('Thr / T')].strip() # strip() just cut the empty spaces in the start and in the end
    second = z[len('Thr / T'):].strip() # strip() just cut the empty spaces in the start and in the end
    
    if "/"in first:
        first = first.split("/")[-1].strip() # [-1] means that we only want the one letter part of the first list
    
    second = second.replace(";", "").replace(",", "").split(" ")# split(" ") breaks in the empy spaces for each iteration
    first = first.replace("STOP", "%")
    
    for w in second:
        dec[w] = first # each codon receives a letter of the first list...resulting in a dict

aminoacids_chain = []
def translation(x):
    # break the string but leave it with empty strings
    aminoacids_chain = re.split("(\S{3})", x)
    
    # remove empty string
    chain = list(filter(None, aminoacids_chain))
    aa=[]
    for q in chain:
        aa.append(dec[q])
    aa = ''.join(aa)
    return aa

