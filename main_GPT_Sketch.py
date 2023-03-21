import tkinter as tk
import serial
import threading

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Arduino Communication App")
        self.master.geometry("300x200")
        self.initUI()

    def initUI(self):
        self.lbl_send = tk.Label(self.master, text="Send to Arduino:")
        self.lbl_send.grid(row=0, column=0, padx=10, pady=10)

        self.entry_send = tk.Entry(self.master)
        self.entry_send.grid(row=0, column=1, padx=10, pady=10)

        self.btn_send = tk.Button(self.master, text="Send", command=self.send_to_arduino)
        self.btn_send.grid(row=0, column=2, padx=10, pady=10)

        self.lbl_recv = tk.Label(self.master, text="Received from Arduino:")
        self.lbl_recv.grid(row=1, column=0, padx=10, pady=10)

        self.entry_recv = tk.Entry(self.master)
        self.entry_recv.grid(row=1, column=1, padx=10, pady=10)

    def send_to_arduino(self):
        self.entry_recv.delete(0, tk.END) # clear the entry box
        self.ser = serial.Serial('COM3', 9600, timeout=1) # change the COM port to match your setup
        self.ser.write(self.entry_send.get().encode())
        t = threading.Thread(target=self.read_from_arduino)
        t.start()

    def read_from_arduino(self):
        while True:
            line = self.ser.readline().decode().strip()
            if line:
                self.master.after(0, self.entry_recv.insert(0, line + '\n')) # update the GUI with the received data
            if not line:
                break
        self.ser.close()

root = tk.Tk()
app = App(root)
root.mainloop()
