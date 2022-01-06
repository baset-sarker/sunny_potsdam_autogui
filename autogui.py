import pyautogui,time

def record_start(recording_time):
    print("record stared at:",time.strftime("%Y-%m-%d %H:%M:%S"))
    print("recording duration:",recording_time," sec")
    pyautogui.moveTo(173, 976, duration=0.25)
    pyautogui.click()
    time.sleep(recording_time)

def record_stop():
    print("record stop at:",time.strftime("%Y-%m-%d %H:%M:%S"))
    pyautogui.moveTo(173, 976, duration=0.25)
    pyautogui.click()
    time.sleep(1)

def go_recording_mode():
    print("select recoring mode")
    pyautogui.moveTo(123, 963, duration=0.25)
    pyautogui.click()
    time.sleep(1)

def save_project():
    pyautogui.hotkey('ctrl','s')
    print("saved at:",time.strftime("%Y-%m-%d %H:%M:%S"))
    time.sleep(1)


def wait_to_save():
    while True:
        #p = pyautogui.locateOnScreen('united.png',grayscale=True,confidence=.6)
        p = pyautogui.locateOnScreen('united.png',grayscale=False)
        if p is not None:
            button7x, button7y = pyautogui.center(p)
            pyautogui.moveTo(button7x, button7y, duration=0.25)
            print('waiting until save finished..')
        else:
            break
        time.sleep(1)


print("Waiting 5 second to start.. please get ready the application..")
time.sleep(5)

while True:
    recording_time = 5

    time.sleep(1)
    go_recording_mode()
    time.sleep(2)
    #go_recording_mode()

    record_start(recording_time)
    record_stop()
    save_project()
    wait_to_save()
    print("################")

    