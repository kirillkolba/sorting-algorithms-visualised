import tkinter as tk

objAmount = 0
objs = []
objBools = []

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
    if (objAmount > 0):
        wind1.quit()
    if (objAmount > 35):
        objAmount = 35
button = tk.Button(wind1, text="Начать сортировку", command=onclick)
button.pack()
wind1.mainloop()
#---------------------------------Экран с вводом количества объектов-----------------------------------


#----------------------------------------Создание графика списка--------------------------------------
wind1.quit()
wind1.destroy()
for i in range(objAmount):
    objs.append(i + 1)
    objBools.append(True)

mw = tk.Tk()
mw.config(bg="blue")

width = objAmount * 50 + 100
height = 200 + objAmount * 5

mw.geometry(str(width) + "x" + str(height))

canvas = tk.Canvas(mw, width = width, height = height)

for i in range(len(objs)):
    canvas.create_rectangle(50 * i + 50, height - 150, 50 * (i + 2), height - 150 - 5 * objs[i], fill="green" if objBools[i] else "red",
                            outline="green" if objBools[i] else "red", tags="object", )
canvas.pack()

mw.mainloop()
#----------------------------------------Создание графика списка--------------------------------------
