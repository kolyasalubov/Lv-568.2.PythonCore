from tkinter import *
import pygame
from tkinter import filedialog
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk

root = Tk()
root.title("My first Player")
root.iconbitmap('icons/icon.ico')
root.geometry('940x450')

# bg = PhotoImage(file='icons/background.png')

# my_canvas = Canvas(root, width=940, height=400)
# my_canvas.pack(fill='both', expand=True)
# # IMG into Canvas
# my_canvas.create_image(0, 0, image=bg, anchor='nw')


pygame.mixer.init()


def song_play_time():
    # To avoid duble running function
    # if stopped:
    #     return

    current_time = pygame.mixer.music.get_pos() / 1000

    # Get data from label
    # slider_label.config(text=f'Slider:  {int(my_slider.get())} and Song position:  {int(current_time)}')

    converted_current_time = time.strftime('%H:%M:%S', time.gmtime(current_time))

    # Get currently playing song
    song = song_box.get(ACTIVE)

    song = f"C:/Users/STRIX/Desktop/IT/My_player/Song_Playlist/{song}"

    # Get song length
    song_mut = MP3(song)
    global song_length
    song_length = song_mut.info.length
    converted_song_length = time.strftime('%H:%M:%S', time.gmtime(song_length))

    current_time += 1 #sec

    if int(my_slider.get()) == int(song_length):
        status_bar.config(text=f'Time: {converted_song_length} of {converted_song_length}   ')

    elif paused:
        pass

    # Current_time increase to == song time position
    elif int(my_slider.get()) == int(current_time):
        # song_length == slider position
        slider_position = int(song_length)
        my_slider.config(to=slider_position, value=int(current_time))

    else:
        # song_length == slider position
        slider_position = int(song_length)
        my_slider.config(to=slider_position, value=int(my_slider.get()))

        converted_current_time = time.strftime('%H:%M:%S', time.gmtime(int(my_slider.get())))

        status_bar.config(text=f'Time: {converted_current_time} of {converted_song_length}   ')

        # Moving slider
        next_time = int(my_slider.get()) + 1
        my_slider.config(value=next_time)

    # Slider according music value
    # my_slider.config(value=int(current_time))
    time_label = Label(root, text=int(current_time))
    time_label.pack(pady=20)

    status_bar.after(1000, song_play_time)


def add_song():
    song = filedialog.askopenfilename(initialdir='Song_Playlist', title="chose the song",
                                      filetypes=(("mp3 Files", "*.mp3"), ("wav Files", "*.wav"),))
    song = song.replace("C:/Users/STRIX/Desktop/IT/My_player/Song_Playlist/", "")
    song_box.insert(END, song)


def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir='Song_Playlist', title="chose the song",
                                        filetypes=(("mp3 Files", "*.mp3"), ("wav Files", "*.wav"),))
    for song in songs:
        song = song.replace("C:/Users/STRIX/Desktop/IT/My_player/Song_Playlist/", "")
        song_box.insert(END, song)


def play():
    song = song_box.get(ACTIVE)
    song = f"C:/Users/STRIX/Desktop/IT/My_player/Song_Playlist/{song}"

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # Call play time function
    song_play_time()

    # Update slider
    slider_position = int(song_length)
    my_slider.config(to=slider_position, value=0)


# global stopped
# stopeed = False
def stop():
    # Reset slider and status bar
    status_bar.config(text='')
    my_slider.config(value=0)
    # Stop function
    pygame.mixer.music.stop()
    song_box.select_clear(ACTIVE)

    # Clear status bar
    status_bar.config(text='')

    # Set stop variable
    # global stopped
    # stopeed = True

    slider_position = int(song_length)
    my_slider.config(to=slider_position, value=0)


# Pause variable
global paused
paused = False


def pause(is_paused):
    global paused
    paused = is_paused

    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True


def next_song():
    # status_bar.config(text='')
    # my_slider.config(value=0)

    # Define number of song from song_box
    next_one = song_box.curselection()
    next_one = next_one[0] + 1

    song = song_box.get(next_one)

    song = f"C:/Users/STRIX/Desktop/IT/My_player/Song_Playlist/{song}"

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    song_box.selection_clear(0, END)
    song_box.activate(next_one)
    song_box.select_set(next_one, last=None)

    slider_position = int(song_length)
    my_slider.config(to=slider_position, value=0)


def prev_song():
    # status_bar.config(text='')
    # my_slider.config(value=0)

    # Define number of song from song_box
    next_one = song_box.curselection()
    next_one = next_one[0] - 1

    song = song_box.get(next_one)

    song = f"C:/Users/STRIX/Desktop/IT/My_player/Song_Playlist/{song}"

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    song_box.selection_clear(0, END)
    song_box.activate(next_one)
    song_box.select_set(next_one, last=None)

    slider_position = int(song_length)
    my_slider.config(to=slider_position, value=0)


def delete_song():
    stop()
    song_box.delete(ANCHOR)
    pygame.mixer.music.stop()


def delete_all_songs():
    stop()
    song_box.delete(0, END)
    pygame.mixer.music.stop()


def slide(x):
    # slider_label.config(text=f'{int(my_slider.get())} of {int(song_length)}')
    song = song_box.get(ACTIVE)
    song = f"C:/Users/STRIX/Desktop/IT/My_player/Song_Playlist/{song}"

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0, start=int(my_slider.get()))


# Playlist window
song_box = Listbox(root, bg='white', fg='black', width='60', selectbackground="black", selectforeground='white')
song_box.pack(pady=20)

# Buttons icons
previous_btn_icon = PhotoImage(file='icons/player_prev.png')
rew_btn_icon = PhotoImage(file='icons/player_rew.png')
fwd_btn_icon = PhotoImage(file='icons/player_fwd.png')
next_btn_icon = PhotoImage(file='icons/player_end.png')
play_btn_icon = PhotoImage(file='icons/player_play.png')
pause_btn_icon = PhotoImage(file='icons/player_pause.png')
stop_btn_icon = PhotoImage(file='icons/player_stop.png')

# Creating control buttons frame
controls_frame = Frame(root)
controls_frame.pack()

# Creating control buttons
previous_btn = Button(controls_frame, image=previous_btn_icon, borderwidth=0, command=prev_song)
rew_btn = Button(controls_frame, image=rew_btn_icon, borderwidth=0)
fwd_btn = Button(controls_frame, image=fwd_btn_icon, borderwidth=0)
next_btn = Button(controls_frame, image=next_btn_icon, borderwidth=0, command=next_song)
play_btn = Button(controls_frame, image=play_btn_icon, borderwidth=0, command=play)
pause_btn = Button(controls_frame, image=pause_btn_icon, borderwidth=0, command=lambda: pause(paused))
stop_btn = Button(controls_frame, image=stop_btn_icon, borderwidth=0, command=stop)

previous_btn.grid(row=0, column=0)
# rew_btn.grid(row=0, column=1)
# fwd_btn.grid(row=0, column=5)
next_btn.grid(row=0, column=6)
play_btn.grid(row=0, column=2)
pause_btn.grid(row=0, column=3)
stop_btn.grid(row=0, column=4)

# Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add song
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label='Add songs', menu=add_song_menu)
add_song_menu.add_command(label='Add song to playlist', command=add_song)

# Add many songs
add_song_menu.add_command(label='Add many song to playlist', command=add_many_songs)

# Song menu
remove_song_menu = Menu(my_menu)
my_menu.add_cascade(label='Remove Songs', menu=remove_song_menu)
remove_song_menu.add_command(label='Del a song', command=delete_song)
remove_song_menu.add_command(label='Del all songs', command=delete_all_songs)

# Cretaing music duration bar
status_bar = Label(root, text='', bd=1, relief=GROOVE, anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=2)

# Creating slider
my_slider = ttk.Scale(root, from_=0, to=100, orient=HORIZONTAL, value=0, command=slide, length=360)
my_slider.pack(pady=30)

# slider_label = Label(root, text='0')
# slider_label.pack(pady=10)

root.mainloop()
