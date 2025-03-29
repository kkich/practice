import pytest
from geometry import calculate_area, calculate_perimeter

def test_rectangle_area():
    assert calculate_area("rectangle", width=5, height=10) == 50

def test_circle_area():
    assert round(calculate_area("circle", radius=3), 2) == 28.27

def test_invalid_area():
    with pytest.raises(ValueError):
        calculate_area("triangle", base=5, height=10)

def test_rectangle_perimeter():
    assert calculate_perimeter("rectangle", width=5, height=10) == 30

def test_circle_perimeter():
    assert round(calculate_perimeter("circle", radius=3), 2) == 18.85

def test_invalid_perimeter():
    with pytest.raises(ValueError):
        calculate_perimeter("triangle", base=5, height=10)
