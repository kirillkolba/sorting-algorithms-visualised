import tkinter as tk
import random
import time

objAmount = 0
objs = []
objBools = []
objsVisual = []
isItFinished = False

#---------------------------------Экран с вводом количества объектов-----------------------------------
wind1 = tk.Tk()
wind1.title("Ввод")
wind1.geometry("330x80")
text = tk.Label(wind1, text="Введите количество сортируемых объектов (макс. - 35)")
text.pack()
objNum = tk.Entry(width=20)
objNum.pack()
def onclick():
    global objAmount
    objAmount = int(objNum.get())
    if objAmount > 0:
        wind1.quit()
    if objAmount > 35:
        objAmount = 35
button = tk.Button(wind1, text="Начать сортировку", command=onclick)
button.pack()
wind1.mainloop()
wind1.quit()
wind1.destroy()
#---------------------------------Экран с вводом количества объектов-----------------------------------
#-------------------------------------------Создание списка-------------------------------------------
for i in range(objAmount):
    objs.append(i + 1)
    objBools.append(True)
#-------------------------------------------Создание списка-------------------------------------------
#----------------------------------------Создание графика списка--------------------------------------
mw = tk.Tk()
mw.config(bg="black")
width = objAmount * 50 + 100
height = objAmount * 10 + 30
mw.geometry(str(width) + "x" + str(height))
def create_graph():
    canva = tk.Canvas(mw, width = width, height = height)
    for k in range(len(objs)):
        objsVisual.append(canva.create_rectangle(50 * k + 50, height, 50 * (k + 2) - 10, height - 10 * objs[k],
        fill="green" if objBools[k] else "red",outline="green" if objBools[k] else "red", tags="object", ))
    canva.pack()
    mw.update()
    canva.destroy()
#----------------------------------------Создание графика списка--------------------------------------
#---------------------------------------------"Сортировка"--------------------------------------------
def sort():
    for l in range(len(objs)):
        ran = random.randint(0, len(objs) - 1)
        a = objs[ran]
        objs[ran] = objs[l]
        objs[l] = a
#---------------------------------------------"Сортировка"--------------------------------------------
#-----------------------------------------------Проверка----------------------------------------------
def check():
    global isItFinished
    isItFinished = True
    for l in range(len(objs)):
        a = 0
        for k in range(len(objs)):
            if objs[l] > objs[k]:
                a+=1
        if a == l:
            objBools[l] = True
        else:
            objBools[l] = False
    for m in range(len(objs)):
        if not objBools[m]:
            isItFinished = False
#-----------------------------------------------Проверка----------------------------------------------

create_graph()
while not isItFinished:
    sort()
    check()
    create_graph()
    time.sleep(0.4)
    mw.update()
mw.mainloop()
