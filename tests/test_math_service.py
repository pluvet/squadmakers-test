from source.services.math import MathService

def test_mcm():
    mcm = MathService.mcm(nums=[5,15])
    
    assert isinstance(mcm, dict)
    
def test_number():
    number = MathService.add_one(num=5)

    assert isinstance(number, dict)