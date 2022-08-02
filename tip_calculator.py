print('Welcome to tip calculator:')

total= input('Qual o valor total da conta $:')

porcentagem= input('Quantos por cento cada pessoa ira pagar da conta? 10, 15 ,12: ')

pessoas=input('quantas pessoas vão dividir a conta ?')

total_int= float(total)
porcentagem_int=int(porcentagem)
pessoas_int=int(pessoas)


porcentagem_conv = porcentagem_int /100
valor_total=total_int*porcentagem_conv
valor_com_desc=total_int+valor_total
conta_por_pessoa=valor_com_desc/pessoas_int
valor_final=round(conta_por_pessoa,2)  


mensagem=f'Cada pessoa ira pagar: {valor_final}'
print(''+mensagem)