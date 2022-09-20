from source.domain.math import mcm, add_one

def test_mcm():
    mcm_number = mcm(nums=[30,45])

    assert mcm_number == 90
    
def test_add_one():
    number = add_one(1)
    
    assert number == 2