#! /usr/bin/env python3
# coding: utf-8

from tkinter import *


class PomodoroTimer(Frame):
    """Display an interface for a Pomodoro Timer"""

    def __init__(self, master):
        super(PomodoroTimer, self).__init__(master)
        self.pack(anchor=CENTER, expand=1, fill=BOTH)
        self.interface()
        self._stop_id = None
        # Start by default for 25 mins
        self._duration = 25*60
        self._paused = False
        self._count_session = 0


    # Display a minimalist GUI with Tkinter library
    def interface(self):
        self.duration = StringVar()
        self.duration.set(None)

        # 4 RadioButtons for options : Focus on 25 mins, Focus on 45 mins, Break for 5 mins or Break for 15 mins.
        self.options_frame = Frame(self, bg="#333333")

        self.focus_25_button = Radiobutton(self.options_frame,text="Focus \n 25 mins",width="10",height='2',
                                           bg="#333333",selectcolor="#3385ff",foreground="white",indicatoron=0,
                                           variable=self.duration,value="focus 25mins",command=self.start_countdown)
        self.focus_25_button.pack(side=LEFT, padx=5, pady=5)

        self.focus_45_button = Radiobutton(self.options_frame,text="Focus \n 45 mins",width="10",height='2',
                                           bg="#333333",selectcolor="#3385ff",foreground="white",indicatoron=0,
                                           variable=self.duration,value="focus 45mins",command=self.start_countdown)
        self.focus_45_button.pack(side=LEFT, padx=5, pady=5)

        self.break_5_button = Radiobutton(self.options_frame,text="Break \n 5 mins",width="10",height='2',
                                           bg="#333333",selectcolor="#3385ff",foreground="white",indicatoron=0,
                                           variable=self.duration,value="break 5mins",command=self.start_countdown)
        self.break_5_button.pack(side=LEFT, padx=5, pady=5)

        self.break_15_button = Radiobutton(self.options_frame,text="Break \n 15 mins",width="10",height='2',
                                           bg="#333333",selectcolor="#3385ff",foreground="white",indicatoron=0,
                                           variable=self.duration,value="break 15mins",command=self.start_countdown)
        self.break_15_button.pack(side=LEFT, padx=5, pady=5)

        self.options_frame.pack(side=TOP)


        # Label for the countdown
        self.timer_label = Label(self, text="25:00", font=("Cantrell",70), bg="#333333", fg="#3385ff")
        self.timer_label.pack(side=TOP, pady=5)


        # Buttons for actions : Start, Stop, Reset or Quit
        self.actions_frame = Frame(self, bg="#333333")

        self.start_button = Button(self.actions_frame,text="Start",highlightbackground="#3385ff",
                                   activeforeground="white",width="10",height="2",command=self.start_action)
        self.start_button.pack(side=LEFT, padx=5, pady=5)

        self.stop_button = Button(self.actions_frame,text="Stop",highlightbackground="#3385ff",
                                   activeforeground="white",width="10",height="2",command=self.stop_action)
        self.stop_button.pack(side=LEFT, padx=5, pady=5)

        self.reset_button = Button(self.actions_frame,text="Reset",highlightbackground="#3385ff",
                                   activeforeground="white",width="10",height="2",command=self.reset_action)
        self.reset_button.pack(side=LEFT, padx=5, pady=5)

        self.quit_button = Button(self.actions_frame,text="Close",highlightbackground="#3385ff",
                                   activeforeground="white",width="10",height="2",command=window.destroy)
        self.quit_button.pack(side=LEFT, padx=5, pady=5)

        self.actions_frame.pack(side=BOTTOM)



    # Prepare the countdown timer for the requested time.
    def start_countdown(self):
        options = self.duration.get()
        if options == "focus 25mins":
            self.countdown_ready(1500)

        elif options == "focus 45mins":
            self.countdown_ready(2700)

        elif options == "break 5mins":
            self.countdown_ready(300)

        elif options == "break 15mins":
            self.countdown_ready(900)


    def countdown_ready(self, duration):
        if self._stop_id is not None:
            self.master.after_cancel(self._stop_id)
        self._paused = False
        self.countdown(duration)
        self._paused = True


    # Start the countdown for the requested time
    def start_action(self):
        self._paused = False
        if self._stop_id is None:
            self.countdown(self._duration)

    # Stop the countdown
    def stop_action(self):
        if self._stop_id is not None:
            self._paused = True

    # Reset the countdown for the previous requested time
    def reset_action(self):
        self.master.after_cancel(self._stop_id)
        self._stop_id = None
        self._paused = False
        self.countdown(self._duration)
        self._paused = True

    # Display a countdown in the form 00:00.
    def countdown(self, time_seconds, start=True):
        if time_seconds >= 0 :
            if start:
                self._duration = time_seconds
            if self._paused:
                self._stop_id = self.master.after(1000, self.countdown, time_seconds, False)
            else:
                mins, secs = divmod(time_seconds, 60)
                timeFormat = "{:02d}:{:02d}".format(mins, secs)

                timer.timer_label.configure(text=timeFormat)
                self._stop_id = self.master.after(1000, self.countdown, time_seconds - 1, False)
        # When the time is out
        else:
            # Count sessions only for focus sessions, not the break
            if self._duration > 1000:
                print("Pomodoro Timer finished !")

                # Increase by an increment of one for each session completed
                self._count_session += 1
                print("Number of session achieved: " + str(self._count_session) + "\a")
            else:
                print("Break is finished ! \a")



if __name__ == "__main__":
    window = Tk()
    window.title("Pomodoro Timer Interface")
    window.resizable(0,0)
    timer = PomodoroTimer(window)
    timer.configure(bg="#333333")
    window.mainloop()

