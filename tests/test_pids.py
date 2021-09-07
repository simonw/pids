import pytest
import pids

def test_from_int():
    assert pids.pid.from_int(1234) == "gxd"


def test_to_int():
    assert pids.pid.to_int("gxd") == 1234
