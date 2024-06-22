
import os
import random
from random import randint
import string
import time
from time import sleep
import msvcrt
import threading as th
import sys

os.system('cls||clear')

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

delay_print('Vital Message'
            '\n')
      
delay_print('Earth has been at war with an alien race for 270 years.'
            '\n')

      
delay_print('The final battle will be decided on starship movements in the Corina Nebula.'
            '\n')

      
delay_print('As the last surviving code breaker, you must intercept the enemies transmission and relay it to the Inter-Galactic Federation.'
            '\n')

      
delay_print('You have to be fast Ensign. The transmission will come only milliseconds before the Borg ships drop out of faster than light speed.'
            '\n')

      
delay_print('Fortunately, you have already been breifed as to the length of the message.'
            '\n')

      
delay_print('Be Ready, the entire human race depends on your ability to relay this message.'
            '\n')

      
delay_print('Good Luck, and God speed.'
            '\n')

while True:
    d = int(input('How many letters are in the message? (4-10)'))
    if d>= 4 and d<= 10:
        break

m = ''

for i in range(d):
    m += random.choice(string.ascii_lowercase)

os.system('cls||clear')

s = randint(1, 5)
sleep(s)     
delay_print('INCOMING BORG TRANSMISSION!!!')

time.sleep(.75)

print('BORG Starship Position Data:'
      '\n'
      '\n', m )


time.sleep(d/2)

os.system('cls||clear')

correct_answer = m
def settime():
    pass
S = th.Timer(d, settime)  
S.start()  
answer = (input("Enter the trasmission!: "))

if answer == correct_answer and S.is_alive():
    delay_print('You did it ensign!,'
        '\n' 'the war is over.')
elif S.is_alive() == False:
    delay_print('Damn you Ensign!, you took too long!!!'
        '\n' 'Humanity is over thanks to you!!!'
        '\n' 'I hope', m, ' is branded across our chest when you burn in hell!')
else:
    delay_print('Damn you Ensign!,'
        '\n' 'Humanity is over thanks to you!!!'
        '\n' 'I hope', m, 'is branded across our chest when you burn in hell!')
         
S.cancel()


