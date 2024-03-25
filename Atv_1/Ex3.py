'''
Uma família fez uma viagem de carro e quer detalhes sobre o desempenho do veículo. 
Faça um programa que pergunta: o momento inicial da partida (hora e minuto), o momento de chegada 
(hora e minuto), o número de segundos parados para descanso, o número de litros de combustível gasto 
(em l), o preço do litro de combustível (em R$) e a distância percorrida (em Km); 
Após receber os dados, o programa informa dados típicos de um computador de bordo: 
a) o tempo de viagem (em segundos)
b) a velocidade média (Km/h) global e a velocidade média em movimento (Km/h) 
c) o custo da viagem com combustível (em R$)
d) o desempenho do carro (em Km/l, l/h e R$/Km).
1 H ---> 60 M
0.12 ----> x
'''

T_H_Inicial = int(input('Informe o tempo de partida(Horas):'))
T_M_Inicial = int(input('Informe o tempo de partida(Minutos):'))
T_H_Final = int(input('Informe o tempo de chegada(Horas):'))
T_M_Final = int(input('Informe o tempo de chegada(Minutos):'))
Combustivel = float(input('Informe o preço do combustível:(R$)'))
Litro = float(input('Litros de combustível usado:'))
Distancia = float(input('Informe a distância percorrida:'))
'''
8:30 --> 2:30
'''
if Combustivel > 0 and Litro > 0 and Distancia > 0:
    print('--------------------------------------------------------------------------')
    T_Inicial = (T_H_Inicial * 3600) + (T_M_Inicial * 60)
    T_Final = (T_H_Final * 3600) + (T_M_Final * 60) 
    tempo_viagem = 0
    if T_H_Final < T_H_Inicial:
       tempo_viagem +=(24 - T_H_Inicial) * 3600
       print(tempo_viagem)
    if T_M_Final < T_M_Inicial:
        tempo_viagem += (60 - T_M_Inicial) * 60
        print(tempo_viagem)
    print(tempo_viagem)
    aux = tempo_viagem
    tempo_viagem = aux + (T_Final - T_Inicial)
    print(tempo_viagem)
    print(f'O tempo de viagem é:{tempo_viagem} segundos')

    Vm_global= Distancia/((T_Final + T_Inicial)/3600)
    Vm_movimento = Distancia/(T_H_Final/3600)
    print(f'Velocidade média global: {Vm_global:0.2f} KM/H, velocidade média em movimento: {Vm_movimento:0.2f} KM/H')

    custo = Combustivel * Litro
    print(f'O custo foi: R$ {custo}')
    
    H_viagem = tempo_viagem / 3600
    KM_L =  Distancia/Litro
    L_H = Litro/H_viagem
    R_KM = custo/Distancia
    print(f'Os desempenhos são: {KM_L:0.2f} Km/l, {L_H:0.2f} l/h e {R_KM:0.2f} R$/Km')
    print('--------------------------------------------------------------------------')
