import tkinter as tk
import serial

class App:
    def __init__(self, master):
        self.master = master
        master.title("Arduino Communication App")

        # create label and entry widgets
        tk.Label(master, text="Enter message to send to Arduino:").grid(row=0, column=0)
        self.msg_entry = tk.Entry(master, width=40)
        self.msg_entry.grid(row=0, column=1)

        # create send button
        self.send_button = tk.Button(master, text="Send", command=self.send_msg)
        self.send_button.grid(row=1, column=0)

        # create label for displaying response
        tk.Label(master, text="Arduino response:").grid(row=2, column=0)
        self.response_label = tk.Label(master, text="")
        self.response_label.grid(row=2, column=1)

        # set up serial connection to Arduino
        self.ser = serial.Serial('COM3', 9600, timeout=1)

    def send_msg(self):
        # send message to Arduino
        msg = self.msg_entry.get().encode()
        self.ser.write(msg)

        # read response from Arduino without blocking GUI
        self.master.after(100, self.read_response)

    def read_response(self):
        if self.ser.in_waiting > 0:
            response = self.ser.readline().decode().strip()
            self.response_label.config(text=response)
        self.master.after(100, self.read_response)

root = tk.Tk()
app = App(root)
root.mainloop()
