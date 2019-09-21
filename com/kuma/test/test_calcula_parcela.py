import pytest 
from com.kuma.calcula_parcela import valorPagamento

def test_parcela():
    assert valorPagamento(500,5) == 540.00, "Should be 540.00"
       