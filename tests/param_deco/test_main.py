import logging

import pytest

logger = logging.getLogger(__name__)


@pytest.mark.parametrized_fixture_data("data for test_dummy_1")
@pytest.mark.parametrize("param", ["val1", "val2"])
def test_dummy_1(setup_tests, parametrized_fixture, param):
    assert "data for test_dummy_1" in parametrized_fixture


@pytest.mark.parametrized_fixture_data("data for test_dummy_2")
def test_dummy_2(setup_tests, parametrized_fixture):
    assert "data for test_dummy_2" in parametrized_fixture