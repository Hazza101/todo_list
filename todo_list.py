

#function that displays to contents of the current todo list

def display_todo(todos):
    print(f"{'#' * 10}Todo list{'#' * 10}")
    for index, todo in enumerate(todos):
        print(f"{index+1}. {todo[0]:<50} {todo[1]:>20}")

    if len(todos) == 0:
        print("Nothing added")

todo_list = []

####main loop of command line application
while True:
    display_todo(todo_list)
    answer = input("\n-->").strip()
    
    #display help
    if answer.strip() in 'help':
        print("commands\n\th or help to see help menu\n\tr[index] to remove\n\td[index] to check a a task\n\tu[index]to uncheck a task\n")
        input()
    
    #this is here for exiting and so elif statements don't break later 'answer[1:].isdigit()'
    elif len(answer) == 1:
        if answer == 'x':
            break
        print("Not enough information")
        input()
        

    #for removing task
    elif answer[0].lower() == 'r' and answer[1:].isdigit():
        try:
            todo_list.pop(int(answer[1:])-1)
        except:
            print(f"Index: {answer[1:]} does not exist")
            input()


    #for checking a task as done 
    elif answer[0].lower() == 'd' and answer[1:].isdigit():
        try:
            print(answer[1:])
            todo_list[int(answer[1:])-1][1] = True
        except:
            print(f"Index: {answer[1:]} does not exist")
            input()


    #for checking a task as complete
    elif answer[0].lower() == 'u' and answer[1:].isdigit():
        try:
            todo_list[int(answer[1:])-1][1] = False
        except:
            print(f"Index: {answer[1:]} does not exist")
            input()

    #makes adding tasks quick
    else:
        todo_list.append([answer, False])        
        
        

    
    
