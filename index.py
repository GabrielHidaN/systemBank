import os
import datetime


menu ='''
[d] Deposito
[s] Saque
[e] Extrato
[q] Sair

=>
'''


saldo = 500
lista_extratos = []
numero_de_saques = 0
LIMITE_SAQUES = 3


def depositar():
   global saldo
   global lista_extratos

   try:
    deposito = float(input('Digite o Valor que deseja depositar R$ : '))
    print(f'Deposito de R$ {deposito} Realizado com SUCESSO!\n')
    saldo = saldo + deposito
    print(f'EXTRATO BANCARIO: \n')
    dataAndHour = datetime.datetime.now()

    extrato = f' Tipo de  Operação : Deposito | Valor Depositado : R$ {deposito} |    Horário da Operação:  {dataAndHour} |  Saldo atual : R$ {saldo}'

    lista_extratos.append(extrato)
    print(lista_extratos[-1])

   except:
     print('Você deve Digitar um Valor Monetário!')
     depositar()



def sacar():
  global saldo
  global lista_extratos

  if saldo > 0:
    global numero_de_saques
    global LIMITE_SAQUES

    if numero_de_saques == LIMITE_SAQUES:
      print('Você atingiu a Quantidade de Saques Diários.\n')
    else:
      while numero_de_saques < LIMITE_SAQUES:
        try:
          saque = float(input('Digite o Valor que deseja sacar R$: \n'))

          limite =  500

          if saldo < saque:
            verExtarto = input('''
              Saldo Insuficiente para Concluir a Operação!
              Para Consultar seu Extrato Digite a Tecla [e]\n''')
            if verExtarto == 'e':
              if len(lista_extratos) == 0:
                print(f' Seu Saldo é : R$ {saldo} ')
              else:
                print(lista_extratos)
              break

          elif saque > 0 and saque <= limite:
            saldo = saldo - saque

            print(f'R${saque} Sacado com SUCESSO!\n')
            numero_de_saques = numero_de_saques + 1

            dataAndHour = datetime.datetime.now()

            print(f'EXTRATO BANCARIO: \n')

            extrato = f' Tipo de  Operação : Saque | Valor Sacado : R$  {saque} |      Horário da Operação:  {dataAndHour} |  Saldo atual :  R$ {saldo} '



            lista_extratos.append(extrato)
            print(lista_extratos[-1])
            break
          else:
            print(f'Você deve sacar um valor entre R$ 1.00 e R$ 500.00 ')
            break


        except:
          print('Você deve Digitar um Valor Monetário!\n')
          sacar()

  else:
    print('Saldo Insuficiente para completar a Operação.\n')


while True:

  opcao = input(menu)

  if opcao == 'd':
    os.system('cls')
    depositar()

  elif opcao == 's':
    os.system('cls')
    sacar()

  elif opcao == 'e':
    os.system('cls')
    if len(lista_extratos) == 0:
      print(f' Seu Saldo é : R$ {saldo} ')
    else:
      i = 0
      tamanhoLista = len(lista_extratos)
      for extrato in range(tamanhoLista):
        print(lista_extratos[extrato])
        i +=1
  elif opcao == 'q':
    break
  else:
    print('Opção invalida Tente novamente')
