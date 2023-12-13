"""Tests for the icd9 module."""

import pytest
import pandas as pd
import numpy as np
from src.icd9 import icd9, interval_type, charlson_factor_icd9, charlson_factor_age

def test_icd9():
    