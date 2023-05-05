import logging

import pytest

import src
import tests

logger = logging.getLogger(__name__)


@pytest.fixture
def useless_fixture():
    print("useless fixture")


@tests.wrap_custom_deco(["pack1", "pack2"])
@pytest.mark.parametrize(
    "s", ["foo", "bar"]
)
def test_negation(useless_fixture, s: str):
    retval = src.Negation(s)
    logger.debug(retval.value)
    assert retval.value == f"Not a {s}"
