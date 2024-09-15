# UT_Login
This program is useable to login into the University of Tehran internet automatically, since it logs out every 10 hours.

How to Use in Windows:

1- Update/install Google Chrome (Last Version)
Download ChromeDriver from here:
https://googlechromelabs.github.io/chrome-for-testing/
and put it:
'C:\'

2- Then run login_Hidden.exe or login.exe (Hidden Version is more userfriendly but doesnot show errors or outputs)

3- Enter your username and password carefully (If you entered wrong, close the program and rerun it)

4- Enter the period time that program will check status and if its disconnected, it logins (1 mintue is appropariate)

#Done! your internet is connected and will never disconnect again.

How to Use in Linux
1- Install google chrome:
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt-get install -f

2-Download ChromeDriver from here:
https://googlechromelabs.github.io/chrome-for-testing/
then give it executable permissions:
chmod +x /path/to/ChromeDriver

3- Install Selenium Library
4- Run the login_script_Linux.py in terminal
5- Enter your username and password carefully (If you entered wrong, close the program and rerun it)
6- Enter the period time that program will check status and if its disconnected, it logins (1 mintue is appropariate)

Features
Note that if proxy is on, login webpage will not be accessible, so the program try to turn it off which some times doesnot work. Therefore make sure to turn off your vpn/proxy.

