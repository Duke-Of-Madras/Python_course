def get_todos(file="todos.txt"):
    with open(file,"r") as file:
        todos=file.readlines()
    
    return todos

def write_todos(todos_arg,filepath="todos.txt",):
    file=open(filepath,"w")
    file.writelines(todos_arg)

if __name__=="__main__":
    print("Hello")