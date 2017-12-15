import pytest

def pytest_addoption(parser):
    parser.addoption("--algorithmia_api_key", action="store", default="",
        help="algorithmia_api_key: simXXXXXXXXXX")

@pytest.fixture
def algorithmia_api_key(request):
    return request.config.getoption("--algorithmia_api_key")
