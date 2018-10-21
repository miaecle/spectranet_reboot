## calculate_frag_mz.py
## collection of functions to calculate fragment m/z from the peptide sequence and ion information

from pyteomics import mass
import parse_data

## set new dictionary elements for the characters we defined for modified amino acids
aa_comp = dict(mass.std_aa_comp)

## go from our new coding back to chemical formula
#   "C[160]": "!",   cystine + Carbamidomethyl
#   "M[147]": "@",   methionine + oxidation
#   "Q[129]": "#",   glutamine + deamidation
#   "N[115]": "$",   asparagine + deamidation
aa_comp["!"] = mass.Composition('C5H8N2O2S1')  ## these need chemical formulas for C[160], etc
aa_comp["@"] = mass.Composition('C5H9N1O2S1')
aa_comp["#"] = mass.Composition('C5H7N1O3')
aa_comp["$"] = mass.Composition('C4H5N1O3')


def get_frag_mz(one_hot, ion_position, ion_type, ion_charge):
  ## go from one hot back to our custom code 
  pep_seq = reverse_one_hot_encode(one_hot, amino_acid_modified_codes)
  
  if (ion_type = 'b'):
    ion_seq = pep_seq[:ion_position]
  elif (ion_type = 'y'):
    ion_seq = pep_seq[-ion_position:]
  
  mz = mass.calculate_mass(sequence=ion_seq, ion_type=ion_type, charge=ion_charge)
  return mz


  