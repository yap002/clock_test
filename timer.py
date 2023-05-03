import time
import winsound

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        m, s = divmod(seconds, 60)
        timer = "{:02d}:{:02d}".format(m, s)
        print("Time remaining: " + timer, end="\r")
        time.sleep(1)
        seconds -= 1

    winsound.Beep(1000, 1000) # Beep sound when timer ends
    print("\nTime's up!")

if __name__ == '__main__':
    minutes = int(input("Enter the duration of focus (in minutes): "))
    focus_timer(minutes)
