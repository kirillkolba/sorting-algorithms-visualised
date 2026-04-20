import tkinter as tk

objAmount = 0
objs = []
objBools = []

#---------------------------------Экран с вводом количества объектов-----------------------------------
wind1 = tk.Tk()
wind1.title("Ввод")
wind1.geometry("300x100")
text = tk.Label(wind1, text="Введите количество сортируемых объектов")
text.pack()
objNum = tk.Entry(width=20)
objNum.pack()
def onclick():
    global objAmount
    objAmount = int(objNum.get())
    if (objAmount > 0):
        wind1.quit()
button = tk.Button(wind1, text="Начать сортировку", command=onclick)
button.pack()
wind1.mainloop()
#---------------------------------Экран с вводом количества объектов-----------------------------------


#----------------------------------------Создание графика списка--------------------------------------
wind1.quit()
wind1.destroy()
for i in range(objAmount):
    objs.append(i)
    objBools.append(True)

mw = tk.Tk()
mw.config(bg="blue")

width = objAmount * 50 + 100
height = 200 + objAmount * 5

mw.geometry(str(width) + "x" + str(height))


canvas = tk.Canvas(mw, width = width, height = height)

for i in range(len(objs)):
    canvas.create_rectangle(100, 100, 300, 200, fill="green" if objBools[i] else "red", outline="green" if objBools[i] else "red")
canvas.pack()

mw.mainloop()
#----------------------------------------Создание графика списка--------------------------------------