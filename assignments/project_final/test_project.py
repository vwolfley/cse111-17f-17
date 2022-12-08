####################
# Date: 2022-10-22
# File: test_project.py
# Author: Vern Wolfley
# Class: CSE 111
# Purpose: Testing for project 
#####################

from project import read_enrollment_ethnicity
from pytest import approx
import pytest

def test_file_import():
    assert read_enrollment_ethnicity.shape == (2419, 13)