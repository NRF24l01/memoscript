import hashlib
from random import choice
from tkinter import filedialog

def error(er):
    while True:
        file = open('vords.txt', 'r', encoding="UTF-8")  # открываем файл smiles.txt для чтения (r)
        s = file.read()  # считываем все содержимое файла в переменную
        file.close()
        text = s.split("\n")
        txt = choice(text)
        print(txt)
        fn = hashlib.md5(txt.encode()).hexdigest()+".txt"
        print(fn)
        file = open(fn, 'w')
        file.write(er)  # записываем строку в файл
        file.close()  # закрываем файл

fName = filedialog.askopenfilename()
if fName.split(".")[-1] != "memoscript":
    exit("Your file must last to .memoscript!!!!!!!!!!!!!!!!!!!!!!!!!")
with open(fName, 'r', encoding="UTF-8") as s:
    d = s.read()
    script = d.split('\n')
    print(script)