class account():
    def __init__(self, holder, balance = 0):
        self.holder = holder
        self.balance = balance

    def deposit(self, dep_ammount):
        self.balance = self.balance + dep_ammount
        print(f"Added {dep_ammount} to your account. Now you have {self.balance}.")


class credit_card():
    consumption = 0
    def __init__(self,holder,account_linked,maxx=10000):
        self.holder = holder
        self.maxx = maxx
        self.account_linked = account_linked
        print(f"Tarjeta de crédito de {self.holder} creada. Linea de credito asignada es {self.maxx}.")

    def gastar(self, monto):
        self.monto = monto
        if self.maxx - self.consumption > monto:
            self.consumption += monto
            print(f"Gastaste {self.monto}, te queda {self.maxx - self.monto} restante de linea de credito.")
        else:

            print(f"Max de {self.maxx} alcanzado")
    
    def pagar(self,pago):
        self.pago = pago
        
        if self.pago > self.account_linked.balance:
            print(f"Sorry, te faltan {self.pago - self.account_linked.balance} en tu cuenta.")
        else:
            self.account_linked.balance -= self.pago
            self.consumption -= self.pago
            print(f"Pagaste {self.pago}, tu línea de crédito restante es ahora {self.maxx - self.consumption}. Te quedan {self.account_linked.balance} en la cuenta.")


if __name__ == "__main__":
    name = input("Ingresa el titular de la cuenta: ")
    cuenta_cliente = account(name)
    deposito = int(input("Ingresa el monto a depositar: "))
    cuenta_cliente.deposit(deposito)

    if ('y'==input("Desea crear tarjeta de crédito? (y/n)").lower()):
        tarj_cliente = credit_card(name,cuenta_cliente)
        gasto = int(input("Ingrese el monto a gastar: "))
        tarj_cliente.gastar(gasto)
    else:
        print("Ok, no se creara tarjeta.")


    try:
        print(f"Acerca de tarjeta de {tarj_cliente.holder}...")
    except Exception as e:
        print(f"Hubo un error {e}.")
    else:
        print(f"Desea pagar algo de su consumo de tarjeta ({tarj_cliente.consumption}) con el monto de su cuenta ({cuenta_cliente.balance})? (y/n):")
        if ('y'== input()):
            monto = int(input("Ingrese el monto a pagar: "))
            tarj_cliente.pagar(monto)
        else:
            print(f"Ok, nos debe {self.consumption}. Le resta {self.maxx - self.consumption} de línea de crédito. su saldo débito es de {self.balance}.")
    finally:
        print("Fin de transaccion.")