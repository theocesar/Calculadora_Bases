print('''Qual operação deverá ser realizada? 
{ 1 } - Conversão de bases
{ 2 } - Soma ou Subtração''')
operação = int(input('Operação escolhida: '))

# menu to determine which operation will be done.
if operação < 1 or operação > 2:
    print('Operação Inválida. Tente Novamente')


# menu to determine the numeric bases involved in the conversion.
if operação == 1:
    print('''Determine a base de referência: 
    [ 1 ] Binária
    [ 2 ] Decimal
    [ 3 ] Octal
    [ 4 ] Hexadecimal''')
    opção = int(input('Base escolhida: '))
    if opção < 1 or opção > 4:
        print('Opção Inválida. Tente Novamente')
        exit()

    print('''Determine a base para qual o número será convertido:  
    [ 1 ] Binária
    [ 2 ] Decimal
    [ 3 ] Octal
    [ 4 ] Hexadecimal''')
    opção_final = int(input('Base escolhida: '))
    if opção == opção_final:
        print('Opção Inválida.Tente Novamente')
        exit()
    if opção_final < 1 or opção_final > 4:
        print('Opção Inválida.Tente Novamente')
        exit()

    if opção == 1:

        # command block with the binary base as reference.
        # performs all possible conversions with this base.
        num = (input('Digite o número binário a ser convertido: '))

        # converts the chosen number to decimal base.
        decimal = int(num, 2)

        # printing the results.
        if opção_final == 2:
            if decimal >= 0:
                print(f'O número BINÁRIO {num} convertido para DECIMAL é igual a {decimal}')
            else:
                print(f'O número BINÁRIO {num} convertido para DECIMAL é igual a {decimal}')
        elif opção_final == 3:
            if decimal >= 0:
                print(f'O número BINÁRIO {num} convertido para OCTAL é igual a {oct(decimal) [2:]}')
            else:
                print(f'O número BINÁRIO {num} convertido para OCTAL é igual a -{oct(decimal)[3:]}')
        elif opção_final == 4:
            if decimal >= 0:
                print(f'O número BINÁRIO {num} convertido para HEXADECIMAL é igual a {hex(decimal)[2:]}')
            else:
                print(f'O número BINÁRIO {num} convertido para HEXADECIMAL é igual a -{hex(decimal)[3:]}')

    if opção == 2:

        # command block with decimal base as reference.
        # performs all possible conversions with this base.
        # because you are working with a decimal base, you don't need to convert anything beforehand.
        num = int(input('Digite o número decimal a ser convertido: '))

        # printing the results.
        if opção_final == 1:
            if num >= 0:
                print(f'O número DECIMAL {num} convertido para BINÁRIO é igual a {bin(num)[2:]}')
            else:
                print(f'O número DECIMAL {num} convertido para BINÁRIO é igual a {bin(num)[3:]}')
        elif opção_final == 3:
            if num >= 0:
                print(f'O número DECIMAL {num} convertido para OCTAL é igual a {oct(num)[2:]}')
            else:
                print(f'O número DECIMAL {num} convertido para OCTAL é igual a -{oct(num)[3:]}')
        elif opção_final == 4:
            if num >= 0:
                print(f'O número DECIMAL {num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
            else:
                print(f'O número DECIMAL {num} convertido para HEXADECIMAL é igual a -{hex(num)[3:]}')

    if opção == 3:

        # command block with octal base as reference.
        # performs all possible conversions with this base.
        num = (input('Digite o número octal a ser convertido: '))

        # converts the chosen number to decimal base.
        decimal = int(num, 8)

        # printing the results.
        if opção_final == 1:
            if decimal >= 0:
                print(f'O número OCTAL {num} convertido para BINÁRIO é igual a {bin(decimal)[2:]}')
            else:
                print(f'O número OCTAL {num} convertido para BINÁRIO é igual a -{bin(decimal)[3:]}')
        elif opção_final == 2:
            if decimal >= 0:
                print(f'O número OCTAL {num} convertido para DECIMAL é igual a {decimal}')
            else:
                print(f'O número OCTAL {num} convertido para DECIMAL é igual a -{decimal}')
        elif opção_final == 4:
            if decimal >= 0:
                print(f'O número OCTAL {num} convertido para HEXADECIMAL é igual a {hex(decimal)[2:]}')
            else:
                print(f'O número OCTAL {num} convertido para HEXADECIMAL é igual a -{hex(decimal)[3:]}')

    if opção == 4:

        # command block with the hexadecimal base as reference.
        # performs all possible conversions with this base.
        num = (input('Digite o número hexadecimal a ser convertido: '))

        # converts the chosen number to decimal base.
        decimal = int(num, 16)

        # printing the results.
        if opção_final == 1:
            if decimal >= 0:
                print(f'O número HEXADECIMAL {num} convertido para BINÁRIO é igual a {bin(decimal)[2:]}')
            else:
                print(f'O número HEXADECIMAL {num} convertido para BINÁRIO é igual a {bin(decimal)[3:]}')
        elif opção_final == 2:
            if decimal >= 0:
                print(f'O número HEXADECIMAL {num} convertido para DECIMAL é igual a {hex(decimal)}')
            else:
                print(f'O número HEXADECIMAL {num} convertido para DECIMAL é igual a {hex(decimal)}')
        elif opção_final == 3:
            if decimal >= 0:
                print(f'O número HEXADECIMAL {num} convertido para OCTAL é igual a {hex(decimal)[2:]}')
            else:
                print(f'O número HEXADECIMAL {num} convertido para OCTAL é igual a -{hex(decimal)[3:]}')


# menu to choose which operation to perform.
if operação == 2:
    print('''Qual das operações deve ser realizada? 
    { 1 } - Soma
    { 2 } - Subtração''')
    operação02 = int(input('Operação escolhida: '))
    if operação02 < 1 or operação02 > 2:
        print('Operação Inválida.')
    print('''Determine qual a base primária da operação (referente ao primeiro número): 
    [ 1 ] Binária
    [ 2 ] Decimal
    [ 3 ] Octal
    [ 4 ] Hexadecimal''')
    opção02 = int(input('Sua escolha: '))
    if opção02 < 1 or opção02 > 4:
        print('Opção Inválida. Tente Novamente')
        exit()
    print('''Determine qual a base secundária da operação (referente ao segundo número): 
    [ 1 ] Binária
    [ 2 ] Decimal
    [ 3 ] Octal
    [ 4 ] Hexadecimal''')
    opção02_final = int(input('Sua escolha: '))

    # entering the numbers for the operations.
    # when obtaining the operand numbers, they are converted to decimal base.
    if opção02 == 1:
        num = (input('Número primordial da operação (BINÁRIO):'))
        decimal01 = int(num, 2)

    elif opção02 == 2:
        num = (input('Número primordial da operação (DECIMAL):'))
        decimal01 = num

    elif opção02 == 3:
        num = (input('Número primordial da operação (OCTAL):'))
        decimal01 = int(num, 8)

    elif opção02 == 4:
        num = (input('Número primordial da operação (HEXADECIMAL):'))
        decimal01 = int(num, 16)

    if opção02_final == 1:
        num2 = (input('Número secundário da operação (BINÁRIO):'))
        decimal02 = int(num2, 2)

    elif opção02_final == 2:
        num2 = (input('Número secundário da operação (DECIMAL):'))
        decimal02 = int(num2)

    elif opção02_final == 3:
        num2 = (input('Número secundário da operação (OCTAL):'))
        decimal02 = int(num2, 8)

    elif opção02_final == 4:
        num2 = (input('Número secundário da operação (HEXADECIMAL):'))
        decimal02 = int(num2, 16)

    # chosing the numeric base of the end result
    print('''Determine em qual base a resposta deve ser apresentada:
        [ 1 ] Binário
        [ 2 ] Decimal
        [ 3 ] Octal
        [ 4 ] Hexadecimal''')
    resposta = int(input('Sua escolha: '))

    # both operations are performed with numbers in decimal base.
    if operação02 == 1:
        soma_sub = decimal01 + decimal02

    if operação02 == 2:
        soma_sub = decimal01 - decimal02

    # after the operations are finished, the result is converted to the numeric base chosen by the user.
    if operação02 == 1 and resposta == 1:
        print('Resultado em BINÁRIO: {}'.format(bin(soma_sub)[2:]))
    elif operação02 == 1 and resposta == 2:
        print('Resultado em DECIMAL: {}'.format(soma_sub))
    elif operação02 == 1 and resposta == 3:
        print('Resultado em OCTAL: {}'.format(oct(soma_sub)[2:]))
    elif operação02 == 1 and resposta == 4:
        print('Resultado em HEXADECIMAL: {}'.format(hex(soma_sub)[2:]))

    elif operação02 == 2 and resposta == 1:
        print('Resultado em BINÁRIO: {}'.format(bin(soma_sub)[2:]))
    elif operação02 == 2 and resposta == 2:
        print('Resultado em DECIMAL: {}'.format(soma_sub))
    elif operação02 == 2 and resposta == 3:
        print('Resultado em OCTAL: {}'.format(oct(soma_sub)[2:]))
    elif operação02 == 2 and resposta == 4:
        print('Resultado em HEXADECIMAL: {}'.format(hex(soma_sub)[2:]))

    print('Operação concluída com sucesso!')

else:
    exit()






