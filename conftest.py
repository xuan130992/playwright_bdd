import os
import pytest
from dotenv import load_dotenv
import pytest


# --- ENV aliases mapping ---
ENV_ALIASES = {
    "QA": "qa",
    "SB": "sb",
    "PROD": "prod",
}

def normalize_env(value: str) -> str:
    if not value:
        return "QA"
    upper = value.upper()
    if upper not in ENV_ALIASES:
        raise ValueError(f"❌ Unsupported --env '{value}'. Use one of: {list(ENV_ALIASES.keys())}")
    return upper

def env_filename(env_upper: str) -> str:
    return f".env.{ENV_ALIASES[env_upper]}"


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    print(">>> conftest.py loaded111 <<<")
    return {

        **browser_type_launch_args,
        "headless": False,    # <--- bật UI
        "slow_mo": 500        # <--- thao tác chậm 250ms để dễ quan sát
    }
#load_dotenv(".env.qa")
def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="QA", help="Environment: QA/SB/PROD")
@pytest.fixture(scope='session',autouse=True)
def load_env(request):
    env = request.config.getoption("--env").upper()
    env_file = f".env.{env.lower()}"
    if not os.path.exists(env_file):
        raise FileNotFoundError(f"❌ Env file not found: {env_file}")
    from dotenv import load_dotenv
    load_dotenv(env_file, override=True)
    print(f"✅ Loaded environment: {env_file}")
    print(f"BASE_URL = {os.getenv('BASE_URL')}")

@pytest.fixture(scope='session')
def username():

    return os.getenv('PARTNER_USERNAME')
@pytest.fixture(scope='session')
def password():
    return os.getenv('PARTNER_PASSWORD')

@pytest.fixture(scope='session')
def base_url(request,load_env):
    env = request.config.getoption("--env").upper()
    env_file = f".env.{env.lower()}"
    url = os.getenv("BASE_URL")
    print(f"fixture.baseurl={url}")
    if not url:
        raise ValueError(f"BASE_URL not found in {env_file}")
    return url

@pytest.fixture(scope='session')
def main_display_url():
    main_page_url = os.getenv("MAIN_PAGE_URL")
    return main_page_url
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    storage_path = "./tests/auth/storage_state.json"
    if os.path.exists(storage_path):
        print(f"✅ Using storage state: {storage_path}")
        return {
            **browser_context_args,
            "storage_state": storage_path,
        }
    else:
        print("⚠️ storage_state.json not found — running without saved login state")
        return browser_context_args

ENV = os.getenv("ENV", "QA").upper()
# Định nghĩa locator theo môi trường
LOCATORS = {
    "co_iframe": {
        "QA": "#iframe-BLZ00000001004",
        "SB": "#iframe-BLZ00000000001"
    },
    "mo_iframe": {
        "QA": "#iframe-BLZ00000005001",
        "SB": "#iframe-BLZ00000000001"
    }
}
@pytest.fixture(scope="session")
def env_config():
    """Fixture trả về ENV và LOCATORS để dùng ở mọi test."""
    return {
        "ENV": ENV,
        "LOCATORS": LOCATORS
    }
