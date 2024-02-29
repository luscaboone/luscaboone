#mostrar alo mundo na tela
print('Ola Mundo!')
#pedir para o usuario digitar um numero e entao imprimir na tela o numero digitado
numero = int(input('Digite um numero: '))
print("Seu numero digitado foi: ", numero)
#conta de soma basica
numero01 = int(input('Digite o Primeiro numero da soma: '))
numero02 = int(input('Agora digite o Segundo numero da soma: '))
soma = numero01 + numero02
print(f'A soma dos dois numeros digitados: {soma}')
#media das notas bimestrais
bimestre01 = int(input('Informe a sua nota no primeiro bimestre: '))
bimestre02 = int(input('Agora informe sua nota do segundo bimestre: '))
media = (bimestre01 + bimestre02)/2
print(f"Sua media nos bimestre foi de: {media}")
#classificaccaco das funcoes, int, string, float e tambem tem outros como lsits, tuples, dict, sets, bool, none e class.
string = 'ola mundo'
inteiro = int(50)
float = 3.75
print(f'{string} {type(string)} minha classificacao e: string.\n{inteiro} {type(inteiro)} minha classificacao e: int.\n{float} {type(float)} minha classificacao e: float')
# tabuada
tabuada = int(input('Digite o numero que voce queira saber a tabuada: '))
calculo01,calculo02,calculo03,calculo04,calculo05,calculo06,calculo07,calculo08,calculo09,calculo10 = (tabuada)*1,(tabuada)*2,(tabuada)*3,(tabuada)*4,(tabuada)*5,(tabuada)*6,(tabuada)*7,(tabuada)*8,(tabuada)*9,(tabuada)*10
print(f'A tabuada ate o numero 10 de {tabuada} sera!\n{tabuada}X1={calculo01}\n{tabuada}X2={calculo02}\n{tabuada}X3={calculo03}\n{tabuada}X4={calculo04}\n{tabuada}x5={calculo05}\n{tabuada}X6={calculo06}\n{tabuada}X7={calculo07}\n{tabuada}X8={calculo08}\n{tabuada}x9={calculo09}\n{tabuada}X10={calculo10}')
#calculadora basica
primeironumero = int(input('digite um numero: '))
segundonumero = int(input('digite outro numero: '))
print(primeironumero, segundonumero)
soma2 = primeironumero + segundonumero
diferenca = primeironumero - segundonumero
multiplicacao = primeironumero * segundonumero
divisao = primeironumero / segundonumero
quociente = primeironumero // segundonumero
resto = primeironumero % segundonumero
expoente = primeironumero ** segundonumero