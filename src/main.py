class Task:
    def __init__(self, title, complete):
        self.title = title
        self.complete = complete


print("=== Task Tracker (без сохранения) ===")
print("Команды: add / list / done / delete / exit")
list = list()
while True:
    a = input("").strip()
    if a == "add":
        b = input("Введите текст: ")
        list.append(Task(b, False))
    elif a == "list":
        for i in list:
            print(f"{i.title} {i.complete}")
    elif a == "exit":
        break
    elif a == "delete":
        b = input("Введите название: ")
        for i in list:
            if i.title == b:
                list.remove(i)
    elif a == "done":
        b = input("Введите название")
        for i in list:
            if i.title == b:
                i.complete = True
    else:
        print("Неизвестная комманда")

        
    
                
                
    



        

        


































