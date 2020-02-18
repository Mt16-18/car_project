import sys
import os
from time import sleep
#os.system("kill `ps aux | pgrep match`")
print("1")
os.popen("./match 2 2 5.83333 1")
process = os.system("ps aux | pgrep match")
# while(process==None) :
#      print("process = ", process,"\n")
#      os.popen("./match 2 2 5.83333 1")
#      sleep(3)
#      process = os.system("ps aux | pgrep match")
sleep(1000000)
print("2")
os.system("kill `ps aux | pgrep match`")
