def wait_until_saving_end():
    substring ='Saving'
    txt = 'Saving'

    while True:
        time.sleep(1)
        print('still saving')
        image = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
        #image = cv2.bitwise_not(image)

        cv2.imwrite("image1.png", image)
        
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        txt = pytesseract.image_to_string(image)
        print(txt)

        if substring in txt:
            print('waiting to save')
        else:
            print("not found,done saving")
            break

        time.sleep(2)