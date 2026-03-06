import tkinter as tk
import pygame
import os
from pathlib import Path
import threading
import time
import sys






# Initiate pygame and pygame mixer
pygame.init()
pygame.mixer.init()



#Test music list
# "C:\\Rock-Pop\\"
# "C:\\hoplite_song_hoard"
#"C:\holding_pen"

#Divide path and dir so that list in listbox is readable
hoard_path = Path("C:\\holding_pen")
hoard_list = os.listdir(hoard_path)

#Set mixer end event for continuous play to work
song_end = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(song_end)



# Populate Song Hoard Listbox
     



#Configure tkinter gui
root = tk.Tk()
root.title('Hoplite Music Player')
root.geometry('1200x980+50+50')
root.columnconfigure([1,2,3,4,5], weight=0)
root.columnconfigure([0,6], weight=1)
root.config(background='#33232f')#'#405f74'
#Create canvas to center list boxes better
list_boxes = tk.Canvas(root, width=1200, height=400, background='#33232f')
list_boxes = tk.Frame(background='#33232f')

# Threading Testing
# def test_funk():
#     while True:
#         print("Yo mamma so fat")
#         time.sleep(30)

# tf = threading.Thread(target=test_funk, args=())
# tf.daemon = True
# tf.start()

#Test music list
# "C:\\Rock-Pop\\"
# "C:\\hoplite_song_hoard"
# "C:\\holding_pen"

#Divide path and dir so that list in listbox is readable.
#this program is intended to be used with a 'one file deep' music file
#enter the path to the file in the variable 'hoard_path' below
hoard_path = Path("C:\\holding_pen")
hoard_list = os.listdir(hoard_path)




#Frames to get the background of the listboxes to be the right color
list_boxes = tk.Frame(background='#33232f')

#Song Hoard Listbox
song_hoard_label = tk.Label(list_boxes, height=1, width=1, background='#33232f', 
foreground='#a7edf9', font=('Nirmala UI', 12),text='SONGHOARD' )
song_hoard_list = tk.Listbox(list_boxes, height=30,width=40, selectmode='single',exportselection=False, 
bg='#33232f', fg='#a7edf9', font=('Nirmala UI', 11), selectbackground='#a7edf9', selectforeground='#33232f')
scrollbar_a = tk.Scrollbar(list_boxes, orient=tk.VERTICAL)
song_hoard_list.config(yscrollcommand=scrollbar_a.set)
scrollbar_a.config(command=song_hoard_list.yview)

# Active Queue Listbox
active_queue_label = tk.Label(list_boxes, height=1, width=1, background='#33232f', 
foreground='#a7edf9', font=('Nirmala UI', 12),text='ACTIVE QUEUE' )
active_queue = tk.Listbox(list_boxes, height=30,width=40, selectmode='single',exportselection=False, 
bg='#33232f', fg='#a7edf9', font=('Nirmala UI',11),selectbackground='#a7edf9', selectforeground='#33232f')
scrollbar_b = tk.Scrollbar(list_boxes, orient=tk.VERTICAL, background='#33232f')
active_queue.config(yscrollcommand=scrollbar_b.set)
scrollbar_b.config(command=active_queue.yview )

for song in hoard_list:
    song_hoard_list.insert('end', song)


class Func_butt(tk.Button):
    """This class creates the control buttons"""
    def __init__(self, master, text, command, **kwargs):
        super().__init__(master, text= text, command= command)

        self['font'] = ("Nirmala UI", 12)
        self['background'] = ('#33232f') #'#d3c0c6'
        self['foreground'] = ('#a7edf9') #'#273951'
        self['text'] = text
        self['command'] = command
        self['activeforeground'] = '#273951'
        self['state'] = 'normal'
        self['borderwidth'] = 5
        
    

        self.config(**kwargs)
 
live_queue_list = []
def transfer_to_queue():
    #Get selected song from song hoard listbox and add to active queue listbox
    for i in song_hoard_list.curselection():
        selected_song = song_hoard_list.get(i)
        live_queue_list.append(selected_song)
        active_queue.insert('end', live_queue_list[-1])
        if len(live_queue_list) >= 1:
            if cont.is_alive():
                pass
            else:
                cont.start()
        

            
        
        
        
        



def continuous_play():
    current_song_index = 0
    def cont_play(index, live_queue_list):
        

        if index < len(live_queue_list):
            


            song = (f'{hoard_path}//{live_queue_list[index]}')
            print(song)
            pygame.mixer.music.load(song)
            pygame.mixer.music.rewind()
            pygame.mixer.music.play()
            return index + 1

            
            
            
    
    
    current_song_index = cont_play(current_song_index, live_queue_list)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == song_end:
                current_song_index = cont_play(current_song_index, live_queue_list)
                if current_song_index >= len(live_queue_list):
                    current_song_index = 0
                    
                
        
        


        pygame.time.Clock().tick(10)

   

    pygame.QUIT
cont = threading.Thread(target=continuous_play, args=())
cont.daemon = True


def stop_func():
    pygame.mixer.music.stop()
def play_func():
    pygame.mixer.music.play()
def pause_func():
    pygame.mixer.music.pause()
def unpause_func():
    pygame.mixer.music.unpause()






add_to_q_butt = Func_butt(list_boxes,'ADD TO QUEUE', command=transfer_to_queue, width=9)
active_queue_label.grid(row=1, column=2, columnspan=1, padx=5, sticky='ew')
# stop_butt = Func_butt(root,'STOP', command=stop_func, width=9)
# stop_butt.grid(row=1, column=2, sticky='ew')
# play_butt = Func_butt(root,'PLAY',command=play_func, width=9)
# play_butt.grid(row=1, column=3, sticky='ew', )
# pause_butt = Func_butt(root,'PAUSE', command=pause_func, width=9)
# pause_butt.grid(row=1, column=4, sticky='ew')
# unpause_butt = Func_butt(root,'UNPAUSE', command=unpause_func, width=9)
# unpause_butt.grid(row=1, column=5, sticky='ew')



list_boxes.grid(row=5, column=1, columnspan=6,padx=5, pady=5, sticky='ew')


song_hoard_label.grid(row=2, column=0, columnspan=1, padx=5, sticky='ew')
active_queue_label.grid(row=2, column=2, columnspan=1, padx=5, sticky='ew')
# mixtape_list_label.grid(row=2, column=4, columnspan=1, padx=5, sticky='ew')

song_hoard_list.grid(row=3, column=0, columnspan=1, padx=5, pady=5, sticky='ew')
scrollbar_a.grid(row=3, column=1, columnspan=1, sticky=tk.N+tk.S)
active_queue.grid(row=3, column=2, columnspan=1)
scrollbar_b.grid(row=3, column=3,columnspan=1, sticky=tk.N+tk.S)
add_to_q_butt.grid(row=5, column=2, columnspan=1, sticky='ew')



root.mainloop()
