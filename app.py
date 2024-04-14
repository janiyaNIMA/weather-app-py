from tkinter import *
from PIL import Image, ImageTk
import requests

root = Tk()
root.geometry("300x250")
root.title("Weather Focast")
root.iconbitmap(r'assets/rain.ico')

search_box = Entry(root)
search_box.focus()

#get Weather
def getWeather():
    
    city_name = search_box.get()
    #API
    API_TOKEN = 'b8a0131cac0cc7e9d7b6ba1c386f8f26'
    URL = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_TOKEN}'
    resp = requests.get(URL)
    json_data = resp.json()

    #weather config
    city = json_data['name']
    temp = int(json_data['main']['temp'] - 273)
    humidity = str(json_data['main']['humidity'])
    speed = json_data['wind']['speed']
    city = json_data['name']

    city_label.config(text=city)
    #temp_label.config(text=temp +'°C')
    temp_label.config(text=f'{temp}°C')
    Humidity_label.config(text=humidity +'%')
    Wind_Speed_label.config(text=f'{speed} km/h')

    #print(resp.json())

search_btn = Button(root, text="Search", command=getWeather)

icn = Image.open('assets/rain.png')
resize = icn.resize((100,100))
new_icon = ImageTk.PhotoImage(resize)
icn_labal = Label(root, image=new_icon)

#def colours

red = '#D10B0B'
orange = '#D97812'
yellow = '#CBD324'
green = '#35991D'
sea_blue = '#30CCAB'


#temp
temp_label = Label(root, text='...', background=red)
city_label = Label(root, text='...', background=orange)
Humidity_text = Label(root, text='Humidity', background=yellow)
Wind_Speed_text = Label(root, text='Wind Speed', background=green)
Humidity_label = Label(root, text='...', background=sea_blue)
Wind_Speed_label = Label(root, text='...', background=orange)

#grid config
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)

#Pack Widgets
search_box.grid(row=0, column=0)
search_btn.grid(row=0, column=1)
icn_labal.grid(row=1, column=0, columnspan=2)
temp_label.grid(row=2, column=0, columnspan=2, sticky='we')
city_label.grid(row=3, column=0, columnspan=2, sticky='we')
Humidity_text.grid(row=4, column=0, sticky='we')
Wind_Speed_text.grid(row=4, column=1, sticky='we')
Humidity_label.grid(row=5, column=0, sticky='we')
Wind_Speed_label.grid(row=5, column=1, sticky='we')


root.mainloop()