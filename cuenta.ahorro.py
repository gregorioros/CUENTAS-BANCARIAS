from cuenta import Cuenta_Bancaria

class Cuenta_ahorro (Cuenta_Bancaria):
    def __init__(self, interes: float= 0, numero= None, nombrepropietario= None, saldo:float=0):
        self._interes = interes
        super(Cuenta_ahorro, self).__init__(numero=numero, nombrepropietario=nombrepropietario, saldo=saldo)

        @property
        def interes(self):
            return self._interes

        @interes.setter
        def interes(self, interes):
            self._interes = interes


        def pagar_interes(self):
            self._saldo = self._saldo + ((float(self._saldo) * int(self._interes))/100)
            return self._saldo
if __name__ == '__main__':
            Cuentas_ahorros = Cuenta_ahorro (6,'0950643973', 'fernando', '680')

            Cuentas_ahorros.mostrar_saldo()
            Cuentas_ahorros.credito(1800)

            Cuentas_ahorros.mostrar_saldo()
            Cuentas_ahorros.debito(45)

            print(Cuentas_ahorros)