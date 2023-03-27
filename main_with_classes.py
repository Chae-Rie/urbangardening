import serial
import time
import tkinter
import threading


class USBInterface:
    def __init__(self, port, baudrate):
        self.arduino = serial.Serial(port, baudrate)
        self.tkTop = tkinter.Tk()
        self.tkTop.geometry('900x400')
        self.tkTop.title("USB-Wartungsschnittstelle")

        self.light_sensor_data = tkinter.Label(self.tkTop, text="0", )
        self.soil_humidity_sensor_data = tkinter.Label(self.tkTop, text="0", )
        self.air_humidity_sensor_data = tkinter.Label(self.tkTop, text="0", )

        # Wird im Standardkonstruktor aufgerufen, ansonsten gibts kein Bild alla
        self.create_gui()

    def create_gui(self):
        label3 = tkinter.Label(text='USB-Wartungsschnittstelle um die Komponenten der Schaltung abzufragen',
                               font=("Courier", 10, 'italic'))
        label3.grid(column=0, columnspan=2, row=0, ipadx=10, padx=10, pady=15, sticky="W")

        # Labels
        light_label = tkinter.Label(self.tkTop, text="Aktuelle Lichtstärke:")
        light_label.grid(column=1, row=1, padx=1, pady=15, sticky="W")
        self.light_sensor_data.grid(column=2, row=1, padx=1, pady=15, sticky="W")

        soil_humidity_label = tkinter.Label(self.tkTop, text="Aktuelle Bodenfeuchte:")
        soil_humidity_label.grid(column=1, row=2, padx=1, pady=15, sticky="W")
        self.soil_humidity_sensor_data.grid(column=2, row=2, padx=1, pady=15, sticky="W")

        air_humidity_label = tkinter.Label(self.tkTop, text="Aktuelle Luftfeuchtigkeit:")
        air_humidity_label.grid(column=1, row=3, padx=1, pady=15, sticky="W")
        self.air_humidity_sensor_data.grid(column=2, row=3, padx=1, pady=15, sticky="W")

        # Buttons and correspoding vars
        light_button = tkinter.Button(self.tkTop,
                                      text="Request_light /ON",
                                      command=self.request_light_state,
                                      height=1,
                                      fg="black",
                                      width=20,
                                      bd=1,
                                      activebackground='green'
                                      )
        light_button.grid(column=0, row=1, ipadx=10, padx=10, pady=15, sticky="W")

        soil_humidity_button = tkinter.Button(self.tkTop,
                                               text="Request_soil_humidity /OFF",
                                               command=self.request_soil_humidity_state,
                                               height=1,
                                               fg="black",
                                               width=20,
                                               bd=1
                                               )
        soil_humidity_button.grid(column=0, row=2, ipadx=10, padx=10, pady=15, sticky="W")

        air_humidity_button = tkinter.Button(
            self.tkTop,
            text="Request_air_humidity",
            command=self.request_air_humidity_state,
            height=1,
            fg="black",
            width=20,
            bd=1
        )
        air_humidity_button.grid(column=0, row=3, ipadx=10, padx=10, pady=15, sticky="W")

        tkButtonQuit = tkinter.Button(
            self.tkTop,
            text="Quit",
            command=self.quit,
            height=1,
            fg="black",
            width=1,
            bg='red',
            bd=1
        )
        tkButtonQuit.grid(column=0, row=4, ipadx=10, padx=10, pady=15, sticky="W")

    def send_data(self, data):
        self.arduino.write(data.encode())

    def read_data(self, label):
        # die loop kann erstmal so durchlaufen
        while True:
            if self.arduino.in_waiting > 0:
                # Lies die gesamt geschriebene Zeile aus, decodier sie und entferne die whitespaces
                # es wird aber nur eine Kopie vom String zurückgegeben -> beachte das.
                data = self.arduino.readline().decode().rstrip()

                if label == "light":
                    self.light_sensor_data.config(text=data)
                elif label == "soil_humidity":
                    self.soil_humidity_sensor_data.config(text=data)
                elif label == "air_humidity":
                    self.air_humidity_sensor_data.config(text=data)
                else:
                    pass
                # something bad happened -> gib eine Fehlermeldung aus

                # label.config(text=data)

    def request_light_state(self):
        data_to_be_sent = "H"
        self.send_data("H")
        thread = threading.Thread(target=self.read_data, args=("light",))
        thread.daemon = True
        thread.start()

    def request_soil_humidity_state(self):
        data_to_be_sent = "L"
        self.send_data("L")
        thread = threading.Thread(target=self.read_data, args=("soil_humidity",))
        thread.daemon = True
        thread.start()

    def request_air_humidity_state(self):
        data_to_be_sent = "J"
        self.send_data("J")
        thread = threading.Thread(target=self.read_data, args=("air_humidity",))
        thread.daemon = True
        thread.start()

    def quit(self):
        # self.arduino.write(bytes('L', 'UTF-8'))
        self.tkTop.destroy()
        # Falls er bereits an war, soll er auf einen erwarteten Status zurückgesetzt werden


if __name__ == '__main__':
    USB = USBInterface("COM3", 9600) # Replace "COM3" and 9600 with your desired port and baudrate
    USB.tkTop.mainloop()