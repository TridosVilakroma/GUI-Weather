
import requests
import tkinter 
from tkinter import * 
from PIL import Image, ImageTk
root = Tk()
def set_output():
    global temp_comment
    global temp_comment_output

    temp_comment_output.set(temp_comment)

def dbl_cmd(event=None):    
    take_input()
    flip()

def flip():    
    main_weather_loop()

def take_input():
    global query
    query=(xtestx.get())
    


root.title('Virtual Door')
root.geometry('400x350')
root.resizable(0, 0)

#Background image
image1 = Image.open(r'C:\Users\Caleb Stock\PythonProjects\GUI Weather\Weather\Sunlit-Skyscape.png')
image1 = image1.resize((500,350), Image.ANTIALIAS)
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(relwidth=1, relheight=1)

#User input, for city name
xtestx = StringVar()
city_input = Entry(root, width=20, textvariable=xtestx)
city_input.place(relx=.35,rely=.2)

#Instrucion text at top of window
interface = tkinter.Canvas(root, height = 100, width = 50)
instruct = Label(root,text='Whats it like in your city?\n Enter a city name and click the door to check the weather.',bg="#B5E3E7", fg='#1B4D51')
instruct.place(relx=.15,rely=.05)

#Door button
door_frame= tkinter.Frame(root,)
door_frame.place(relx=.4, rely=.3)
image2=Image.open(r'C:\Users\Caleb Stock\PythonProjects\GUI Weather\Weather\door.png')
image2 = image2.resize((75,125), Image.ANTIALIAS)
door = ImageTk.PhotoImage(image2)
button = tkinter.Button(door_frame, image= door, command=dbl_cmd)
root.bind('<Return>',dbl_cmd )
button.pack()

#City weather output area
temp_comment_output=StringVar()
user_output=Label(root, bg='#082326', fg="#B5E3E7",anchor=W, width=19, wraplength=125, textvariable=temp_comment_output )
user_output.place(relx=.33, rely=.7)









class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'




def main_weather_loop():
    global query
    global xtestx
    req = requests.get('https://www.metaweather.com/api/location/search/?query={}'.format(query)).json()
    


    city_unvalidated = True
    woeid = None
    while city_unvalidated:
        try:
            woeid = req[0]['woeid']
            break
        except:
            global temp_comment
            temp_comment ='That city was not recognized. Maybe it\'s too small or fictional. Try entering a bigger non-fictional city like New York or London.'
            set_output()
            req = requests.get('https://www.metaweather.com/api/location/search/?query={}'.format(query)).json()
            break

    if not woeid == None:
        
        weather_res = requests.get('https://www.metaweather.com/api/location/{}'.format(woeid)).json()

        current_temp = (weather_res['consolidated_weather'][0]['the_temp'] * 1.80 + 32)
        weather_state = weather_res['consolidated_weather'][0]['weather_state_name']

        if current_temp >= 80:
            temp_comment = (str(int(current_temp)) + '°F \n' +"Yikes, it's scorching!")
            set_output()
            return
        elif current_temp >= 70 and current_temp < 80:
            temp_comment = (str(int(current_temp)) + '°F \n' + 'Okay, this temperature is perfect!')
            set_output()
            return
        elif current_temp >= 60 and current_temp < 70:
            temp_comment = (str(int(current_temp)) + '°F \n' +'Kinda chilly out, grab a jacket.')
            set_output()
            return
        elif current_temp < 60:
            temp_comment = (str(int(current_temp)) + '°F \n' +"It's too darn cold out! I'm migrating South!")
            set_output()
            return


       



root.mainloop()