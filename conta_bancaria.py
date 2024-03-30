
saldo_atual = 500
movimento_extrato_depositos = ""
movimento_extrato_saques = ""
valor_max_para_sacar = 500
qtd_max_de_saques = 0



while True:
    mensagem_inicial = '''

    Seja bem vindo a sua conta bancária
        - Selecione o que deseja fazer -
'''
    print(mensagem_inicial)

    msg_decisao_texto = ''' 
            > Digite 1 para Depositar
            > Digite 2 para Sacar
            > Digite 3 para Checar seu Extrato 
            > Digite 4 para Sair 
    '''
    
    msg_decisao = input(msg_decisao_texto)
    msg_decisao_int = int(msg_decisao)
    
    if msg_decisao_int == 1:
        quantidade_a_depositar = input('Qual a quantidade que você deseja depositar? R$ ')
        quantidade_a_depositar_int = int(quantidade_a_depositar)
        movimento_extrato_depositos.append(quantidade_a_depositar_int)
        saldo_atual += quantidade_a_depositar_int  
        print(f'Valor depositado com sucesso! Seu saldo atual é de R${saldo_atual:.2f}')
        continue

    elif msg_decisao_int == 2:
        if qtd_max_de_saques < 3:
            quantidade_a_sacar = input('Qual a quantidade que você deseja sacar? R$')
            quantidade_a_sacar_int = int(quantidade_a_sacar)
            if quantidade_a_sacar_int > saldo_atual:
                print('O valor solicitado é maior do que o saldo da sua conta!')
                continue
            elif quantidade_a_sacar_int >= valor_max_para_sacar:
                print('O valor solicitado é maior que o limite máximo de saque diário!')
                continue
            else:
                saldo_atual -= quantidade_a_sacar_int
                qtd_max_de_saques += 1
                movimento_extrato_saques.append(quantidade_a_sacar_int)
                print(f'Valor sacado! Seu novo saldo é igual a R${saldo_atual:.2f}')
                continue
        else:
            print('Você chegou no limite de saques da sua conta por hoje!')
            continue

    elif msg_decisao_int == 3:
        msg_extrato = f''' 
            Este é o seu movimento de depósitos: {movimento_extrato_depositos}
            Este é o seu movimento de saques: {movimento_extrato_saques}
            Este é o seu saldo atual: R${saldo_atual:.2f}
'''
        print(msg_extrato)
        continue
    elif msg_decisao_int == 4:
        break
    else:
        print('[ATENÇÃO] Você digitou errado. Tente novamente!')
        continue

    

    
    break
