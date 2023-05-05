import logging

import pytest

logger = logging.getLogger(__name__)


@pytest.mark.parametrized_fixture_data("data for test_dummy_3")
def test_dummy_3(setup_tests):
    logger.debug(f"test_dummy_3")
