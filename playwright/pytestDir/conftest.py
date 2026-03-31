import pytest

@pytest.fixture(scope = "session")     # scope = module or function or class or session
def preSetupWork():
    print("I setup browser instance")
    
