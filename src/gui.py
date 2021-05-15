import processviewer

import os
import tkinter

def gettheme():
    theme = {}
    theme['fg'] = 'white'
    theme['bg'] = '#0E0F13'
    theme['font'] = 'Yu Gothic UI Light'
    theme['text'] = 'Yu Gothic UI Bold'
    theme['light'] = '#008AE6'
    theme['warn'] = '#fc9d19'
    theme['critical'] = '#fc3b19'
    theme['ok'] = '#28ff02'
    return theme

win = tkinter.Tk()
win.title('ProcessViewer')
win.config(bg=gettheme()['bg'])
win.geometry('500x750')
def loadicon():
    return win.iconphoto(False, tkinter.PhotoImage(file='media/icon.png'))

def info(task):
    win = tkinter.Tk()
    win.title('ProcessViewer - ' + task['name'])
    win.config(bg=gettheme()['bg'])
    win.geometry('400x400')
    win.iconbitmap('media/icon.ico') #idc if this works or not

    tkinter.Label(win,
        fg=gettheme()['fg'],
        bg=gettheme()['bg'],
        font=(gettheme()['font'], 20),
        text=task['name'],
    ).pack()

    pid_list = '\n'.join(str(task['pids']).replace('[', '').replace(']', '').replace(',', '').split())

    tkinter.Label(win,
        fg=gettheme()['fg'],
        bg=gettheme()['bg'],
        font=(gettheme()['font'], 15),
        text=pid_list,
        wrap='300'
    ).pack()

    win.mainloop()

for p in processviewer.tasks()[:15]:
    process_frame = tkinter.Frame(win)
    process_frame.pack()

    p_name = p["name"].split(".")[0]
    if len(p_name) > 14: tabs = '\t'
    elif len(p_name) > 6: tabs = '\t\t' 
    else: tabs = '\t\t\t'

    tkinter.Button(process_frame,
        fg=gettheme()['fg'],
        bg=gettheme()['bg'],
        font=(gettheme()['font'], 15),
        text=f'{p["instances"]}x {p_name}{tabs}{round(p["memory"]/1024)} MB',
        relief='flat',
        command=lambda p=p: info(p),
        activebackground=gettheme()['light'],
        activeforeground=gettheme()['fg']
        ).pack(side='left')

    tkinter.Button(process_frame,
        fg=gettheme()['critical'],
        bg=gettheme()['bg'],
        font=(gettheme()['font'], 15),
        text=f'❌',
        relief='flat',
        command=lambda p=p: processviewer.kill(p),
        activebackground=gettheme()['light'],
        activeforeground=gettheme()['fg']
        ).pack(side='right')

    tkinter.Button(process_frame,
        fg=gettheme()['light'],
        bg=gettheme()['bg'],
        font=(gettheme()['font'], 15),
        text=f'➕',
        relief='flat',
        command=lambda p=p: print(p),
        activebackground=gettheme()['light'],
        activeforeground=gettheme()['fg']
        ).pack(side='right')
       
loadicon()

win.mainloop()