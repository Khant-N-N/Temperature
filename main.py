
import customtkinter
from customtkinter import CTkFrame, CTkLabel, CTkFont


def temperature_convert():
    choice = selected_value.get()
    if choice == "C":
        to_celsius()
    else:
        to_fahrenheit()


def to_celsius():
    fahrenheit = float(input_box.get())
    celsius = (fahrenheit - 32) * 5/9
    celsius_text = f"{celsius:.2f} °C"
    result_text.configure(text=celsius_text)


def to_fahrenheit():
    celsius = float(input_box.get())
    fahrenheit = (celsius * 9/5) + 32
    fahrenheit_text = f"{fahrenheit:.2f} °F"
    result_text.configure(text=fahrenheit_text)


app = customtkinter.CTk()
customtkinter.set_appearance_mode("dark")
app.geometry("600x400")

app.title("Temperature Converter")
title_label = customtkinter.CTkLabel(app, text="Temperature Converter",
                                     text_color="aqua", font=customtkinter.CTkFont(size=30, weight="bold"))
title_label.pack(padx=30, pady=(30, 20))

# radio
radio_frame = customtkinter.CTkFrame(app)
radio_frame.pack(fill="x", padx=50)

selected_value = customtkinter.StringVar(value="C")

radio_button_F_to_C = customtkinter.CTkRadioButton(
    radio_frame, value="C", text="Fahrenheit to Celsius", variable=selected_value)
radio_button_F_to_C.pack(side="left", padx=(80, 10), pady=10)

radio_button_C_to_F = customtkinter.CTkRadioButton(
    radio_frame, value="F", text="Celsius to Fahrenheit", variable=selected_value)
radio_button_C_to_F.pack(side="right", padx=(10, 80), pady=10)

# input
input_frame = customtkinter.CTkFrame(app)
input_frame.pack(pady="20", fill="x", padx=50)

input_box = customtkinter.CTkEntry(
    input_frame, placeholder_text="Enter Temperature...")
input_box.pack(side="left", padx=(80, 10), pady=10)

convert_button = customtkinter.CTkButton(
    input_frame, text="Convert", command=temperature_convert)
convert_button.pack(side="right", padx=(10, 80), pady=10)

# temp text
text_frame = CTkFrame(app)
text_frame.pack(fill="x", padx=50, pady=10)

result_text = CTkLabel(text_frame, text_color="aqua",
                       text="", font=CTkFont(weight="bold", size=30))
result_text.pack()

app.mainloop()
