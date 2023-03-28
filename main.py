import serial
import tkinter
import threading


class USBInterface:
    def __init__(self, port, baudrate):
        self.arduino = serial.Serial(port, baudrate)
        self.tkTop = tkinter.Tk()
        self.tkTop.geometry('1000x400')
        self.tkTop.title("USB-Wartungsschnittstelle")

        self.actual_air_humidity = 0
        self.actual_soil_humidity = 0
        self.actual_light = 0

        self.light_label = tkinter.Label(self.tkTop, text="Aktuelle Lichtstärke:")
        self.light_sensor_data_label = tkinter.Label(self.tkTop, text="0", )
        self.light_status = tkinter.Label(self.tkTop, text="N/A",)
        self.soil_humidity_label = tkinter.Label(self.tkTop, text="Aktuelle Bodenfeuchte:")
        self.soil_humidity_sensor_data_label = tkinter.Label(self.tkTop, text="0", )
        self.soil_humidity_status = tkinter.Label(self.tkTop, text="N/A",)
        self.air_humidity_label = tkinter.Label(self.tkTop, text="Aktuelle Luftfeuchtigkeit:")
        self.air_humidity_sensor_data_label = tkinter.Label(self.tkTop, text="0", )
        self.air_humidity_status = tkinter.Label(self.tkTop, text="N/A",)

        self.arduino_info_label = tkinter.Label(self.tkTop, text=f"My board on port: {port} with baudrate: {baudrate}.")
        # Wird im Standardkonstruktor aufgerufen, ansonsten gibts kein Bild alla
        self.create_gui()

        # Es wird ein Thread abgestellt der permanent die read_data() Methode callen soll
        self.start_reading_thread()

    def create_gui(self):
        label3 = tkinter.Label(text='USB-Wartungsschnittstelle um die Komponenten der Schaltung abzufragen',
                               font=("Courier", 10, 'italic'))
        label3.grid(column=0, columnspan=2, row=0, ipadx=10, padx=10, pady=15, sticky="W")

        # Labels

        self.light_label.grid(column=1, row=1, padx=1, pady=15, sticky="W")
        self.light_sensor_data_label.grid(column=2, row=1, padx=1, pady=15, sticky="W")
        self.light_status.grid(column=3, row=1, padx=1, pady=15, sticky="W")

        self.soil_humidity_label.grid(column=1, row=2, padx=1, pady=15, sticky="W")
        self.soil_humidity_sensor_data_label.grid(column=2, row=2, padx=1, pady=15, sticky="W")
        self.soil_humidity_status.grid(column=3, row=2, padx=1, pady=15, sticky="W")

        self.air_humidity_label.grid(column=1, row=3, padx=1, pady=15, sticky="W")
        self.air_humidity_sensor_data_label.grid(column=2, row=3, padx=1, pady=15, sticky="W")
        self.air_humidity_status.grid(column=3, row=3, padx=1, pady=15, sticky="W")

        self.arduino_info_label.grid(column=1, row=4, padx=1, pady=15, sticky="W")

        # Buttons and corresponding vars
        light_button = tkinter.Button(self.tkTop,
                                      text="Request_light",
                                      command=self.request_light_state,
                                      height=1,
                                      fg="black",
                                      width=20,
                                      bd=1,
                                      activebackground='green'
                                      )
        light_button.grid(column=0, row=1, ipadx=10, padx=10, pady=15, sticky="W")

        soil_humidity_button = tkinter.Button(self.tkTop,
                                               text="Request_soil_humidity",
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

    def start_reading_thread(self):
        thread = threading.Thread(target=self.read_data,)
        thread.daemon = True
        thread.start()

    def send_data(self, data):
        self.arduino.write(data.encode())

    def read_data(self):
        # die loop kann erstmal so durchlaufen
        while True:
            if self.arduino.in_waiting > 0:
                # Lies die gesamt geschriebene Zeile aus -> bis \n, decodier sie und entferne die whitespaces
                # es wird aber nur eine Kopie vom String zurückgegeben -> beachte das.

                data = self.arduino.readline().decode().strip()

                components = data.split(',')
                # TODO: Die Liste components erzeugt manchmal einen out of range fehler -> irgendwas stimmt mit dem Index nicht
                # Die Strings sind besser auseinanderzuhalten wenn delimiter verwendet werden
                self.actual_air_humidity = int(components[0])
                self.actual_soil_humidity = int(components[1])
                self.actual_light = int(components[2])

    def request_light_state(self):
        self.light_sensor_data_label.config(text=self.actual_light)
        # Im Arduino code wird ein unsigned integer verwendet, aber sicherheitshalber wird gegen kleiner als getestet

        if self.actual_light <= 0:
            self.light_status.config(text="Something went off with the lights, \nif pressing 'request_light_state' "
                                          "again doesn't help, please check!")
        else:
            self.light_status.config(text="Light sensor is working properly.")

    def request_soil_humidity_state(self):
        self.soil_humidity_sensor_data_label.config(text=self.actual_soil_humidity)
        if self.actual_soil_humidity <= 0:
            self.soil_humidity_status.config(text="Something went off with the soil humidity-sensor, \nif pressing "
                                                  "'request_soil_humidity_state' again doesn't help, please check!")
        else:
            self.soil_humidity_status.config(text="Humidity-sensor is working properly.")

    def request_air_humidity_state(self):
        self.air_humidity_sensor_data_label.config(text=self.actual_air_humidity)
        if self.actual_air_humidity <= 0:
            self.air_humidity_status.config(text="Something went off with the air humidity-sensor, \nif pressing "
                                                 "'request_air_humidity_state' again doesn't help, please check!")
        else:
            self.air_humidity_status.config(text="Air humidity-sensor is working properly.")

    def quit(self):
        self.tkTop.destroy()
        # Falls er bereits an war, soll er auf einen erwarteten Status zurückgesetzt werden


if __name__ == '__main__':
    USB = USBInterface("COM3", 9600) # Our Arduino
    USB.tkTop.mainloop()