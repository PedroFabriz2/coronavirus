# Coronavirus
###### Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome
**Coronaviruses (CoVs) are enveloped, positive-sense, single-stranded RNA viruses that belong to the subfamily Coronavirinae, family Coronavirdiae, order Nidovirales.**

## :crystal_ball: thinking...
- [x] How corona interact with human cells
- [x] find genetic code of corona
- [x] what can i do with python?


### what i know

* Transcription is when RNA is created based on DNA
* Reverse Transcription is when DNA is created based on RNA. That's what RNA based virus do when entry our cells
* Translation is the production of amino acids based on three nuclebases(codons = 3 * nucleobase)
* Genetic Code tells us how to decode RNA.
*  Reading Frames for RNA (3 existing reading frames) is the way that translate happens: when Start and Finish the translate
* Usually Start Codon:  AUG
* Usually Stop Codon:  UAG UGA UAA
* 2019-nCov is a temporary nomenclature and the oficial name is  Sars-CoV-2(virus from family Coronaviridae.

## :wrench: Steps 
 - [x] create function that returns dictionary with decoding
 - [x] create function that translate RNA chain.
 - [x] translate all corona RNA and find all the proteins
 - [x] discover what is the function of each protein
 - [ ] discover orf3a,6,7a,8,10 functions
 - [ ] can we unfold the corona?
 - [ ] transform the dict into json file
 
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


Fonts: https://www.uniprot.org/uniprot/Q0ZJN1

## :clock10: Look later
ACE2 receptor protein 
S-Protein - spike protein

## Important Links and Articles

about genetic code :arrow_forward: https://djalmasantos.wordpress.com/2010/11/15/codigo-genetico/
genome Sars-CoV-2 :arrow_forward: https://www.ncbi.nlm.nih.gov/nuccore/MN908947

https://pt.khanacademy.org/science/biology/gene-expression-central-dogma/central-dogma-transcription/a/the-genetic-code-discovery-and-properties
https://www.khanacademy.org/science/biology/gene-expression-central-dogma/translation-polypeptides/a/translation-overview
https://www.sciencedirect.com/science/article/pii/S0092867420302622
