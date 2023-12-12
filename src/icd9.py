# make some tools for dealing with ICD9 codes

# regex mask

def categorise_icd9(code):

    lookup = [{"mask":"","start":"001", "end":"139", "desc": "infectious and parasitic diseases"},
    {"mask":"","start":"140", "end":"239", "desc": "neoplasms"},
    {"mask":"","start":"240", "end":"279", "desc": "endocrine, nutritional and metabolic diseases, and immunity disorders"},
    {"mask":"","start":"280", "end":"289", "desc": "diseases of the blood and blood-forming organs"},
    {"mask":"","start":"290", "end":"319", "desc": "mental disorders"},
    {"mask":"","start":"320", "end":"389", "desc": "diseases of the nervous system and sense organs"},
    {"mask":"","start":"390", "end":"459", "desc": "diseases of the circulatory system"},
    {"mask":"","start":"460", "end":"519", "desc": "diseases of the respiratory system"},
    {"mask":"","start":"520", "end":"579", "desc": "diseases of the digestive system"},
    {"mask":"","start":"580", "end":"629", "desc": "diseases of the genitourinary system"},
    {"mask":"","start":"630", "end":"679", "desc": "complications of pregnancy, childbirth, and the puerperium"},
    {"mask":"","start":"680", "end":"709", "desc": "diseases of the skin and subcutaneous tissue"},
    {"mask":"","start":"710", "end":"739", "desc": "diseases of the musculoskeletal system and connective tissue"},
    {"mask":"","start":"740", "end":"759", "desc": "congenital anomalies"},
    {"mask":"","start":"760", "end":"779", "desc": "certain conditions originating in the perinatal period"},
    {"mask":"","start":"780", "end":"799", "desc": "symptoms, signs, and ill-defined conditions"},
    {"mask":"","start":"800", "end":"999", "desc": "injury and poisoning"}]

    if code[0] in ["E","V"]:
        return "external causes of injury and supplemental classification" 
    else:
        for i in lookup:
            if code >= i["start"] and code <= i["end"]:
                return i["desc"]
        