from meseta import Meseta
import pytest

@pytest.mark.parametrize("width, height, expected_result", [
    (4,4, "Meseta 4x4"),
    (5,5, "Meseta 5x5"),
    (3,4, "Meseta 3x4")
])
def test_str(width,height, expected_result):
    my_meseta=Meseta(width,height)
    assert str(my_meseta) == expected_result

@pytest.mark.parametrize("width, height, x, y, expected_result", [
    (4,4,1,3, True),
    (4,4,1,5, False),
    (1,2,0,0, True),
])
def test_dentro_limites(width, height, x, y, expected_result):
    my_meseta=Meseta(width,height)
    assert my_meseta.within_the_limits(x, y) == expected_result


