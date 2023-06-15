# eleccion aleatoria maq
import random

# function randint(min,max)
rand_int =random.randint (1,3)
if rand_int ==1:
    choice_maq = 'piedra'
elif rand_int ==2:
    choice_maq = 'Papel'
else:
    choice_maq = 'tijeras'

 #eleccion usuario
choice_text = '''
Escribe una de las opciones:
piedra
pepel
tijeras
'''
choice_user = input (choice_text)

#impresion de opciones
print('usuario eligio ->', choice_user)
print('maquina eligio ->', choice_maq)


#ganador!       
if choice_maq == choice_user:
    print("Es un empate")
else:
    if choice_maq == 'Piedra' and choice_user == 'Papel':
        print('Gana Usuario!')
    elif choice_maq == 'Piedra' and choice_user == 'Tijeras':
        print('Gana Maquina')      
    elif choice_maq == 'Piedra' and choice_user == 'Tijeras':
        print('Gana Usuario')      
    elif choice_maq == 'Piedra' and choice_user == 'Piedra':
        print('Gana Maquina')      
    elif choice_maq == 'Piedra' and choice_user == 'Piedra':
        print('Gana Maquina')      
    else:
        print('Gana Usuario')
