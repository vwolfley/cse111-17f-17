from address import extract_city, extract_state, extract_zipcode
import pytest


def test_extract_city():
    """Verify that the extract_city function works correctly.
    Parameters: none
    Return: nothing
    """

    # Call the extract_city function ten times and use an assert
    # statement to verify that the string returned by the
    # extract_city function is correct each time.
    # number and street, city, state zipcode
    assert extract_city("12833 W Llano Dr, Litchfield Park, AZ 85340") == "Litchfield Park"
    assert extract_city("13513 W Verde Ln, Avondale, AZ 85392-3562") == "Avondale"
    assert extract_city("11291 N Dysart Rd, El Mirage, AZ 85335") == "El Mirage"
    assert extract_city("22376 N 94th Ln, Peoria, AZ 85383") == "Peoria"
    assert extract_city("14551 W La Reata Ave, Goodyear, AZ 85395") == "Goodyear"
    assert extract_city("2069 W Arya Ct, South Jordan, UT 84095") == "South Jordan"
    assert extract_city("1086 Jade Hill Ave, Sun Land Park, NM 88008") == "Sun Land Park"
    assert extract_city("327 E Alvarado Rd, Phoenix, AZ 85004") == "Phoenix"
    assert extract_city("13475 Hedi Rd, Woodland Park, CO 80863") == "Woodland Park"
    assert extract_city("15802 N Parkview Pl, Surprise, AZ 85374") == "Surprise"



def test_extract_state():
    """Verify that the extract_state function works correctly.
    Parameters: none
    Return: nothing
    """

    # Call the extract_state function ten times and use an assert
    # statement to verify that the string returned by the
    # extract_state function is correct each time.
    # number and street, city, state zipcode
    assert extract_state("12833 W Llano Dr, Litchfield Park, AZ 85340") == "AZ"
    assert extract_state("13513 W Verde Ln, Avondale, AZ 85392-3562") == "AZ"
    assert extract_state("11291 N Dysart Rd, El Mirage, AZ 85335") == "AZ"
    assert extract_state("22376 N 94th Ln, Peoria, AZ 85383") == "AZ"
    assert extract_state("14551 W La Reata Ave, Goodyear, AZ 85395") == "AZ"
    assert extract_state("2069 W Arya Ct, South Jordan, UT 84095") == "UT"
    assert extract_state("1086 Jade Hill Ave, Sun Land Park, NM 88008") == "NM"
    assert extract_state("327 E Alvarado Rd, Phoenix, AZ 85004") == "AZ"
    assert extract_state("13475 Hedi Rd, Woodland Park, CO 80863") == "CO"
    assert extract_state("15802 N Parkview Pl, Surprise, AZ 85374") == "AZ"
    
    
def test_extract_zipcode():
    """Verify that the extract_zipcode function works correctly.
    Parameters: none
    Return: nothing
    """

    # Call the extract_zipcode function ten times and use an assert
    # statement to verify that the string returned by the
    # extract_zipcode function is correct each time.
    # number and street, city, state zipcode
    assert extract_zipcode("12833 W Llano Dr, Litchfield Park, AZ 85340") == "85340"
    assert extract_zipcode("13513 W Verde Ln, Avondale, AZ 85392-3562") == "85392-3562"
    assert extract_zipcode("11291 N Dysart Rd, El Mirage, AZ 85335") == "85335"
    assert extract_zipcode("22376 N 94th Ln, Peoria, AZ 85383") == "85383"
    assert extract_zipcode("14551 W La Reata Ave, Goodyear, AZ 85395") == "85395"
    assert extract_zipcode("2069 W Arya Ct, South Jordan, UT 84095") == "84095"
    assert extract_zipcode("1086 Jade Hill Ave, Sun Land Park, NM 88008") == "88008"
    assert extract_zipcode("327 E Alvarado Rd, Phoenix, AZ 85004") == "85004"
    assert extract_zipcode("13475 Hedi Rd, Woodland Park, CO 80863") == "80863"
    assert extract_zipcode("15802 N Parkview Pl, Surprise, AZ 85374") == "85374"







# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])