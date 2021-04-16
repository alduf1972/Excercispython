import winsound

frequency = int(input("What frequence you want to beep ?"))
duration = int(input ("What duration will the beep last ?"))
winsound.Beep(frequency, duration)