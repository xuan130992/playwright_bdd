import os
import pytest
from dotenv import load_dotenv
import pytest


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    print(">>> conftest.py loaded111 <<<")
    return {

        **browser_type_launch_args,
        "headless": False,    # <--- bật UI
        "slow_mo": 250        # <--- thao tác chậm 250ms để dễ quan sát
    }
load_dotenv(".env.qa")
@pytest.fixture(scope='session',autouse=True)
def load_env():
    print(">>> load_env fixture is running <<<")
    print("printos",os.getenv('BASE_URL'))
    yield

@pytest.fixture(scope='session')
def username():

    return os.getenv('USERNAME')
@pytest.fixture(scope='session')
def password():
    return os.getenv('PASSWORD')
@pytest.fixture(scope='session')
def base_url():
    url = os.getenv('BASE_URL')
    print("testtttttttt")
    print(f"fixture.baseurl={url}")
    if not url:
        raise ValueError("BASE_URL not found in .env.qa")
    return url
