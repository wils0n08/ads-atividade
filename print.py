print("olá mundo")

#questão 1

número = 2
  if número > 0:
    print(negativo)
  elif número < 0:
    print(positivo)
  else:
    print (zero)
    
#questão 2 

número = 2 
dobro = número * 2
print("o dobro do valor é:", dobro)

#questão 3

valor = 2 
print("valor digitado:", valor)
print("tipo de variável:",:type(valor))

#questão 4 

número = 2 
  if número % 2==0:
    print("par")
  else:
    print("impar")
    
#questão 5 

número = 2     
triplo = * 3       # numero * 3 → calcula o triplo
print("o triplo do valor é:" triplo)    #print("texto", variavel) → separa com vírgula

#questão 6

número = 4
número = 6
  if número 4 < 6:
    print(a)
  elif número 6 > 4:
    print( 6 e maior que 4)

#questão 7

numero1 = 5
numero2 = 8

if numero1 > numero2:
    print("O maior número é:", numero1) #if / elif → compara os números
elif numero2 > numero1:
    print("O maior número é:", numero2) # else → caso sejam iguais
else:
    print("Os dois números são iguais")
    
#questão 8

numero = 0
if numero >= 0:    #numero >= 0 → aceita zero e números positivos
    raiz = numero ** 0.5. #numero ** 0.5 → calcula a raiz quadrada
    print("Raiz aproximada:", raiz) 
else:
    print("Número inválido") #else → mostra “Número inválido” se for negativo
    
#questão 9 

valor = 0 
metade = valor / 2  #Em Python, só usamos espaço no início quando estamos dentro de if.
 
  print("a metade do valor é:", metade)

#questão 10 

numero = 0

if numero >= 0 and numero <= 10:
    print("Dentro do intervalo")
else:
    print("Fora do intervalo")
    
#questão 11

numero = int(input("Digite um número: ")) #numero % 2 == 0 → verifica se é par

if numero % 2 == 0 and numero > 0:     #else → qualquer número que não for par → ímpar
    print("Par positivo")
elif numero % 2 == 0 and numero < 0:
    print("Par negativo")
else:
    print("Ímpar")
    
#questão 12

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

soma = n1 + n2
print("Soma:", soma).         

if n1 > n2:
    print("O maior número é:", n1)
elif n2 > n1:
    print("O maior número é:", n2)
else:
    print("Os dois números são iguais")
    
#n1 + n2 → calcula a soma
#if n1 > n2 → verifica se o primeiro é maior
#elif → testa a segunda condição
#else → se nenhum for maior, então são iguais


#1questão 13

numero = int(input("Digite um número: "))

if numero > 100:
    print("Metade:", numero / 2)
else:
    print("Dobro:", numero * 2)
    
#Se o número for maior que 100 → divide por 2
#Senão (else) → multiplica por 2

#questão 14

valor = int(input("Digite um valor: "))

if valor % 3 == 0:
    print("Múltiplo de 3")
else:
    print("Não é múltiplo de 3")
    
#% → pega o resto da divisão
#Se o resto for 0 → é múltiplo de 3
#Senão → não é

#questão 15 

numero = int(input("Digite um número: "))

if numero >= 10 and numero <= 20:
    print("Dentro")
else:
    print("Fora")
    
#>= 10 → maior ou igual a 10
#<= 20 → menor ou igual a 20
#and → precisa atender as duas condições
#Se não atender → cai no else

#questão 17
 
idade = int(input("Digite sua idade: "))

if idade < 18:
    print("Menor de idade")
elif idade <= 59:
    print("Adulto")
else:
    print("Idoso")
    
#•	< 18 → menor de idade
#•	18 até 59 → adulto
#•	60+ → idoso
#•	O elif idade <= 59 funciona porque já passou pelo < 1


#questão 18 

numero = int(input("Digite um número: "))

if numero == 0:
    print("Neutro")
elif numero % 2 == 0 and numero > 0:
    print("Par positivo")
elif numero % 2 == 0 and numero < 0:
    print("Par negativo")
elif numero % 2 != 0 and numero > 0:
    print("Ímpar positivo")
else:
    print("Ímpar negativo")
    
    
 #questão 19


n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 == n2:
    print("Os números são iguais")
else:
    print("Os números são diferentes")
    diferenca = abs(n1 - n2)
    print("Diferença:", diferenca)
    
#== →  compara se são iguais
#abs() → garante que a diferença seja positiva
#Só calcula a diferença se forem diferentes

#questão 20 

valor = int(input("Digite um valor: "))

if valor >= 0 and valor <= 100:
    print("Está dentro do intervalo")
else:
    print("Fora do intervalo. Valor digitado:", valor)
    
#Primeiro casos especiais (ex: zero)
#Depois combinações (par + positivo)
#Por último o else







    



    
    
