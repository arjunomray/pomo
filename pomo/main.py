import sys
import time
from helper_methods import clear_screen


def countdown(min):
    sec = min * 60

    while sec:
        clear_screen()
        disp_min = sec // 60
        disp_sec = sec % 60
        print(f"{disp_min:02d}:{disp_sec:02d}")
        #time.sleep(1)
        sec -= 1
    clear_screen()
    print("00:00")


def pomodoro(session_time=25, break_time=5):
    while True:
        count_session = 0
        countdown(session_time)
        count_session += 1
        break_check = input("Start break ? Y/N") 
        if break_check == 'y' or 'Y':
            print("Break Time")
            countdown(break_time)
        session_check =input("Start next session ? Y/N \n")
        if not session_check == 'y' or "Y":
            print(f"Ending session!!!... Worked for {count_session} session(s) ")
            break


if __name__ == "__main__":
    try:
        pomodoro(25,5)

    except KeyboardInterrupt as e:
        print("\nTimer stopped. Bye :)\n")
        sys.exit()
