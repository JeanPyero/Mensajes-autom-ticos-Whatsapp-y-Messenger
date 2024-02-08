import pyautogui #will send the message
import webbrowser #will open the url
import datetime #alerts us of the time
from time import sleep #timed actions

flag = 1 #variable to control the end of the while
id = '100027781651271' #recipient id in messenger(on the facebook messenger URL)

def send():
    global flag
    flag = 0
    
    # Messenger Open
    webbrowser.open(f'https://www.facebook.com/messages/t/{id}')
    sleep(7)
    
    # Send message
    pyautogui.typewrite("Hola desde Python")
    pyautogui.press("enter")
    return flag
# While that controls the message sending time
while flag:
    current_time = datetime.datetime.now().strftime('%H:%M')
    if current_time == '00:00':
        flag = send()
        sleep(3)  # Wait 1 minute before exiting the loop
    else:
        sleep(1)  # Wait 1 second before checking again

