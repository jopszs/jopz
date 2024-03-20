original=0
desejada=0
temperatura=0
resultado=0

print ('\nOla, seja bem vindo')
print ('Porgrama para converção de temperatura\n')

while(original<=0 or original>=5):
    print('1)celcius')
    print('2)Fahrenheit')
    print('3)kelvin')
    print('4)Rankine')

    try:
        original=int(input('Qual a unidade original?\n'))
    except: print('\nDigite apenas números inteiros')

    if original <= 0 or original >= 5:
        print('\nValor inválio. Digite novamente.\n\n')
try:
    temperatura=float(input('\n\nDigite a temperatura\n'))
except: print('\nDigite apenas números')


while (desejada <= 0 or desejada >= 5):
    print('\n\n')
    print('1)Celcius')
    print('2)Fahrenheit')
    print('3)Kelvin')
    print('4)Rankine')

    try:
        desejada=int(input('Qual a unidade deseja converter?\n'))
    except: print('\nDigite apenas números inteiros')

    if desejada <= 0 or desejada >= 5:
        print('\nValor inválio. Digite novamente.\n\n')


if(original ==1 and desejada==1):
    print('\n\nNão pode converter de celcius para celcius')

if(original ==1 and desejada==2):
    resultado = (temperatura*1.8)+32
    print('\n\nResultado:',resultado)











