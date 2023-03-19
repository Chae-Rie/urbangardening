import serial
import time
import tkinter


def quit():
    global tkTop
    arduino.write(bytes('L', 'UTF-8'))
    tkTop.destroy()
    #Falls er bereits an war, soll er auf einen erwarteten Status zurückgesetzt werden


def request_light_state():
    data_to_be_sent = "H"
    expected_size_of_answer = 4
    arduino.write(bytes(data_to_be_sent, 'UTF-8'))
    result = arduino.read(expected_size_of_answer)
    light_var.set(result)
    # Request the sensor data


def request_soil_humidity_state():
    data_to_be_sent = "L"
    expected_size_of_answer = 4  #Jenachdem wie groß die erwartete Menge an bits ist
    arduino.write(bytes(data_to_be_sent, 'UTF-8'))
    result = arduino.read(expected_size_of_answer)
    soil_humidity_var.set(result)
    # Request the sensor data


def request_air_humidity_state():
    data_to_be_sent = "J"
    expected_size_of_answer = 4
    arduino.write(bytes(data_to_be_sent, "UTF-8"))
    result = arduino.read(expected_size_of_answer)
    #air_humidity_var.set(f"{result}")
    air_humidity_var.set(result)
    # Request the sensor data


def something_else_to_request():
    expected_size_of_answer = 4
    pass
    #Muss noch was abgefragt werden?


arduino = serial.Serial('com3', 9600)
print("Reset Arduino")
time.sleep(3)
arduino.write(bytes('L', 'UTF-8'))

tkTop = tkinter.Tk()
tkTop.geometry('700x400')
tkTop.title("USB-Wartungsschnittstelle")
label3 = tkinter.Label(text='USB-Wartungsschnittstelle um die Komponenten der Schaltung abzufragen',
                       font=("Courier", 10, 'italic')).grid(
    column=0, columnspan=2,  row=0, ipadx=10, padx=10, pady=15, sticky="W"
)


# Buttons
light_var = tkinter.StringVar()
light_button = tkinter.Button(tkTop,
                              text="Request_light /ON",
                              command=request_light_state,
                              height=1,
                              fg="black",
                              width=20,
                              bd=1,
                              activebackground='green'
                              )

light_button.grid(column=0, row=1, ipadx=10, padx=10, pady=15, sticky="W")

soil_humidity_var = tkinter.StringVar()
soil_humidity_button = tkinter.Button(tkTop,
                                    text="Request_soil_humidity /OFF",
                                    command=request_soil_humidity_state,
                                    height=1,
                                    fg="black",
                                    width=20,
                                    bd=1
                                    )

soil_humidity_button.grid(column=0, row=2, ipadx=10, padx=10, pady=15, sticky="W")

air_humidity_var = tkinter.StringVar()
air_humidity_button = tkinter.Button(
    tkTop,
    text="Request_air_humidity",
    command=request_air_humidity_state,
    height=1,
    fg="black",
    width=20,
    bd=1
)
air_humidity_button.grid(column=0, row=3, ipadx=10, padx=10, pady=15, sticky="W")

tkButtonQuit = tkinter.Button(
    tkTop,
    text="Quit",
    command=quit,
    height=1,
    fg="black",
    width=1,
    bg='red',
    bd=1
)
tkButtonQuit.grid(column=0, row=4, ipadx=10, padx=10, pady=15, sticky="W")

# Labels

light_lable = tkinter.Label(tkTop, text="Aktuelle Lichtstärke:").grid(
    column=1, row=1, padx=1, pady=15, sticky= "W")

light_sensor_data = tkinter.Label(tkTop, textvariable=light_var, ).grid(
    column=2, row=1, padx=1, pady=15, sticky= "W")

soil_humidity_lable = tkinter.Label(tkTop, text="Aktuelle Bodenfeuchte:").grid(
    column=1, row=2, padx=1, pady=15, sticky= "W")

soil_humidity_sensor_data = tkinter.Label(tkTop, textvariable=soil_humidity_var, ).grid(
    column=2, row=2, padx=1, pady=15, sticky= "W")


air_humidity_lable = tkinter.Label(tkTop, text="Aktuelle Luftfeuchtigkeit:").grid(
    column=1, row=3, padx=1, pady=15, sticky= "W")

air_humidity_sensor_data = tkinter.Label(tkTop, textvariable=air_humidity_var, ).grid(
    column=2, row=3, padx=1, pady=15, sticky= "W")

tkinter.mainloop()
