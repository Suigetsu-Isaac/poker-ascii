from termcolor import colored

'''
    cor de texto            cor de background
    30 -> branco            40 -> branco    
    31 -> vermelho          41 -> vermelho
    32 -> verde             42 -> verde
    33 -> amarelo           43 -> amarelo
    34 -> azul              44 -> azul
    35 -> Magenta           45 -> Magenta
    36 -> azulinho          46 -> azulinho
    37 -> cinza             47 -> cinza

    0 - none
    1 - bold
    4 - underline
    7 - negative
'''


print(colored('Error Test!!!', 'red'))
print(colored('Warning Test!!!', 'yellow'))
print(colored('Success Test!!!', 'green'))
