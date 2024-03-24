'''
O número de dias decorridos entre duas datas é importante em uma infinidade de 
situações da vida cotidiana. Faça um programa que recebe inicialmente dois valores (dia inicial e mês 
inicial), depois mais dois valores (dia final, mês final), ao final deve indicar quantos dias se passaram entre 
as datas (considere que o ano não é bissexto).
Exemplos: 
o 02 de 05 até 03 de 05 - 1 dia
o 27 de 04 até 03 de 05 - 6 dias
o 03 de 02 até 03 de 05 - 79 dias
Não esqueça de verificar se a data inicial é menor ou igual à data final.
Dica: conte o número de dias até cada uma das datas e subtraia esses números.
'''

D_inicial = int(input('Informe o dia inicial:'))
M_inicial = int(input('Informe o mês inicial:'))
D_final = int(input('Informe o dia final:'))
M_final = int(input('Informe o mês final:'))

if D_inicial <= D_final and M_inicial <= M_final:
    Janeiro = 31
    Fevereiro = 28
    Março = 31
    Abril = 30
    Maio = 31
    Junho = 30
    Julho = 31
    Agosto = 31
    Setembro = 30
    Outubro = 31
    Novembro = 30
    Dezembro = 31
    if M_inicial == M_final:
        print(f'Se passaram {D_final - D_inicial} dias')
    elif M_inicial < M_final and M_final == M_inicial + 1:
        if M_inicial == 1:
            dias = 31 - D_inicial + D_final
        elif M_inicial == 2:
            dias = 28 - D_inicial + D_final
        elif M_inicial == 3:
            dias = 31 - D_inicial + D_final
        elif M_inicial == 4:
            dias = 30 - D_inicial + D_final
        elif M_inicial == 5:
            dias = 31 - D_inicial + D_final
        elif M_inicial == 6:
            dias = 30 - D_inicial + D_final
        elif M_inicial == 7:
            dias = 31 - D_inicial + D_final
        elif M_inicial == 8:
            dias = 31 - D_inicial + D_final
        elif M_inicial == 9:
            dias = 30 - D_inicial + D_final
        elif M_inicial == 10:
            dias = 31 - D_inicial + D_final
        elif M_inicial == 11:
            dias = 30 - D_inicial + D_final
        elif M_inicial == 12:
            dias = 31 - D_inicial + D_final
    elif M_inicial < M_final and M_final == M_inicial + 2:
        if M_inicial == 1:
            dias = 31 - D_inicial + D_final
        elif M_inicial == 2:
            dias = 28 - D_inicial + D_final
        elif M_inicial == 3:
            dias = 31 - D_inicial + D_final
        elif M_inicial == 4:
            dias = 30 - D_inicial + D_final
        elif M_inicial == 5:
            dias = 31 - D_inicial + D_final
        elif M_inicial == 6:
            dias = 30 - D_inicial + D_final
        elif M_inicial == 7:
            dias = 31 - D_inicial + D_final
        elif M_inicial == 8:
            dias = 31 - D_inicial + D_final
        elif M_inicial == 9:
            dias = 30 - D_inicial + D_final
        elif M_inicial == 10:
            dias = 31 - D_inicial + D_final
        elif M_inicial == 11:
            dias = 30 - D_inicial + D_final
        elif M_inicial == 12:
            dias = 31 - D_inicial + D_final
    elif M_inicial < M_final and M_final == M_inicial + 3:
        if M_inicial == 1:
            dias = 31 - D_inicial + D_final
        elif M_inicial == 2:
            dias = 28 - D_inicial + D_final
        elif M_inicial == 3:
            dias = 31 - D_inicial + D_final
        elif M_inicial == 4:
            dias = 30 - D_inicial + D_final
        elif M_inicial == 5:
            dias = 31 - D_inicial + D_final
        elif M_inicial == 6:
            dias = 30 - D_inicial + D_final
        elif M_inicial == 7:
            dias = 31 - D_inicial + D_final
        elif M_inicial == 8:
            dias = 31 - D_inicial + D_final
        elif M_inicial == 9:
            dias = 30 - D_inicial + D_final
        elif M_inicial == 10:
            dias = 31 - D_inicial + D_final
        elif M_inicial == 11:
            dias = 30 - D_inicial + D_final
        elif M_inicial == 12:
            dias = 31 - D_inicial + D_final
    print(f'Se passaram {dias} dias')
        