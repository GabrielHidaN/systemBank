import os
import sys
import datetime


'''
x = datetime.datetime.now()

print(x)
'''

saldo = 500
lista_extratos = []


def depositar():
   try:
    deposito = float(input('Digite o Valor que deseja depositar R$ : '))
    print(f'Deposito de R$ {deposito} Realizado com SUCESSO!\n')
   except:
     print('Você deve Digitar um Valor Monetário!')

   global saldo

   saldo = deposito + saldo
   print(f'EXTRATO BANCARIO: \n')
   dataAndHour = datetime.datetime.now()

   extrato = f' Tipo de  Operação : Deposito | Valor Depositado : R$ {deposito} |    Horário da Operação:  {dataAndHour} |  saldo atual : R$ {saldo}'
   global lista_extratos
   lista_extratos.append(extrato)
   print(lista_extratos[-1])

def sacar():
  global saldo

  if saldo > 0:
    numero_de_saques = 0
    LIMITE_SAQUES = 3

    while numero_de_saques < LIMITE_SAQUES:
      try:
        saque = float(input('Digite o Valor que deseja sacar R$: '))
      except:
        print('Você deve Digitar um Valor Monetário!')

      limite = limite >=1 and limite >= 500

      if limite == True:
        saldo = saldo - saque

        print(f'R${saque} Sacado com SUCESSO!\n')

        dataAndHour = datetime.datetime.now()

        print(f'EXTRATO BANCARIO: \n')

        extrato = f' Tipo de  Operação : Saque | Valor Sacado : R$ {saque} |    Horário da Operação:  {dataAndHour} |  saldo atual : R$ {saldo}'

        global lista_extratos

        lista_extratos.append(extrato)
        print(lista_extratos[-1])

        numero_de_saques += 1
      else:
        print(f'Você deve sacar um valor entre R$ 1.00 e R$ 500.00 ')

    if numero_de_saques == LIMITE_SAQUES:
      print('Você atingiu a Quantidade de Saques Diários.')

    if saldo < saque:
      verExtarto = input('''
            Saldo Insuficiente para Concluir a Operação!
            Para Consultar seu Extrato Digite a Tecla [e]''')
      if verExtarto == 'e':
        print(lista_extratos)
  else:
    print('Saldo Insuficiente para completar a Operação.')

menu ='''
[d] Deposito
[s] Saque
[e] Extrato
[q] Sair

=>
'''

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
    print(lista_extratos)
  elif opcao == 'q':
    break
  else:
    print('Opção invalida Tente novamente')
