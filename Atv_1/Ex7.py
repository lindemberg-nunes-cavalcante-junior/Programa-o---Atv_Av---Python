'''
Desenvolva um código em Python que solicite ao usuário que informe os comprimentos dos três lados de 
um triângulo. Em seguida, verifique se esses comprimentos podem formar um triângulo. Caso afirmativo, 
calcule e informe os valores dos ângulos do triângulo e classifique-o quanto aos lados e aos ângulos.
• Instruções:
(feito)a) Peça ao usuário para inserir os comprimentos dos três lados do triângulo.

(feito)b) Verifique se os comprimentos fornecidos podem formar um triângulo. Caso contrário, informe 
que não é possível formar um triângulo com esses lados.

(feito)c) Se for possível formar um triângulo, calcule os três ângulos do triângulo.

(feito)d) Classifique o triângulo quanto aos lados (equilátero, isósceles ou escaleno) e aos ângulos 
(agudo, obtuso ou retângulo).

(Feito)e) Exiba a classificação do triângulo quanto aos lados e aos ângulos.
• Observações:
(feito)o Para determinar se os lados fornecidos pelo usuário podem formar um triângulo, é necessário 
verificar a seguinte condição: A soma de quaisquer dois lados de um triângulo deve ser 
sempre maior que o terceiro lado.

o Você pode usar a Lei dos cossenos para calcular os ângulos de um triângulo.

(feito)o Para classificar quanto aos lados, verifique se os três lados são iguais (equilátero), se dois 
lados são iguais (isósceles) ou se todos os lados são diferentes (escaleno).

o Para classificar quanto aos ângulos, verifique se um dos ângulos é maior que 90 graus 
(obtuso), se um dos ângulos é igual a 90 graus (retângulo) ou se todos os ângulos são 
menores que 90 graus (agudo).

o Considere que os ângulos são expressos em graus.
Desenvolva o código em Python para atender às especificações acima
'''
import math
import sys

L_1 = float(input('Informe um dos lado:'))
L_2 = float(input('Informe mais um lado:'))
L_3 = float(input('Informe o último lado:'))

if L_1 + L_2 <= L_3 or L_1 + L_3 <= L_2 or L_2 + L_3 <= L_1:
    print("Esses lados não conseguem formar um triângulo, pois a soma de dois lados não é maior que o outro ou é igual ao outro.")
    sys.exit()


if L_1 == L_2 == L_3: # Comparação dos lados
    tipo = 'equilátero'
elif L_1 == L_2 != L_3 or L_1 == L_3 != L_2 or L_2 == L_3 != L_1:
    tipo = 'isósceles'
else:
    tipo = 'escaleno'
    
Ang1 = math.degrees(math.acos((L_1 * L_1 + L_2 * L_2 - L_3 * L_3)/(2 * L_1 * L_2))) # Seguindo a Lei do Cosseno, você acha -cos = acos
Ang2 = math.degrees(math.acos((L_3 * L_3 + L_2 * L_2 - L_1 * L_1)/(2 * L_3 * L_2))) # Então descobre o ângulo
Ang3 = math.degrees(math.acos((L_3 * L_3 + L_1 * L_1 - L_2 * L_2)/(2 * L_3 * L_1)))

if Ang1 > 90 or Ang2 > 90 or Ang3 > 90: # Comparação dos ângulos
    tipo2 = 'obtuso'
elif Ang1 == 90 or Ang2 == 90 or Ang3 == 90:
    tipo2 = 'retângulo'
elif Ang1 < 90 and Ang2 < 90 and Ang3 < 90:
    tipo2 = 'agudo'
    
print(f"Seus ângulos são: {Ang1}, {Ang2} e {Ang3}")
print(f"Seu triângulo pelos lados é {tipo} e pelos ângulos é {tipo2}")