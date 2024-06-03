print('*** cajero automático ***')

saldo = 1000

salir = False
while not salir:
    print(f'''Operaciones que puedes realizar:
    1. Consultar saldo
    2. Retirar
    3. Depositar
    4. Salir''')
    opcion = int(input('Escoje una opción: '))
    if opcion == 1:
        print(f'Tu saldo actual es: {saldo}')
    elif opcion == 2:
        monto_retiro = int(input('ingrese la suma  retirar: '))
        if saldo >= monto_retiro:
            saldo = saldo - monto_retiro
            print(f'''tu retiro es de: {monto_retiro}\ntu saldo restante es de:{saldo}''')
        elif saldo < monto_retiro:
            print('Saldo insuficiente')
        else:
            print('ingrese un monto valido')
    elif opcion == 3:
        ingreso = int(input('ingrese el monto a depositar: '))
        saldo = saldo + ingreso
        print(f'tu nuevo saldo es de: {saldo}')
    elif opcion == 4:
        print('Saliendo del sistema')
        salir = True
    else:
        print('ingrese una opción valida')