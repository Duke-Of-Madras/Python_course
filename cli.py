#from functions import get_todos,write_todos
import functions
import time

now=time.strftime("%b %d, %y %H:%M:%S")
print("it is",now)

while True:
    user_action=input("Type add, show, edit, complete or exit: ")
    user_action=user_action.strip()


    if user_action.startswith("add"):

        todo=user_action[4:]+"\n"
        todos=functions.get_todos()
        todos.append(todo)
        functions.write_todos(todos)
    
    elif user_action.startswith("show"):

        todos=functions.get_todos()
        modified_todos=[i.strip("\n") for i in todos]
        for index,item in enumerate(modified_todos):
            print(f"{index+1}-{item}")
    
    elif user_action.startswith("edit"):
        try:

            number=int(user_action[5:])
            todos=functions.get_todos()
            new_todo=input("Enter the new todo!")
            todos[number-1]=new_todo+"\n"
            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid!")
            continue




    
    elif user_action.startswith("complete"):
        try:
            number=int(user_action[9:])
            todos=functions.get_todos()
            todo_to_remove=todos[number-1].strip("\n")
            todos.pop(number-1)
            functions.write_todos(todos)
            print(f"{todo_to_remove} has been removed!")
        except IndexError:
            print("There is no item with that number")
            continue


       

    elif user_action.startswith("exit"):
        break

    else:
        print("command is not valid! try again!")
            
