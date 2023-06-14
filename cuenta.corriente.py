from cuenta import Cuenta_Bancaria

class Cuenta_corriente (Cuenta_Bancaria):

    def __init__(self, numero= None, nombrepropietario= None, saldo:float= 0, tiene_cheque=bool):
        self._tiene_cheque= tiene_cheque
        super(Cuenta_corriente, self).__init__(numero=numero, nombrepropietario=nombrepropietario, saldo=saldo)

    @property
    def tiene_cheque(self):
        return self._tiene_cheque

    @tiene_cheque.setter
    def tiene_cheque(self, tiene_cheque):
        self._tiene_cheque = tiene_cheque
        return self._saldo

    def pagar_cheque(self):
        self._saldo = self._saldo + ((float (self._saldo) - int (self._pagar_cheque)))
        return self._saldo

if __name__=='__main__':
    Cuentas_corrientes = Cuenta_corriente('0950643973', 'fernando', '380', bool)

    Cuentas_corrientes.mostrar_saldo()
    Cuentas_corrientes.credito(2800)

    Cuentas_corrientes.mostrar_saldo()
    Cuentas_corrientes.debito(190)

    print(Cuentas_corrientes)