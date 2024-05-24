from random import randint
from time import sleep
import emoji

a = randint(0,5)
print('-=-'*20)
r = input('Vamos Jogar um jogo?(S/N) ').strip().upper()
print('-=-'*20)

if r == 'S' or r == 'SIM':
    print('Vou pensar em um número tente adivinhar🤓!')
    print('PROCESSANDO...')
    sleep(3)
    n = int(input('Me fale um número de 1 a 5: '))
    if n == a:
        print(emoji.emojize('PARABENS!!! VOCÊ \033[32mVENCEU!\033[m :beaming_face_with_smiling_eyes:'))
    else:
        print(emoji.emojize('Você \033[31mPERDEU!\033[m Eu pensei no número {}... \033[4;37;41mO mundo será dominado!\033[m:loudly_crying_face:'.format(a)))
elif r == 'N' or r == 'NAO' or r =='NÃO':
    print(emoji.emojize('Que pena...Fica para proxima então! :angry_face_with_horns:'))

else:
    print('=-=-;'*20)
    print("""Por favor... 
Coloque uma resposta valida! 
 é apenas SIM ou NÃO!!!!!!""")



