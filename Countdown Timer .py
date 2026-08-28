import time

my_time = int(input("Masukkan angka untuk waktu:"))

#for x in range (0,my_time):
#for x in reversed(range(0, my_time)):

#for x in range(my_time, 0,-1):
#    print(x)
#    time.sleep(1)

#digital clock

for x in range(my_time, 0, -1):
    second = x % 60
    minutes = int(x/60) % 60 
    hours   = int(x/360)
    print(f"{hours:02}:{minutes:02}:{second:02}")
    time.sleep(1)

print("Times up")