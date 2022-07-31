print('''Qual operação deverá ser realizada? 
{ 1 } - Conversão de bases
{ 2 } - Soma ou Subtração''')
operação = int(input('Operação escolhida: '))
# menu para determinar a operação que será feita.
if operação < 1 or operação > 2:
    print('Operação Inválida. Tente Novamente')


# menu para determinar as bases envolvidas na conversão.
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


    # bloco de comando tendo a base binária como referência.
    # realiza todas as possíveis conversões com esta base.
    if opção == 1:
        num = (input('Digite o número binário a ser convertido: '))
        decimal = int(num, 2)
        # converte o número em questão para base decimal.
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



    # bloco de comando tendo a base decimal como referência.
    # realiza todas as possíveis conversões com esta base.
    # pelo fato de se estar trabalhando com base decimal, não é necesário converter nada previamente.
    if opção == 2:
        num = int(input('Digite o número decimal a ser convertido: '))
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



    # bloco de comando tendo a base octal como referência.
    # realiza todas as possíveis conversões com esta base.
    if opção == 3:
        num = (input('Digite o número octal a ser convertido: '))
        decimal = int(num, 8)
        # converte o número em questão para base decimal.
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


    # bloco de comando tendo a base hexadecimal como referência.
    # realiza todas as possíveis conversões com esta base.
    if opção == 4:
        num = (input('Digite o número hexadecimal a ser convertido: '))
        decimal = int(num, 16)
        # converte o número em questão para base decimal.
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


# menu para escolher qual das operações será feita.
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


    # entrada dos números para as operações.
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
    # ao obter os números operantes, eles são convertidos para base decimal.


    print('''Determine em qual base a resposta deve ser apresentada:
        [ 1 ] Binário
        [ 2 ] Decimal
        [ 3 ] Octal
        [ 4 ] Hexadecimal''')
    resposta = int(input('Sua escolha: '))

    # ambas as operações são realizadas com os números em base decimal.
    if operação02 == 1:
        soma_sub = decimal01 + decimal02

    if operação02 == 2:
        soma_sub = decimal01 - decimal02
    # após o término das operações, o resultado é convertido para a base escolhida pelo usuário.

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






