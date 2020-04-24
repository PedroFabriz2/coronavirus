# 🦇 Coronavirus
###### Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome
**Coronaviruses (CoVs) are enveloped, positive-sense, single-stranded RNA viruses that belong to the subfamily Coronavirinae, family Coronavirdiae, order Nidovirales.**

## :crystal_ball: thinking...
- [x] How corona interact with human cells
- [x] find genetic code of corona
- [x] what can i do with python?


### what i know

* [Transcription](https://en.wikipedia.org/wiki/Transcription_(biology)) is when RNA is created based on DNA
* [Reverse Transcriptase](https://en.wikipedia.org/wiki/Reverse_transcriptase) is when DNA is created based on RNA. That's what RNA based virus do when entry our cells
* Translation is the production of amino acids based on three nuclebases(codons = 3 * nucleobase)
* Genetic Code tells us how to decode RNA.
*  Reading Frames for RNA (3 existing reading frames) is the way that translate happens: when Start and Finish the translate
* Usually Start Codon:  AUG
* Usually Stop Codon:  UAG UGA UAA
* 2019-nCov is a temporary nomenclature and the oficial name is  [Sars-CoV-2(virus from family Coronaviridae)](https://en.wikipedia.org/wiki/Severe_acute_respiratory_syndrome_coronavirus_2).

## :wrench: Steps 
 - [x] create function that returns dictionary with decoding
 - [x] create function that translate RNA chain.
 - [x] translate all corona RNA and find all the proteins
 - [x] discover what is the function of each protein
 - [x] discover orf3a,6,7a,8,10 functions
 - [ ] can we unfold the corona?
 - [x] transform the dict into json file
 
## :computer: about the code
* in corona folder, [corona.ipynb](corona/corona.ipynb) is a jupyter notebook where you can find the first code that i made

* in scripts folder, [Genome.py](scripts/Genome.py) contains the genome of coronavirus import from [ncbi](https://www.ncbi.nlm.nih.gov/nuccore/MN908947).

* the translate function can be found in [translate.py](scripts/translate.py) and it was used in [proteins_corona.py](scripts/proteins_corona.py) to create a dictionary with all the 9 proteins(spike, orf1ab, N, E, M and some others ORF's).

* [proteins.pdf](proteins.pdf) contains more information about coronavirus proteins.
 
## :pencil2: Proteins - function
* Orf1ab polyprotein- _Viral protein involved in the activation of host autophagy. Autophagy is a major intracellular pathway in the delivery of cytoplasmic material to lysosomes for degradation. It is also essential for the removal of pathogenic protein aggregates from the cell during infection. Although autophagy is clearly important for antiviral immune response, it can also be activated by viruses and serves as platform for viral replication. Some viruses such as poliovirus, use the autophagic pathway as a nonlytic mechanism for viral release._

* Spike glycoprotein [S] - _Spike proteins assemble into trimers on the virion surface to form the distinctive “corona”, or crown-like appearance. Spike mediates fusion of the virion and cellular membranes by acting as a class I viral fusion protein. Under the current model, the protein has at least three conformational states: pre-fusion native state, pre-hairpin intermediate state, and post-fusion hairpin state. During viral and target cell membrane fusion, the coiled coil regions (heptad repeats) assume a trimer-of-hairpins structure, positioning the fusion peptide in close proximity to the C-terminal region of the ectodomain. The formation of this structure appears to drive apposition and subsequent fusion of viral and target cell membranes._

* o SARS-CoV-2 tem quatro proteínas estruturais, conhecidas como proteínas S (spike), E (envelope), M (membrana) e N (nucleocapsídeo). A proteína N contém o genoma ARN e em conjunto as proteínas S, E e M criam o envelope viral.

* E(structural protein) - _envelope_

* M(structural protein) - _membrane_

* N(structural protein) - _nucleocapsid_


Proteins | Function 
------------ | -------------
orf1ab | activation of host autophagy
S | fusion of the virion and cellular membranes
E, M, N | create the virus envelope
orf1a | viral genome replication && viral protein processing


Fonts: https://www.uniprot.org/uniprot/Q0ZJN1

## :clock10: Look later
ACE2 receptor protein 
S-Protein - spike protein

## :mortar_board: New knowledge
#### ORF
* In molecular genetics, an open reading frame (ORF) is the part of a reading frame that has the ability to be translated.
* In eukaryotic genes with multiple [exons](https://en.wikipedia.org/wiki/Exon), [introns](https://en.wikipedia.org/wiki/Intron) are removed and exons are then joined together after transcription to yield the final mRNA for protein translation.
* One common use of open reading frames (ORFs) is as one piece of evidence to assist in [gene prediction](https://en.wikipedia.org/wiki/Gene_prediction).
* Long ORFs are often used, along with other evidence, to initially identify candidate protein-coding regions or functional RNA-coding regions in a DNA sequence.
* The presence of an ORF does not necessarily mean that the region is always translated.
* By itself even a long open reading frame is not conclusive evidence for the presence of a [gene](https://en.wikipedia.org/wiki/Gene).

## Important Links and Articles

about genetic code :arrow_forward: https://djalmasantos.wordpress.com/2010/11/15/codigo-genetico/
genome Sars-CoV-2 :arrow_forward: https://www.ncbi.nlm.nih.gov/nuccore/MN908947

https://pt.khanacademy.org/science/biology/gene-expression-central-dogma/central-dogma-transcription/a/the-genetic-code-discovery-and-properties
https://www.khanacademy.org/science/biology/gene-expression-central-dogma/translation-polypeptides/a/translation-overview
https://www.sciencedirect.com/science/article/pii/S0092867420302622
https://en.wikipedia.org/wiki/Open_reading_frame
