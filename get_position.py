


# for i in range(10):
#     pyautogui.moveTo(100, 100, duration=0.25)
#     pyautogui.moveTo(200, 100, duration=0.25)
#     pyautogui.moveTo(200, 200, duration=0.25)
#     pyautogui.moveTo(100, 200, duration=0.25)


# print('Press Ctrl-C to quit.')
# try:
#     while True:
#         #pos = pyautogui.position()
#         pos = pyautogui.displayMousePosition()
#         print(pos)
#         # TODO: Get and print the mouse coordinates.

# except KeyboardInterrupt:
#     print('\nDone.')


from pynput import mouse

def on_click(x, y, button, pressed):
    if button == mouse.Button.left:
        print('{} at {}'.format('Pressed Left Click' if pressed else 'Released Left Click', (x, y)))
        return False # Returning False if you need to stop the program when Left clicked.
    else:
        print('{} at {}'.format('Pressed Right Click' if pressed else 'Released Right Click', (x, y)))

while True:
    listener = mouse.Listener(on_click=on_click)
    listener.start()
    listener.join()