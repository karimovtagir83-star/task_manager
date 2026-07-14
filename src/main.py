import manager as mn


mn.load_tasks()


def show_menu():
    while True:
        lang = input("Choose language (rus/eng): ").strip().lower()
        if lang == "rus":
            print("""
<команда> <аргумент(если есть)> <описание>

Команды:

add <название>  <описание> : создать и дать название |
list : список задач |
complete <title> / <all> : задача выполнена / все задачи выполнены |
delete <title> / <all> : удалить задачу / удалить все |
exit : выйти |
""")
            break

        elif lang == "eng":
            print("""
<command> <argument (if any)> <description>

Commands:

add <text> : create a new task |
list : show all tasks |
complete <title> / <all> : mark a task / all tasks as completed |
delete <title> / <all> : delete a task / delete all tasks |
exit : exit the program |
""")
            break

print("""
=== Task Tracker ===
""")


show_menu()


while True:
    command = input("> ").strip().lower()
    parts = command.split(maxsplit=2)

    if not command:
        continue

    if parts[0] == "add" and len(parts) == 3:
        mn.add_task(parts[1], parts[2])
        mn.save_tasks()

    elif parts[0] == "list":
        mn.list_tasks()
    
    elif parts[0] == "exit":
        mn.save_tasks()
        break
    
    elif parts[0] == "delete" and len(parts) == 2:
        mn.delete_task(parts[1])
        mn.save_tasks()
    
    elif parts[0] == "complete" and len(parts) == 2:
        mn.complete_task(parts[1])
        mn.save_tasks()
    
    else:
        print("Unknown command or invalid argument.")    
