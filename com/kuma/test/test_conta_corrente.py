import pytest
from com.kuma.conta_corrente import ContaCorrente

def test_conta():
    conta = ContaCorrente(100, 'Tales')
    conta.deposito(100)
    assert(conta.deposito)
    conta.saque(200)
    assert(conta.saldo)
