from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import tkinter as tk
from tkinter import simpledialog
import socket
import winreg

print('This program is written by Mohammadsadegh Salimian and Mehrdad Shariati \nEmail:sadeghsalimian.98@gmail.com')


def get_credentials():
    root = tk.Tk()
    root.withdraw()  
    username = simpledialog.askstring("Input", "This program is written by Mohammadsadegh Salimian and Mehrdad Shariati, Email:sadeghsalimian.98@gmail.com\nEnter your username:")
    password = simpledialog.askstring("Input", "Enter your password:", show='*')
    runtime = simpledialog.askstring("Input", "Enter the period time to login by minutes:")
    
    return username, password,runtime


username, password,runtime = get_credentials()
runtime=float(runtime)
driver_path = 'C:/chromedriver.exe'  


chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--headless')  
chrome_options.add_argument('--disable-gpu')  
chrome_options.add_argument('--no-sandbox') 
chrome_options.add_argument('--disable-dev-shm-usage') 

service = Service(driver_path)

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

def check_and_disable_proxy():
    try:
        # Open the registry key where proxy settings are stored
        registry_path = r"Software\Microsoft\Windows\CurrentVersion\Internet Settings"
        reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, registry_path, 0, winreg.KEY_ALL_ACCESS)
        
        # Read the current proxy settings
        proxy_enable, _ = winreg.QueryValueEx(reg_key, "ProxyEnable")

        # Check if proxy is enabled
        if proxy_enable == 1:
            print("Proxy is enabled. Disabling now...")
            winreg.SetValueEx(reg_key, "ProxyEnable", 0, winreg.REG_DWORD, 0)
            print("Proxy has been disabled.")
            print("Proxy can be abled manually.")
        else:
            print("Proxy is already disabled.")

        # Close the registry key
        winreg.CloseKey(reg_key)

    except FileNotFoundError:
        print("Proxy settings not found in the registry.")
    except PermissionError:
        print("Permission denied. Run the script with administrative privileges.")
    except Exception as e:
        print(f"An error occurred: {e}")


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


        time.sleep(2)
        # Check if login was successful by looking for a specific element that appears post-login
        if "portal" not in driver.current_url:  
            time.sleep(1)
            print("Logged in successfully!")
        else:
            print("Failed to log in. Please check your credentials or login flow.")
    except Exception as e:

        print(f"An error occurred: {e}")
        print('trying to disable proxy')
        check_and_disable_proxy()
        try:
            driver.get('https://internet.ut.ac.ir:1003/portal?')
            time.sleep(2) 
            username_input = driver.find_element(By.NAME, 'username') 
            password_input = driver.find_element(By.NAME, 'password') 
            username_input.send_keys(username)
            password_input.send_keys(password)
            password_input.send_keys(Keys.RETURN)
        except:
            print("An error occurred. Turn off VPN manually")  

    finally:
        driver.quit()

# Run the login function
while True:
    if not check_internet():
        login()
    print(f"Waiting for {runtime} minutes before the next attempt \n")
    time.sleep(round(float(60*runtime)))
    