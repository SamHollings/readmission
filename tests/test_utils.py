"""Tests for the utils module."""

import pytest
import pandas as pd
import numpy as np
import src.utils as utils


def test_categorise_icd9():
    assert utils.categorise_icd9("401.9") == "diseases of the circulatory system"
    assert utils.categorise_icd9(250) == "endocrine, nutritional and metabolic diseases, and immunity disorders"
    assert utils.categorise_icd9("V70.0") == "external causes of injury and supplemental classification"


def test_interval_type():
    assert utils.interval_type("[1-10)") == pd.Interval(1, 10, closed="left")
    assert utils.interval_type("[20-30]") == pd.Interval(20, 30,closed="both")
    assert utils.interval_type("(90-100]") == pd.Interval(90, 100, closed="right")


def test_charlson_factor_icd9():
    assert utils.charlson_factor_icd9("401") == 0
    assert utils.charlson_factor_icd9("196") == 6
    assert utils.charlson_factor_icd9("V70") == 0


def test_charlson_factor_age():
    assert utils.charlson_factor_age(pd.Interval(40, 49)) == 0
    assert utils.charlson_factor_age(pd.Interval(50, 59)) == 1
    assert utils.charlson_factor_age(pd.Interval(60, 69)) == 2


def test_charlson_comorb_index():
    diag_list = ["401", "196", "V70"]
    age_interval = pd.Interval(50, 59)
    assert utils.charlson_comorb_index(diag_list, age_interval) == 7


def test_surgical_specialty():
    assert utils.surgical_specialty("Surgery-Neuro") == True
    assert utils.surgical_specialty("Emergency/Trauma") == True
    assert utils.surgical_specialty("Internal Medicine") == False

