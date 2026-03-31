# Fixtures
import pytest

@pytest.fixture(scope = "module")     # scope = module or function or class or session
def preWork():
    print("I setup module instance")
    return "pass"
            
@pytest.fixture(scope = "function")     
def secondWork():
    print("I setup secondWork instance")
    yield   # pause and go to the original test(in this case i.e: test_initialCheck) and come back
    print("tear down validation")

@pytest.mark.smoke
def test_initialCheck(preWork, secondWork):         # pytest -s .\test_PyTestValidation.py::test_initialCheck
    print("This is first test")
    assert preWork == "pass"
    
@pytest.mark.skip             # To skip test      # pytest -s
def test_SecondCheck(preSetupWork, secondWork):
    print("This is Second test")