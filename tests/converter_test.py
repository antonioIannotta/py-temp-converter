import pytest
from temp_converter.converter import converter

def test_c_to_k():
    assert converter("c", 0, "k") == 273.15
    assert converter("c", 100, "k") == 373.15

def test_c_to_f():
    assert converter("c", 0, "f") == 32
    assert converter("c", 100, "f") == 212

def test_k_to_c():
    assert converter("k", 273.15, "c") == 0
    assert converter("k", 373.15, "c") == 100

def test_k_to_f():
    assert converter("k", 273.15, "f") == 32
    assert converter("k", 373.15, "f") == 212

def test_f_to_c():
    assert converter("f", 32, "c") == 0
    assert converter("f", 212, "c") == 100

def test_f_to_k():
    assert converter("f", 32, "k") == 273.15
    assert converter("f", 212, "k") == 373.15

def test_same_unit():
    assert converter("c", 25, "c") == 25
    assert converter("k", 300, "k") == 300
    assert converter("f", 77, "f") == 77

def test_invalid_unit():
    with pytest.raises(ValueError):
        converter("x", 100, "c")
    with pytest.raises(ValueError):
        converter("c", 100, "x")

def test_invalid_value_type():
    with pytest.raises(TypeError):
        converter("c", "100", "k")