import serial
import tkinter
import threading
import struct


class USBInterface:
    def __init__(self, port, baudrate):
        self.arduino = serial.Serial(port, baudrate)
        self.tkTop = tkinter.Tk()
        self.tkTop.geometry('900x400')
        self.tkTop.title("USB-Wartungsschnittstelle")

        self.air_humidity = 0
        self.soil_humidity = 0
        self.light = 0

        self.light_label = tkinter.Label(self.tkTop, text="Aktuelle Lichtstärke:")
        self.light_sensor_data = tkinter.Label(self.tkTop, text="0", )
        self.light_status = tkinter.Label(self.tkTop, text="N/A",)
        self.soil_humidity_label = tkinter.Label(self.tkTop, text="Aktuelle Bodenfeuchte:")
        self.soil_humidity_sensor_data = tkinter.Label(self.tkTop, text="0", )
        self.soil_humidity_status = tkinter.Label(self.tkTop, text="N/A",)
        self.air_humidity_label = tkinter.Label(self.tkTop, text="Aktuelle Luftfeuchtigkeit:")
        self.air_humidity_sensor_data = tkinter.Label(self.tkTop, text="0", )
        self.air_humidity_status = tkinter.Label(self.tkTop, text="N/A",)

        # Wird im Standardkonstruktor aufgerufen, ansonsten gibts kein Bild alla
        self.create_gui()
        thread = threading.Thread(target=self.read_data,)
        thread.daemon = True
        thread.start()

    def create_gui(self):
        label3 = tkinter.Label(text='USB-Wartungsschnittstelle um die Komponenten der Schaltung abzufragen',
                               font=("Courier", 10, 'italic'))
        label3.grid(column=0, columnspan=2, row=0, ipadx=10, padx=10, pady=15, sticky="W")

        # Labels

        self.light_label.grid(column=1, row=1, padx=1, pady=15, sticky="W")
        self.light_sensor_data.grid(column=2, row=1, padx=1, pady=15, sticky="W")
        self.light_status.grid(column=3, row=1, padx=1, pady=15, sticky="W")

        self.soil_humidity_label.grid(column=1, row=2, padx=1, pady=15, sticky="W")
        self.soil_humidity_sensor_data.grid(column=2, row=2, padx=1, pady=15, sticky="W")
        self.soil_humidity_status.grid(column=3, row=2, padx=1, pady=15, sticky="W")

        self.air_humidity_label.grid(column=1, row=3, padx=1, pady=15, sticky="W")
        self.air_humidity_sensor_data.grid(column=2, row=3, padx=1, pady=15, sticky="W")
        self.air_humidity_status.grid(column=3, row=3, padx=1, pady=15, sticky="W")


        # Buttons and corresponding vars
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

        tkbuttonquit = tkinter.Button(
            self.tkTop,
            text="Quit",
            command=self.quit,
            height=1,
            fg="black",
            width=1,
            bg='red',
            bd=1
        )
        tkbuttonquit.grid(column=0, row=4, ipadx=10, padx=10, pady=15, sticky="W")

    def send_data(self, data):
        self.arduino.write(data.encode())

    def read_data(self):
        # die loop kann erstmal so durchlaufen
        while True:
            if self.arduino.in_waiting > 0:
                # Lies die gesamt geschriebene Zeile aus -> bis \n, decodier sie und entferne die whitespaces
                # es wird aber nur eine Kopie vom String zurückgegeben -> beachte das.

                # passend für strings
                data = self.arduino.readline().decode().strip()

                components = data.split(',')
                self.air_humidity = int(components[0])
                self.soil_humidity = int(components[1])
                self.light = int(components[2])

    def request_light_state(self):
        # data_to_be_sent = "H"
        self.send_data("H")

        self.light_sensor_data.config(text=self.light)

    def request_soil_humidity_state(self):
        # data_to_be_sent = "L"
        self.send_data("L")
        self.soil_humidity_sensor_data.config(text=self.soil_humidity)


    def request_air_humidity_state(self):
        # data_to_be_sent = "J"
        self.send_data("J")
        self.air_humidity_sensor_data.config(text=self.air_humidity)


    def quit(self):
        # self.arduino.write(bytes('L', 'UTF-8'))
        self.tkTop.destroy()
        # Falls er bereits an war, soll er auf einen erwarteten Status zurückgesetzt werden


if __name__ == '__main__':
    USB = USBInterface("COM3", 9600) # Replace "COM3" and 9600 with your desired port and baudrate
    USB.tkTop.mainloop()