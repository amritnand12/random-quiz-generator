import tkinter
import datetime


class Countdown(tkinter.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.create_widgets()
        self.show_widgets()
        self.seconds_left=0
        self._timer_on=False

    def show_widgets(self):
        self.label.pack()

    def create_widgets(self):
        self.label = tkinter.Label(self,text="00:00:00")
        self.entry = 300

    def countdown(self):
        self.label['text']=self.convert_seconds_left_to_time()
        if self.seconds_left:
            self.seconds_left-=1
            self._timer_on=self.after(1000,self.countdown)
        else:
            self._timer_on=False

    def start_button(self):
        self.seconds_left=int(self.entry)
        self.stop_timer()
        self.countdown()

    def stop_timer(self):
        if self._timer_on:
            self.after_cancel(self._timer_on)
            self._timer_on=False

    def convert_seconds_left_to_time(self):
        return datetime.timedelta(seconds=self.seconds_left)

