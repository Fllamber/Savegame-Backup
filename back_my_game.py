from datetime import datetime
#from locale import setlocale
from locale import LC_ALL
from sched import scheduler
from time import time
from time import sleep
from subprocess import Popen
from subprocess import STDOUT
from subprocess import PIPE

# Set The Locale for your machine
# This is for reading stdout from the compression
# setlocale(LC_ALL, '<YOUR LOCALE>')

# Prepare the scheduler
s = scheduler(time, sleep)

# specify wich program will compress
zip_path = "C:\\Program Files\\7-Zip\\7z.exe"

# Your Savegame Path, CHANGE IT!
game_path = "C:\\Users\\<USER>\\<GAME>\\Saves\\"

# Where will you store the savefile? CHANGE IT!
game_store = "C:\\Users\\<USER>\\<BACKUP PATH>"

# Specify the individual FOLDER of the save.
save = "< The name of the save to bakcup>" 
full_save = game_path + "\\" + save


# Return Current Time
def get_time():
    return datetime.now().strftime("%H-%M-%S")


# Return full file name to store
def file_name_store():
    return game_store + "\\" + save + "_" + get_time()


# main compression function
def compress():
    cmd = [zip_path, 'a', '-t7z',  file_name_store() + ".7z", full_save, '-mx9']
    sp = Popen(cmd, stderr=STDOUT, stdout=PIPE)
    # stdout = sp.communicate()[0]
    # print('STDOUT:{}'.format(stdout.decode("UTF-8")))
    s.enter(seconds, 1, compress)

#First Time

time_min = 5  # minutes
seconds = time_min * 60  # seconds
# print(seconds)
#compress()
s.enter(seconds, 1, compress)
s.run()
