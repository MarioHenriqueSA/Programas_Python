dia,mes,ano = input().split("/")
dia = int(dia)
mes = int(mes)
ano = int(ano)

print('{:02d}/{:02d}/{}, estas informações estão corretas, se sim, escreva "Sim",se não escreva "Não" \nOs dados estão corretos : '.format(dia,mes,ano))
res = str(input())

if res == "Sim":
    print('Tudo bem, Seu acesso será liberado em instantes')
elif res == "Não":
    print('Por gentileza Informe de maneira correta a data de seu nascimento')
else:
    print('Por gentileza, escreva somente "Sim" ou "Não"')

# Explicação sobre o : {:02d}
# ' : ', inicio da formatação
# ' 02 ', comprimento minimo
# ' d ', numero inteiro (decimal), caso não coloque pode ser que dê um erro