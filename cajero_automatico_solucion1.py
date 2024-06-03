print('*** Cajero Automático ***')

saldo = 1000  # Saldo Inicial
salir = False

while not salir:
    print(f'''Operaciones que puedes realizar:
    1. Consultar Saldo
    2. Retirar
    3. Depositar
    4. Salir''')
    opcion = int(input('Escoje una opción: '))
    if opcion == 1:
        print(f'Tu saldo actual es de: $ {saldo:.2f}\n')
    elif opcion == 2:
        retiro = float(input('ingrese el monto a retirar: '))
        if retiro <= saldo:
            saldo -= retiro
            print(f'El monto retirado es de: $ {retiro:.2f}')
            print(f'El saldo restante en tu cuenta es de: $ {saldo:.2f}\n')
        else:
            print(f'No cuentas con saldo suficiente, Saldo actual $ {saldo:.2f}\n')
    elif opcion == 3:
        deposito = float(input('Ingresa el monto a depositar: '))
        saldo += deposito
        print(f'Tu nuevo saldo es de: $ {saldo:.2f}\n')
    elif opcion == 4:
        print('Saliendo del sistema')
        salir = True
    else:
        print('Seleccione una opción valida')
