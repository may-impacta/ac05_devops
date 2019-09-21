import pytest 
from com.kuma.calcula_parcela import valorPagamento

def test_parcela():
	assert valorPagamento(-1,0) == None, "Should be None"
	assert valorPagamento(500,5) == 540.00, "Should be 540.00"
	assert valorPagamento(100,0) == 100.00, "Should be 100.00"
