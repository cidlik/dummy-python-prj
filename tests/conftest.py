import logging
import os

import pytest

logger = logging.getLogger(__name__)


@pytest.fixture(scope="module")
def parametrized_fixture(request):
    logger.debug("parametrized_fixture")
    current_test = os.environ.get("PYTEST_CURRENT_TEST").split(":")[-1].split(" ")[0].split("[")[0]
    test_func = getattr(request.module, current_test)
    if hasattr(test_func, "pytestmark"):
        param = next((m for m in test_func.pytestmark if m.name == "parametrized_fixture_data"), None).args[0]
        logger.warning(f"param = {param}")
        yield param
    else:
        yield


@pytest.fixture
def setup_tests(parametrized_fixture):
    logger.debug("setup_tests")
