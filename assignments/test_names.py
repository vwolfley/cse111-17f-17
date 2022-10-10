from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest


def test_make_full_name():
    """Verify that the make_full_name function works correctly.
    Parameters: none
    Return: nothing
    """

    # Call the make_full_name function ten times and use an assert
    # statement to verify that the string returned by the
    # make_full_name function is correct each time.
    assert make_full_name("Vern", "Wolfley") == "Wolfley; Vern"
    assert make_full_name("Bill", "Clinton") == "Clinton; Bill"
    assert make_full_name("Tom", "Jones") == "Jones; Tom"
    assert make_full_name("Julia", "Louis-Dreyfus") == "Louis-Dreyfus; Julia"
    assert make_full_name("Kiefer", "Sutherland") == "Sutherland; Kiefer"
    assert make_full_name("José", "Francisco de Paula") == "Francisco de Paula; José"
    assert make_full_name("Rosie", "Huntington-Whiteley") == "Huntington-Whiteley; Rosie"
    assert make_full_name("BJ", "Bear") == "Bear; BJ"
    assert make_full_name("CY", "Young") == "Young; CY"
    assert make_full_name("Bartholomew", "Armstrong") == "Armstrong; Bartholomew"



def test_extract_family_name():
    """Verify that the extract_family_name function works correctly.
    Parameters: none
    Return: nothing
    """

    # Call the extract_family_name function ten times and use an assert
    # statement to verify that the string returned by the
    # extract_family_name function is correct each time.
    assert extract_family_name("Wolfley; Vern") == "Wolfley"
    assert extract_family_name("Clinton; Bill") == "Clinton"
    assert extract_family_name("Jones; Tom") == "Jones"
    assert extract_family_name("Louis-Dreyfus; Julia") == "Louis-Dreyfus"
    assert extract_family_name("Sutherland; Kiefer") == "Sutherland"
    assert extract_family_name("Francisco de Paula; José") == "Francisco de Paula"
    assert extract_family_name("Huntington-Whiteley; Rosie") == "Huntington-Whiteley"
    assert extract_family_name("Bear; BJ") == "Bear"
    assert extract_family_name("Young; CY") == "Young"
    assert extract_family_name("Armstrong; Bartholomew") == "Armstrong"



def test_extract_given_name():
    """Verify that the extract_given_name function works correctly.
    Parameters: none
    Return: nothing
    """

    # Call the extract_given_name function ten times and use an assert
    # statement to verify that the string returned by the
    # extract_given_name function is correct each time.
    assert extract_given_name("Wolfley; Vern") == "Vern"
    assert extract_given_name("Clinton; Bill") == "Bill"
    assert extract_given_name("Jones; Tom") == "Tom"
    assert extract_given_name("Louis-Dreyfus; Julia") == "Julia"
    assert extract_given_name("Sutherland; Kiefer") == "Kiefer"
    assert extract_given_name("Francisco de Paula; José") == "José"
    assert extract_given_name("Huntington-Whiteley; Rosie") == "Rosie"
    assert extract_given_name("Bear; BJ") == "BJ"
    assert extract_given_name("Young; CY") == "CY"
    assert extract_given_name("Armstrong; Bartholomew") == "Bartholomew"

  

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])