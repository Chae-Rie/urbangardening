import serial
import time
import tkinter


def quit():
    global tkTop
    ser.write(bytes('L', 'UTF-8'))
    tkTop.destroy()
    # Falls er bereits an war, soll er auf einen erwarteten Status zurückgesetzt werden


def request_light_state():
    ser.write(bytes('H', 'UTF-8'))
    # Request the sensor data


def request_soil_humidity_state():
    ser.write(bytes('L', 'UTF-8'))
    time.sleep(1)
    result = ser.read(4) # Ich glaube es wird ein Bit zurückgegeben
    print(result)
    # Request the sensor data


def request_air_humidity_state():
    pass
    # Request the sensor data


def something_else_to_request():
    pass
    # Muss noch was abgefragt werden?


ser = serial.Serial('com3', 9600)
print("Reset Arduino")
time.sleep(3)
ser.write(bytes('L', 'UTF-8'))

tkTop = tkinter.Tk()
tkTop.geometry('700x500')
tkTop.title("USB-Wartungsschnittstelle")
label3 = tkinter.Label(text='USB-Wartungsschnittstelle um die Komponenten der Schaltung abzufragen',
                       font=("Courier", 10, 'italic')).grid(
    column=0, row=0, ipadx=10, padx=10, pady=15, sticky="W"
)


# Buttons
light_button = tkinter.IntVar()
light_button_state = tkinter.Button(tkTop,
                              text="ON",
                              command=request_light_state,
                              height=1,
                              fg="black",
                              width=1,
                              bd=1,
                              activebackground='green'
                              )

light_button_state.grid(column=0, row=1, ipadx=10, padx=10, pady=15, sticky="W")

soil_humidity_button = tkinter.IntVar()
soil_humidity_state = tkinter.Button(tkTop,
                                    text="OFF",
                                    command=request_soil_humidity_state,
                                    height=1,
                                    fg="black",
                                    width=1,
                                    bd=1
                                    )

soil_humidity_state.grid(column=0, row=2, ipadx=10, padx=10, pady=15, sticky="W")


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

# Lables

light_sensor_data = tkinter.Label(tkTop, text="Result of the light sensor").grid(
    column=1, row=1, ipadx=10, padx=10, pady=15, sticky= "W")

soil_humidity_sensor_data = tkinter.Label(tkTop, text="Result of the soil humidity sensor").grid(
    column=1, row=2, ipadx=10, padx=10, pady=15, sticky= "W")

air_humidity_sensor_data = tkinter.Label(tkTop, text="Result of the air humidity sensor").grid(
    column=1, row=3, ipadx=10, padx=10, pady=15, sticky= "W")

tkinter.mainloop()
