from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import tkinter as tk
from tkinter import simpledialog
import socket

def get_credentials():
    root = tk.Tk()
    root.withdraw()  
    username = simpledialog.askstring("Input", "Enter your username:")
    password = simpledialog.askstring("Input", "Enter your password:", show='*')
    runtime = simpledialog.askstring("Input", "Enter the period time to login or check internet connection by minutes:")  
    path = simpledialog.askstring("Input", "Enter the Path to Chrome driver, Example: '/path/to/chromedriver':")
    return username, password,runtime,path

username, password,runtime,path= get_credentials()

def check_internet(host="8.8.8.8", port=53, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        print("Internet connection is available.")
        return True
    except socket.error as ex:
        print(f"Connection error: {ex}")
        print("No internet connection.")
        return False

runtime = 0.2
runtime=float(runtime)

driver_path = path 

chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--headless')  
chrome_options.add_argument('--disable-gpu')  
chrome_options.add_argument('--no-sandbox') 
chrome_options.add_argument('--disable-dev-shm-usage') 

service = Service(driver_path)

def login():
    driver = webdriver.Chrome(service=service, options=chrome_options)
    try:
        driver.get('https://internet.ut.ac.ir:1003/portal?')

        time.sleep(2)


        username_input = driver.find_element(By.NAME, 'username')  
        password_input = driver.find_element(By.NAME, 'password')  

        username_input.send_keys(username)
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)

        print('This program is written by Mohammadsadegh Salimian and Mehrdad Shariati, All rights reserved.')

        # Check if login was successful by looking for a specific element that appears post-login
        if "portal" not in driver.current_url: 
            time.sleep(1)
            print("Logged in successfully!")
        else:
            print("Failed to log in. Please check your credentials or login flow.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

while True:
    if not check_internet():
        login()
    print(f"Waiting for {runtime} minutes before the next attempt \n")
    time.sleep(round(float(60*runtime)))