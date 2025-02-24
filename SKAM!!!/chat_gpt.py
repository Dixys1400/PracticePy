import g4f
import os
import pyfiglet
import xlrd
from openpyxl import load_workbook
from colorama import init, Fore, Style
from pystyle import *
import random
import time              
import requests
from fake_useragent import UserAgent
import subprocess
from colorama import Fore, Style
import colorama

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_console()

print("""

                                            

                   ______  _    _   ______  _______    ______   ______  _______
                  | |     | |  | | | |  | |   | |     | | ____ | |  | \   | |   
                  | |     | |--| | | |__| |   | |     | |  | | | |__|_/   | |   
                  |_|____ |_|  |_| |_|  |_|   |_|     |_|__|_| |_|        |_|   
                                                                                
                    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                    ┃ info: creator:@asphyxia_panic tgc:@xwondedperehod ┃
                    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                    ┃ [1] > задать вопрос      ┃ [2] > выход            ┃
                    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛          
                                                                                
                                                                                
                                                                                
                                                                                """)

choice = input(F"             Введите опцию : " + Style.RESET_ALL)

if choice.lower() == "1":

 user_input = input("             Введите ваш запрос: ")
 print("Обработка...")

 response = g4f.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[{'role': 'user', 'content': user_input}]
 )

 print(response)

if choice.lower() == "1":
 exit()
 
else:
    print("             Неверный выбор")