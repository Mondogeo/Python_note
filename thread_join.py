import threading
import time
def mythread (nome, ritardo):
    print(f'Avvio thread {nome} con ritardo di {ritardo}')
    time.sleep(ritardo)
    print('Thread secondario terminato')

if __name__=='main':
    print ('Avvio modulo main')
    #definisco l'oggetto thread
    th==threading.Tread(targhet='mythread', args=(thread2, 2))
    #avvio il thread secondario
    th.start()
    #fermo l esecuzione del main fintanto non sia finito il
    #thread secondario
    print('Main terminato')
    

