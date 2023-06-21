import os
result=''
def finder_file(name_file, rash, way='D:\\'):
    my_folders=[]
    my_files=[]
    for filename in os.listdir(way):
        f=os.path.join(way,filename)
        file=os.path.join(way,filename)
        if os.path.isdir(f):
            my_folders.append(f)
        if os.path.isfile(file):
            my_files.append(file)
    if os.path.join(way,name_file)+rash in my_files:
        print("Знайдено")
        print(os.path.join(way,name_file) + rash)
        global result
        result=(os.path.join(way,name_file) + rash)
        return True
    else:
        for z in my_folders:
            try:
                way=z
                if finder_file(name_file, rash,way=z):
                    return True
            except PermissionError:
                continue
#What aRee we finding?
def menu():
    x=input(str('Що будемо шукати?\n- '))
    y=input(str('Формат файлу? ( По замовчуванню - .txt/.docx/.exe./.xlsx )\n- '))
    finder_file(x,y)
    def open_exe():
        dia=input('Відкриваємо?\n- ')
        if dia=='+':
            os.startfile(result)
    def open_txt():
        multi=False
        def open_txt_read():
            _file=open(result,'r')
            print(_file.read())
            _file.close()
        def open_txt_write():
            _file=open(result,'w')
            _file.write((input('Файл очищено! Введіть новий текст.\n- '))+' ')
            _file.close()
        def open_txt_append():
            _file=open(result,'r+')
            print(_file.read())
            _file.write((input('Введіть текст для дозапису файлу!\n- '))+' ')
            _file.close()
        while multi==False:
            _mydia=input('Доступні дії: read/write/append/quit\n- ')
            if _mydia=='read': open_txt_read()
            elif _mydia=='write': open_txt_write()
            elif _mydia=='append': open_txt_append()
            elif _mydia=='quit': multi=True
            else: print('Невідома операція')
    if y=='.txt':
        open_txt()
    elif y=='.txt':
        open_exe()

menu()
