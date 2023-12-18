"""Functions for working with ICD9 codes"""

import pandas as pd
import ast

def categorise_icd9(code: str) -> str:

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

    if str(code)[0] in ["E","V"]:
        return "external causes of injury and supplemental classification" 
    elif str(code) == "?":
        return "unknown"
    else:
        code_3char = int(str(code)[0:3])
        for i in lookup:
            if  code_3char >= int(i["start"]) and code_3char <= int(i["end"]):
                return i["desc"]


def interval_type(s: str) -> pd.Interval:
    """Parse interval string to Interval"""
    try:
        import ast
        table = str.maketrans({'[': '(', ']': ')', '-': ','})
        left_closed = s.startswith('[')
        right_closed = s.endswith(']')

        left, right = ast.literal_eval(s.translate(table))

        t = 'neither'
        if left_closed and right_closed:
            t = 'both'
        elif left_closed:
            t = 'left'
        elif right_closed:
            t = 'right'

        return pd.Interval(left, right, closed=t)

    except Exception as e:
        return pd.NA


def charlson_factor_icd9(code) -> int:
    """Determine the Charlson factor for a given ICD9 code"""

    try:
        charlson_groups = pd.read_csv("data/CharlsonRules1.csv")
        charlson_code_map = pd.read_csv("data/CharlsonRules3.csv")
        factor  = charlson_code_map[charlson_code_map["PartialICD9"].str[0:3]==str(code)].join(charlson_groups.set_index('Group'), on="Group")['Factor'].iloc[0]	
    except Exception as e:
        factor = 0

    return factor


def charlson_factor_age(age_interval: pd.Interval) -> int:
    """Determine the Charlson factor for a given age"""

    try:
        age_factor_lookup = pd.DataFrame([{'range' : pd.Interval(50, 60, closed='left'), 'factor' : 1},
                                        {'range' : pd.Interval(60, 70, closed='left'), 'factor' : 2},
                                        {'range' : pd.Interval(70, 80, closed='left'), 'factor' : 3},
                                        {'range' : pd.Interval(80, 150, closed='left'), 'factor' : 4}])

        age_factor = age_factor_lookup[age_factor_lookup.apply(lambda x: age_interval.mid in x.range, axis=1)]['factor'].iloc[0]

    except Exception as e:
        age_factor = 0

    return age_factor


def charlson_comorb_index(diag_list: list, age_interval: pd.Interval) -> int:
    """Calculate the charlson index for a list of diagnoses"""

    charlson_factor_sum = pd.Series([charlson_factor_icd9(diag) for diag in diag_list]).sum()
    
    age_factor = charlson_factor_age(age_interval)

    return charlson_factor_sum + age_factor


def surgical_specialty(specialty):
    """Determine if a specialty is surgical or not"""

    surgical_specialties = [
                            "Surgery-Neuro",
                            "Surgery-Cardiovascular/Thoracic",
                            "Emergency/Trauma",
                            "Orthopedics",
                            "Surgery-General",
                            "Orthopedics-Reconstructive",
                            "Surgery-Pediatric",
                            "Otolaryngology",
                            "Surgery-Vascular",
                            "Urology",
                            "Surgery-Cardiovascular",
                            "Surgery-Thoracic",
                            "Surgery-Plastic",
                            "Surgery-Colon&Rectal",
                            "Surgery-PlasticwithinHeadandNeck",
                            "Obstetrics",
                            ]
    if specialty in surgical_specialties:
        return True
    else:
        return False