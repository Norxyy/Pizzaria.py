print(' Seja bem vindo(a) à Vergara Pizzaria de Murilo Vergara    ')
print('|_______________________CARDÁPIO_______________________|')
print('| Código |   Descrição     |Pizza Média   |Pizza Grande|')
print('|  21    |   Napolitana    |R$ 20,00      | R$ 26,00   |')
print('|  22    |   Margherita    |R$ 20,00      | R$ 26,00   |')
print('|  23    |   Calabresa     |R$ 25,00      | R$ 32,50   |')
print('|  24    |   Toscana       |R$ 30,00      | R$ 39,00   |')
print('|  25    |   Portuguesa    |R$ 30,00      | R$ 39,00   |')
print('+------------------------------------------------------+')

#  Variáveis
num_pizza = 1
c_pizza = True
q_pizza_M = 0
v_pizza_M = 0
valor_t_pizza_M = 0
q_pizza_G = 0
v_pizza_G = 0
valor_t_pizza_G = 0
cod_pizza = 0
valor_cobrado = 0
n_pizza = ''

#  Estrutura de repetição
while (c_pizza == True):
    tamanho_pizza = input('Por favor nos informe o tamanho da sua pizza (M/G): ')
    if (tamanho_pizza == 'M'):
        q_pizza_M += 1
    elif (tamanho_pizza == 'G'):
        q_pizza_G += 1
    else:
        print('Tamanho incorreto. Favor tente novamente. :)')
        continue

        # Valor do codigo da pizza escolhida.
    cod_pizza = int(input('Por favor nos informe o Código da sua pizza: '))

    #  Codigo de cada pizza conforme o cardapio
    if (cod_pizza == 21 and tamanho_pizza == 'M'):
        n_pizza = 'Napolitana'
        valor_t_pizza_M += 20
    elif (cod_pizza == 21 and tamanho_pizza == 'G'):
        n_pizza = 'Napolitana'
        valor_t_pizza_G += 26
    elif (cod_pizza == 22 and tamanho_pizza == 'M'):
        n_pizza = 'Margherita'
        valor_t_pizza_M += 20
    elif (cod_pizza == 22 and tamanho_pizza == 'G'):
        n_pizza = 'Margherita'
        valor_t_pizza_G += 26
    elif (cod_pizza == 23 and tamanho_pizza == 'M'):
        n_pizza = 'Calabresa'
        valor_t_pizza_M += 25
    elif (cod_pizza == 23 and tamanho_pizza == 'G'):
        n_pizza = 'Calabresa'
        valor_t_pizza_G += 32
    elif (cod_pizza == 24 and tamanho_pizza == 'M'):
        n_pizza = 'Toscana'
        valor_t_pizza_M += 30
    elif (cod_pizza == 24 and tamanho_pizza == 'G'):
        n_pizza = 'Toscana'
        valor_t_pizza_G += 39
    elif (cod_pizza == 25 and tamanho_pizza == 'M'):
        n_pizza = 'Portuguesa'
        valor_t_pizza_M += 30
    elif (cod_pizza == 25 and tamanho_pizza == 'G'):
        n_pizza = 'Portuguesa'
        valor_t_pizza_G += 39
    else:
        print('Código inválido. Tente novamente.')
        if (tamanho_pizza == 'M'):
            q_pizza_M -= 1
        else:
            q_pizza_G -= 1
        continue
    print('Cliente pediu uma pizza {}.\n'.format(n_pizza))
    # Caso queira outra pizza
    outra_pizza = input(('O Sr(a) deseja fazer outro pedido ? (S/N): '))
    if (outra_pizza == 'S'):
        continue
    else:
        print('_________________________________________________________________')
        print('OBRIGADO PELA COMPRA :)')
        # Total de pizza M.
        if (q_pizza_M > 0):
            print('Quantidade de pizzas tamanho M: {}'.format(q_pizza_M))
            print('Valor total de pizzas tamanho M: {:.2f}'.format(valor_t_pizza_M))
            # Total de pizza G.
        if (q_pizza_G > 0):
            print('Quantidade de pizzas tamanho G: {}'.format(q_pizza_G))
            print('Valor total de pizzas tamanho G: R$ {:.2f}'.format(valor_t_pizza_G))
        print('__________________________________________________________________')
        # Valor total a ser pago.
        valor_cobrado = valor_t_pizza_M + valor_t_pizza_G
        print('Total a pagar: R$ {:.2f}'.format(valor_cobrado))
        print('Obrigado pela compra volte sempre :)')
        break
