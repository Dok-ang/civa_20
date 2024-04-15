from kivy.app import App # Клас App є основою для створення програм Kivy
# Screen - шаблон вікон
# ScreenManager - менеджер перемикання вікон
# WipeTransition - клас анімації переходу вікон
from kivy import platform # перевірка платформи
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
import pygame
pygame.init()
from kivy.core.window import Window
import threading
import os
import heapq
import time
all_command=[]
all_priority={
    "reboot":5,
    "update_resource":8,
    "donat":0
    }
path=""
if platform=="android":
    path=os.path.abspath('')+"/"

if platform=="win":
    w,h=pygame.display.Info().current_w,pygame.display.Info().current_h
    Window.size=[w//2.5,h//6*4]
    Window.left=w/2-Window.size[0]/2
    Window.top=h/2-Window.size[1]/2
resource_mining_speed={} # стандартний час збільшення ресурсів без впливу будівель
resource_time_mining_speed={} # час оновлення
import json
#options={"volume":0.5}
#file_options=open("options.txt","w")
#file_options.write(json.dumps(options))
#file_options.close()
file_options=open(path+"file/options.json","r")
#list_options=file_options.readlines()
options=json.loads(file_options.read())
file_options.close()
fon_music=pygame.mixer.Sound("music/something_lost-185380.mp3")
fon_music.play(-1)
#fon_music.set_volume(float(list_options[0]))
fon_music.set_volume(options["volume"])
# 1 рядок гучність звуку
#options={"text_size":Window.size[0]/15,"volume":float(list_options[0])}
options["text_size"]=Window.size[0]/15
options["server_connect"]=False
from kivy.uix.screenmanager import Screen, ScreenManager, WipeTransition, SlideTransition, FallOutTransition, CardTransition, SwapTransition
import socket

def start_game():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    with open("file/atile.json","r") as f:
        reg_options=f.read()
        while True:
            try:
                s.connect(("80.77.36.110",2024))
                break
            except:
                pass     
    #print(text)
    
    s.sendall(reg_options.encode("utf-8"))
    reg_options=json.loads(reg_options)
    date=s.recv(1024).decode("utf-8")
    print(date)
    command=json.loads(date)
    if command["action"]=="reboot":
        print("reboot")
        reg_options["id"]=command["id"]
        reg_options["token"]=command["token"]
        with open("file/atile.json","w") as f:
            f.write(json.dumps(reg_options))
            print("dumps")
        heapq.heappush(all_command,(all_priority["reboot"],time.time(),command))
    elif command["action"]=="update_resource":
        heapq.heappush(all_command,(all_priority["update_resource"],time.time(),command))
    command={"action":"resource_mining"}
    date=json.dumps(command)
    s.close()

    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    while True:
        try:
            s.connect(("80.77.36.110",2024))
            break
        except:
            pass   

    s.sendall(date.encode("utf-8"))
    date=s.recv(1024).decode("utf-8")
    mys=json.loads(date)
    #print(mys)
    resource_mining_speed.update(mys)
    time_now=time.time()
    rtms={
        "people":time_now,"food":time_now,"tree":time_now,"stone":time_now,
        "oil":time_now,"iron":time_now,"gold":time_now}
    resource_time_mining_speed.update(rtms)
    s.close()
    

class Policy(Screen): # ігровий клас
    name="policy" # ім'я гри для переходу між вікнами
    def __init__(self): # конструктор класу
        Screen.__init__(self) # звертаємо до конструктора суперкласу
        self.add_widget(Button(text="Політика",color=[1,1,0,1]))
class Trade(Screen): # ігровий клас
    name="trade" # ім'я гри для переходу між вікнами
    def __init__(self): # конструктор класу
        Screen.__init__(self) # звертаємо до конструктора суперкласу
        self.add_widget(Button(text="Торгівля",color=[1,1,0,1]))
class Infrastructure(Screen): # ігровий клас
    name="infrastructure" # ім'я гри для переходу між вікнами
    def __init__(self): # конструктор класу
        Screen.__init__(self) # звертаємо до конструктора суперкласу
        self.add_widget(Button(text="Моя інфраструктура",color=[1,1,0,1]))
class Army(Screen): # ігровий клас
    name="army" # ім'я гри для переходу між вікнами
    def __init__(self): # конструктор класу
        Screen.__init__(self) # звертаємо до конструктора суперкласу
        self.add_widget(Button(text="Моя армія",color=[1,1,0,1]))
class City(Screen): # ігровий клас
    name="city" # ім'я гри для переходу між вікнами
    def __init__(self): # конструктор класу
        Screen.__init__(self) # звертаємо до конструктора суперкласу
        self.add_widget(Button(text="Моє місто",color=[1,1,0,1]))


thred_game=threading.Thread(target=start_game)
class Game(Screen): # ігровий клас
    name="game" # ім'я гри для переходу між вікнами
    def __init__(self): # конструктор класу
        Screen.__init__(self) # звертаємо до конструктора суперкласу



        box=BoxLayout(orientation="vertical",spacing=Window.size[1]//20+1)
        
        self.panel=BoxLayout(size_hint=[1,0.2])

        button_menu=Button(text="Menu",font_size=options["text_size"],
                           font_name="font/7fonts_Knight2.ttf",
        color=[1,1,0,0.7],background_color=[0,0,0,0],on_press=self.go_menu) # кнопка переходу в гру
        self.panel.add_widget(button_menu)


        #all_resource=GridLayout(cols=4)
        #self.panel.add_widget(all_resource)





        resource_box=GridLayout(size_hint=[4,1],cols=7)
        self.panel.add_widget(resource_box)

        box_people=BoxLayout(orientation="vertical")
        people_button_image=Button(background_normal=path+"sprites/people.png", background_down=path+"sprites/people.png")
        box_people.add_widget(people_button_image)
        self.people_button_text=Button(size_hint=[1,0.1],text="-",background_normal="", background_down="",color=[1,0,1,1],background_color=[0,0,0,1])
        box_people.add_widget(self.people_button_text)
        resource_box.add_widget(box_people)

        box_food=BoxLayout(orientation="vertical")
        food_button_image=Button(background_normal=path+"sprites/food.png", background_down=path+"sprites/food.png")
        box_food.add_widget(food_button_image)
        self.food_button_text=Button(size_hint=[1,0.1],text="-",background_normal="", background_down="",color=[1,0,1,1],background_color=[0,0,0,1])
        box_food.add_widget(self.food_button_text)
        resource_box.add_widget(box_food)

        box_tree=BoxLayout(orientation="vertical")
        tree_button_image=Button(background_normal=path+"sprites/tree.png", background_down=path+"sprites/tree.png")
        box_tree.add_widget(tree_button_image)
        self.tree_button_text=Button(size_hint=[1,0.1],text="-",background_normal="", background_down="",color=[1,0,1,1],background_color=[0,0,0,1])
        box_tree.add_widget(self.tree_button_text)
        resource_box.add_widget(box_tree)

        box_stone=BoxLayout(orientation="vertical")
        stone_button_image=Button(background_normal=path+"sprites/stone.png", background_down=path+"sprites/stone.png")
        box_stone.add_widget(stone_button_image)
        self.stone_button_text=Button(size_hint=[1,0.1],text="-",background_normal="", background_down="",color=[1,0,1,1],background_color=[0,0,0,1])
        box_stone.add_widget(self.stone_button_text)
        resource_box.add_widget(box_stone)

        box_iron=BoxLayout(orientation="vertical")
        iron_button_image=Button(background_normal=path+"sprites/iron.png", background_down=path+"sprites/iron.png")
        box_iron.add_widget(iron_button_image)
        self.iron_button_text=Button(size_hint=[1,0.1],text="-",background_normal="", background_down="",color=[1,0,1,1],background_color=[0,0,0,1])
        box_iron.add_widget(self.iron_button_text)
        resource_box.add_widget(box_iron)

        box_gold=BoxLayout(orientation="vertical")
        gold_button_image=Button(background_normal=path+"sprites/gold.png", background_down=path+"sprites/gold.png")
        box_gold.add_widget(gold_button_image)
        self.gold_button_text=Button(size_hint=[1,0.1],text="-",background_normal="", background_down="",color=[1,0,1,1],background_color=[0,0,0,1])
        box_gold.add_widget(self.gold_button_text)
        resource_box.add_widget(box_gold)

        box_oil=BoxLayout(orientation="vertical")
        oil_button_image=Button(background_normal=path+"sprites/oil.png", background_down=path+"sprites/oil.png")
        box_oil.add_widget(oil_button_image)
        self.oil_button_text=Button(size_hint=[1,0.08],text="-",background_normal="", background_down="",color=[1,0,1,1],background_color=[0,0,0,1])
        box_oil.add_widget(self.oil_button_text)
        resource_box.add_widget(box_oil)



        box.add_widget(self.panel)
        box_menu_window=BoxLayout() # для меню та вікон
        box.add_widget(box_menu_window)
        box_menu=BoxLayout(orientation="vertical") # ліва панель переключення
        box_menu_window.add_widget(box_menu)

        self.add_widget(box)

        self.all_window_game=ScreenManager(transition=SwapTransition(),size_hint=[4,1])
        self.all_window_game.add_widget(City())
        self.all_window_game.add_widget(Army())    
        self.all_window_game.add_widget(Infrastructure())   
        self.all_window_game.add_widget(Policy())  
        self.all_window_game.add_widget(Trade())  
        box_menu_window.add_widget(self.all_window_game)

        def go_game_city(button):
            self.all_window_game.current="city"
        city_button_menu=Button(background_normal=path+"sprites/city_icon0.png", background_down=path+"sprites/city_icon1.png",
                           font_name="font/7fonts_Knight2.ttf",
        color=[1,1,0,1],background_color=[1,1,0,1],on_press=go_game_city)
        box_menu.add_widget(city_button_menu)

        def go_game_infrastructure(button):
            self.all_window_game.current="infrastructure"
        infrastructure_button_menu=Button(background_normal=path+"sprites/Infrastructure_icon0.png", background_down=path+"sprites/Infrastructure_icon1.png",
                           font_name="font/7fonts_Knight2.ttf",
        color=[1,1,0,1],background_color=[1,1,0,1],on_press=go_game_infrastructure)
        box_menu.add_widget(infrastructure_button_menu)

        def go_game_army(button):
            self.all_window_game.current="army"
        army_button_menu=Button( background_normal=path+"sprites/army.png", background_down=path+"sprites/army2.png",
        color=[1,1,0,1],background_color=[1,1,0,1],on_press=go_game_army)
        box_menu.add_widget(army_button_menu)

        def go_game_policy(button):
            self.all_window_game.current="policy"
        policy_button_menu=Button(background_normal=path+"sprites/policy_icon0.png", background_down=path+"sprites/policy_icon1.png",
                           font_name="font/7fonts_Knight2.ttf",
        color=[1,1,0,1],background_color=[1,1,0,1],on_press=go_game_policy)
        box_menu.add_widget(policy_button_menu)

        def go_game_trade(button):
            self.all_window_game.current="trade"
        trade_button_menu=Button(background_normal=path+"sprites/trade_icon0.png", background_down=path+"sprites/trade_icon1.png",
                           font_name="font/7fonts_Knight2.ttf",
        color=[1,1,0,1],background_color=[1,1,0,1],on_press=go_game_trade)
        box_menu.add_widget(trade_button_menu)

        #window_action=GridLayout(cols=3)
        #box.add_widget(window_action)
        Clock.schedule_interval(self.update,1/60)
    def update(self,clock):
        if all_command:
            _,_,command=heapq.heappop(all_command)
            if command["action"]=="reboot" or command["action"]=="update_resource":
                self.people_button_text.text=str(command["people"])
                self.tree_button_text.text=str(command["tree"])
                self.iron_button_text.text=str(command["iron"])
                self.stone_button_text.text=str(command["stone"])
                self.oil_button_text.text=str(command["oil"])
                self.gold_button_text.text=str(command["gold"])
                self.food_button_text.text=str(command["food"])     
        if resource_mining_speed:
            for res in resource_time_mining_speed:
                pass

    def go_menu(self,button):
        self.manager.current="menu"
class MySettings(Screen): # ігровий клас
    name="settings" # ім'я гри для переходу між вікнами
    def __init__(self): # конструктор класу
        Screen.__init__(self) # звертаємо до конструктора суперкласу
        button_menu=Button(text="Menu",font_size=options["text_size"],
                           font_name="font/7fonts_Knight2.ttf",
        color=[0,0,0.2,0.7],background_color=[0,0,0,0],size_hint=[0.3,0.05],
        pos_hint={'center_x':0.5,'center_y':0.65},on_press=self.go_menu) # кнопка переходу в гру
        self.add_widget(button_menu)
        slide_music=Slider(min=0,max=1,value=options["volume"],size_hint=[0.5,0.1],pos_hint={"center_x":0.5,"center_y":0.55})
        self.add_widget(slide_music)
        def sliders(button,value):
            #list_options[0]=str(value)+"\n"
            file_options=open(path+"file/options.json","w")
            #file_options.writelines(list_options)
            options["volume"]=value
            file_options.write(json.dumps(options))
            file_options.close()
            fon_music.set_volume(value)
        slide_music.bind(value=sliders)

    def go_menu(self,button):
        self.manager.current="menu"
class Records(Screen): # ігровий клас
    name="records" # ім'я гри для переходу між вікнами
    def __init__(self): # конструктор класу
        Screen.__init__(self) # звертаємо до конструктора суперкласу
    def go_menu(self,button):
        self.manager.current="menu"
class Menu(Screen): # ігровий клас
    name="menu" # ім'я гри для переходу між вікнами
    background_menu_pic=path+"sprites/background_menu.png"
    def __init__(self): # конструктор класу
        Screen.__init__(self) # звертаємо до конструктора суперкласу 
        button_play=Button(text="Play",font_size=options["text_size"],
                           font_name="font/7fonts_Knight2.ttf",
        color=[0,0,0.2,0.7],background_color=[0,0,0,0],size_hint=[0.3,0.05],
        pos_hint={'center_x':0.5,'center_y':0.65},on_press=self.go_game) # кнопка переходу в гру
        self.add_widget(button_play)
        button_settings=Button(text="Settings",font_size=options["text_size"],
                           font_name="font/7fonts_Knight2.ttf",
        color=[0,0,0.2,0.7],background_color=[0,0,0,0],size_hint=[0.3,0.05],
        pos_hint={'center_x':0.5,'center_y':0.55},on_press=self.go_settings) # кнопка переходу в гру
        self.add_widget(button_settings)
        button_records=Button(text="Records",font_size=options["text_size"],
                           font_name="font/7fonts_Knight2.ttf",
        color=[0,0,0.2,0.7],background_color=[0,0,0,0],size_hint=[0.3,0.05],
        pos_hint={'center_x':0.5,'center_y':0.45},on_press=self.go_records) # кнопка переходу в гру
        self.add_widget(button_records)
    def go_game(self,button):
        if not options["server_connect"]:
            options["server_connect"]=True
            thred_game.start()
        self.manager.current="game"   
    def go_settings(self,button):
        self.manager.current="settings"  
    def go_records(self,button):
        self.manager.current="records"  
class CivilizationApp(App):
    background_pic=path+"sprites/fon.png"
    def build(self):
        all_windows=ScreenManager(transition=WipeTransition())
        all_windows.add_widget(Menu())
        all_windows.add_widget(Game())
        all_windows.add_widget(MySettings())
        all_windows.add_widget(Records())
        return all_windows
if __name__=="__main__": # якщо запуска'ємо даний файл не як модуль
    CivilizationApp().run() # то запустимо програму на основи головного класу