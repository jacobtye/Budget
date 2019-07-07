#!/usr/bin/python
from Tkinter import *
from ttk import *
import tkMessageBox
import threading
import cv2
import numpy as np
import sys
import os
import time
import multiprocessing
import signal


class ControlPanel:
    def __init__(self):
        self.master = Tk()
        self.master.style = Style()
        # ('clam', 'alt', 'default', 'classic')
        self.master.style.theme_use("classic")
        self.master.style.configure(
            "TButton", relief="raised", font=("bookman", 10))
        self.master.title("Budget")
        self.open_video_threads = []
        self.open_arm_threads = []
        self.open_gripper_threads = []
        self.open_head_threads = []
        self.run_event = threading.Event()
        self.run_event.set()
        self.updateAngles = True

        self.main_panel = PanedWindow(
            self.master, orient=VERTICAL, height=1000, width=1000)
        self.main_panel.pack(fill=BOTH, expand=1)

        self.col_one = PanedWindow(self.main_panel, orient=VERTICAL)
        self.main_panel.add(self.col_one)
        Label(self.col_one, text="BUDGET PROGRAM").pack()

        self.col_two = PanedWindow(self.main_panel, orient=VERTICAL)
        self.main_panel.add(self.col_two)
        self.accounts = LabelFrame(self.col_two, text="accounts")
        self.col_two.add(self.accounts)
        # accounts_label = Label(
        # self.accounts, text="ACCOUNTS").grid(row=0, column=1000, stick=NE)
        # self.accounts = LabelFrame(self.accounts_window, text="Current Amounts")
        # self.col_one.add(self.accounts)

        self.checking = StringVar()
        self.checking.set("0.0")
        self.saving = StringVar()
        self.saving.set("0.0")
        self.wellsFargoCreditCard = StringVar()
        self.wellsFargoCreditCard.set("0.0")
        self.amazonCreditCard = StringVar()
        self.amazonCreditCard.set("0.0")
        self.studentLoan = StringVar()
        self.studentLoan.set("0.0")

        # self.wristAngle = StringVar()
        # self.wristAngle.set("0.0")
        # self.gripperAngle = StringVar()
        # self.gripperAngle.set("0.0")
        # self.headAngle = StringVar()
        # self.headAngle.set("0.0")
        # for r in range(1000):
        #     for c in range(1000):
        #         Label(self.accounts, text='R%s/C%s' % (r, c),
        #               borderwidth=1).grid(row=r, column=c)
        # self.checking_label = Label(
        #     self.accounts, textvariable=self.checking).grid(row=500, column=500)
        # self.sholderLabel = Label(
        #     self.col_one, textvariable=self.sholderAngle).pack(side=LEFT)
        # self.upperArmLabel = Label(
        #     self.col_one, textvariable=self.upperArmAngle).pack(side=LEFT)
        # self.elbowLabel = Label(
        #     self.col_one, textvariable=self.elbowAngle).pack(side=LEFT)
        # self.forearmLabel = Label(
        #     self.col_one, textvariable=self.forearmAngle).pack(side=LEFT)
        # self.wristLabel = Label(
        #     self.col_one, textvariable=self.wristAngle).pack(side=LEFT)
        # self.gripperLabel = Label(
        #     self.col_one, textvariable=self.gripperAngle).pack(side=LEFT)
        # self.headLabel = Label(
        #     self.col_one, textvariable=self.headAngle).pack(side=LEFT)

        self.closing = LabelFrame(self.col_two, text="Closing")
        self.col_two.add(self.closing)

        self.close_program = Button(
            self.closing, text="Close GUI", width=100, command=self.closing_handle)
        self.close_program.pack()
        # Test
        # self.checking_var = "0.0"
        # self.checking = Entry(self.col_one, width = 100, textvariable = self.checking_var)

        # Label(self.col_one, text="Checking").pack()
        # self.checking.pack()
        # self.checking.bind('<Return>')
        # self.checking.bind('<KP_Enter>')

    def closing_handle(self):
        self.updateAngles = False
        print "Running Threads: "
        runningThreads = threading.enumerate()
        thread = threading.Thread()
        for t in runningThreads:
            if t.isAlive() and not t.isDaemon():
                print t
        self.master.destroy()


def main(args):
    control_panel = ControlPanel()
    control_panel.master.protocol(
        "WM_DELETE_WINDOW", control_panel.closing_handle)
    control_panel.master.mainloop()


if __name__ == '__main__':
    # proc = multiprocessing.process(target=helper_scripts.ready_robot)
    main(sys.argv)
