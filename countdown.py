import time

def countdown(t):
    while t:
        min , secs = divmod(t,60)
        tiempo = '{:02d}:{:02d}'.format(min,secs)
        print(tiempo, end="\r")
        time.sleep(1)
        t -= 1
    print('Se acabo el tiempo')

t = input("Ingrese la cuenta atras: ")

countdown(int(t))