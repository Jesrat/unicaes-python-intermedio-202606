
print("definiendo la clase SaldoInsuficiente")


class SaldoInsuficiente(Exception):
    def __init__(self, saldo_actual, monto_requerido):
        self.saldo_actual = saldo_actual
        self.monto_requerido = monto_requerido
        super().__init__(
            f"Saldo insuficiente: tienes '${saldo_actual:.2f}' "
            f"y el monto requerido es '${monto_requerido:.2f}'"
        )


print(__name__)
if __name__ == '__main__':
    try:
        # simulando hacer un debito
        raise SaldoInsuficiente(12, 23)
    except SaldoInsuficiente as e:
        print(f"el saldo actual de la cuneta es {e.saldo_actual}")
        raise e
