import pytest
from rover import Rover
from meseta import Meseta

@pytest.mark.parametrize("x, y, direction, command,meseta, expected_result", [
    (0,0,"N","F", Meseta(3,4),"(0,1,N)"), 
    (0,2,"N","B",Meseta(3,4),"(0,1,N)"), 
    (0,0,"N","L",Meseta(3,4),"(0,0,W)"), 
    (0,0,"N","R",Meseta(3,4),"(0,0,E)"), 
    (0,0,"N","FF",Meseta(3,4),"(0,2,N)"), 
    (0,0,"E","F",Meseta(3,4),"(1,0,E)"), 
    (0,0,"E","FF",Meseta(3,4),"(2,0,E)"), 
    (1,1,"N","LF",Meseta(3,4),"(0,1,W)"), 
    (0,0,"N","LRFF",Meseta(3,4),"(0,2,N)"), 
    (3,2,"N","LLBB",Meseta(3,4),"(3,2,S)"), # En este punto se sale de la meseta
    (1,1,"N","RRRFLF",Meseta(3,4),"(0,0,S)"), 
    (1,1,"N","LFLLFFR",Meseta(3,4),"(2,1,S)"), 
    (1,2,"N","LFLFF",Meseta(3,4),"(0,0,S)"), 
])
def test_move(x,y, direction, command, meseta, expected_result):
    my_rover=Rover(x,y, direction, meseta) 
    my_rover.move(command)
    assert my_rover.get_current_position()==expected_result
