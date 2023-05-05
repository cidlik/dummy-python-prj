import logging
import os

import pytest

logger = logging.getLogger(__name__)


@pytest.fixture(scope="module")
def parametrized_fixture(request):
    logger.debug("parametrized_fixture")
    if hasattr(request, "param"):
        logger.warning(f"param = {request.param}")
        yield request.param
    else:
        yield


@pytest.fixture
def setup_tests(parametrized_fixture):
    logger.debug("setup_tests")
