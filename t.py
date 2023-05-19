import time
alive = True #@param {type:"boolean"}

temps = 0
sec = 36
while(temps < 4320000):
  if(temps == sec):
    sec += 36
    x = (temps/60)/60
    print("It's been ",x,"  hour...")
  time.sleep(1)
  temps +=1
