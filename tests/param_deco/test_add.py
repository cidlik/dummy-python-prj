import logging

import pytest

logger = logging.getLogger(__name__)


@pytest.mark.parametrize("parametrized_fixture", ["data for test_dummy_3"], indirect=True)
def test_dummy_3(setup_tests, parametrized_fixture):
    assert "data for test_dummy_3" in parametrized_fixture
