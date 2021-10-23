import time, random
import os, sys
import threading as th
import typewriter

class Waiting:
    busy = False

    def start(self):
        c = '|/-\\'
        i = 0
        self.busy = True
        while self.busy:
            print('\r',c[i],end='',flush=True)
            i += 1
            i = i % 4
            time.sleep(0.1)

    def stop(self):
        self.busy = False

tw = typewriter.Typewriter
wait = Waiting()
skor = 0
trial = 0
tot_skor = 0

if sys.platform in ['linux', 'darwin']: os.system('clear') 
else: os.system('cls')
    
tw.print('# Game Tembak')
tw.print('=============\n')

tw.print('Misi: Anda punya 1 kesempatan untuk menembak jatuh musuh yang memasuki zona sasaran tepat pada waktunya.')

while True:
    th_wait = th.Thread(target=wait.start)

    waktu = random.randint(10, 100)/10
    tw.print(f'\nMusuh mendekati zona tembak dalam tempo {waktu:.2f} detik. Enter untuk memulai..',end='')
    input()

    sw_start = time.perf_counter()
    print('Enter untuk menembak..')
    th_wait.start()

    input()

    wait.stop()
    th_wait.join()
    sw_stop = time.perf_counter()
    elapsed = sw_stop - sw_start

    delta = abs(elapsed - waktu)
    skor = max(0, waktu - delta) / waktu * 100

    tw.print(f'Anda menembak pd detik ke {elapsed:.2f} dari target {waktu:.2f}')

    tw.print(f'Skor {skor:.2f}. ', end='')
    trial += 1
    tot_skor += skor
    
    if skor < 50:
        tw.print('Ngawur!')
    elif skor < 75:
        tw.print('Meleset!')
    elif skor < 90:
        tw.print('Kurang akurat')
    elif skor < 95:
        tw.print('Cukup akurat!')
    else:
        tw.print('Sangat akurat!')

    tw.print('Skor rata2', format(tot_skor/trial, '.2f'))

    q = tw.input('\nMain lagi, q keluar ')
    if q and q in 'qQ':
        break
