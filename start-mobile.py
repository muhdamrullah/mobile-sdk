import subprocess
import time
import sys, signal

def signal_handler(signal, frame):
    print("\nProgram is exiting gracefully")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

while True:
    subprocess.call('sudo airodump-ng wlan0 -w dump &', shell=True)
    for x in range(0,9):
        subprocess.call('python post_api.py', shell=True)
        time.sleep(30)
    subprocess.call('sudo pkill airodump-ng', shell=True)
    time.sleep(1)
