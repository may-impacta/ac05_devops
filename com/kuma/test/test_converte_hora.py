import pytest 
from com.kuma.converte_hora import converteHora

def test_hora():
    assert converteHora(13,1) == "01:01 PM", "Should be 01:01 PM"
       