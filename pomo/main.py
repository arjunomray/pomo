import sys
import time
import argparse
from .helper_methods import clear_screen


def countdown(min):
    sec = min * 60

    while sec:
        clear_screen()
        disp_min = sec // 60
        disp_sec = sec % 60
        print(f"{disp_min:02d}:{disp_sec:02d}")
        time.sleep(1)
        sec -= 1
    clear_screen()
    print("00:00")


def pomodoro(session_time=25, break_time=5):
    count_session = 0
    yes = ["y", "Y"]
    while True:
        session_check = input("\nStart session ? Y/N \n")
        if session_check in yes:
            countdown(session_time)
            count_session += 1
        else:
            print(f"\nEnding session!!!... Worked for {count_session} session(s)\n")
            break

        break_check = input("\nStart break ? Y/N\n")
        if break_check in yes:
            print("Break Time")
            countdown(break_time)
        else:
            print(f"\nEnding session!!!... Worked for {count_session} session(s)\n")
            break


def run():
    parser = argparse.ArgumentParser(
        description="A python pomodoro timer for the terminal.",
        usage="pomo --session <time_in_min> --break <time_in_min>",
    )
    parser.add_argument("--session", help="set time for the main sessions (default=25)")

    parser.add_argument("--breaks", help="set time for the breaks (default=5)")
    args = parser.parse_args(sys.argv[1:])

    session = int(args.session) if args.session else 25
    breaks = int(args.breaks) if args.breaks else 5

    pomodoro(session_time=session, break_time=breaks)


def main():
    try:
        run()

    except KeyboardInterrupt:
        print("\nTimer stopped. Bye :)\n")
        sys.exit()

if __name__ == "__main__":
    main()

