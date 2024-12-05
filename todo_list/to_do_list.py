import csv
import sys

class List_Actions:
    file_name = 'todo_list.csv'
    def __init__(self):
        pass
    @staticmethod
    def display_todo_list():
        tasks = []
        with open(List_Actions.file_name,'r') as file:
            task_reader = csv.reader(file)
            next(task_reader)
            for row in task_reader:
                tasks.append(row)
        return tasks
    
    def add_task(self):
        while True:
            try:
                task = input('Enter your task(ex. Clean my room): ')
                if task.isdigit():
                    raise ValueError
                break
            except ValueError:
                print()
                print('Only numerical tasks are not allowed. Please try again.')
                print()
                continue
        completion = 'incomplete'
        with open(List_Actions.file_name,'r') as file:
            reader = csv.reader(file)
            next(reader)
            num_of_lines = []
            for line in reader:
                num_of_lines.append(int(line[0]))
            if not num_of_lines:
                self.task_number = 1
            else:
                self.task_number = num_of_lines[-1]+1
        to_append = [str(self.task_number),task,completion]
        with open(List_Actions.file_name,'a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(to_append)
        print()
        print('Task added.')
        print()    

    def delete_task(self):
        while True:
            try:
                filtered_tasks = []
                deletion = int(input('Enter which task to delete: '))
                with open(List_Actions.file_name,'r',) as file:
                    Tasks = csv.reader(file)
                    header = next(Tasks)
                    for task in Tasks:
                        task_num = task[0].strip()
                        if int(task_num) == deletion:
                            continue
                        filtered_tasks.append(task)
                with open(List_Actions.file_name,'w',newline='') as file:
                    task_writer = csv.writer(file)
                    task_writer.writerow(header)
                    task_writer.writerows(filtered_tasks)
                print()
                print('Task deleted.')
                print()
                self.task_number-=1
                break
            except ValueError:
                print('Invalid Task. Please Try Again.')
                continue
    @staticmethod
    def mark_task():
        while True:
            try:
                filtered_tasks = []
                mark = int(input('Enter which task you would like to complete: '))
                with open(List_Actions.file_name,'r',) as file:
                    Tasks = csv.reader(file)
                    header = next(Tasks)
                    for task in Tasks:
                        task_num = task[0].strip()
                        if int(task_num) == mark:
                            task[2] = 'complete'
                        filtered_tasks.append(task)
                with open(List_Actions.file_name,'w',newline='') as file:
                    task_writer = csv.writer(file)
                    task_writer.writerow(header)
                    task_writer.writerows(filtered_tasks)
                print()
                print('Task marked as complete.')
                print()
                break
            except ValueError:
                print()
                print('Invalid Task. Please Try Again.')
                print()
                continue        
def main():
    user = List_Actions()
    while True:
        try:
            action = int(input('''Enter you action(1, 2, 3, 4, or 5):
1. Display current todo list
2. Add a task to todo list
3. Delete item from todo list
4. Mark a task as complete
5. Exit todo list
'''))
            if action == 1:
                todo_list = user.display_todo_list()
                if not todo_list:
                    print()
                    print('Todo list is empty.')
                    print()
                else:
                    print('''         Todo List
---------------------------''')
                    for task in todo_list:
                        print(f'{task[0]}. {task[1]} [{task[2]}]')
                    print()
                continue
            elif action == 2:
                todo_list = user.display_todo_list()
                print('''         Todo List
---------------------------''')
                for task in todo_list:
                    print(f'{task[0]}. {task[1]} [{task[2]}]')
                print()
                user.add_task()
                continue
            elif action == 3:
                todo_list = user.display_todo_list()
                if not todo_list:
                    print()
                    print('Todo list is empty.')
                    print()
                else:
                    print('''         Todo List
    ---------------------------''')
                    for task in todo_list:
                        print(f'{task[0]}. {task[1]} [{task[2]}]')
                    print()
                    user.delete_task()
                continue
            elif action == 4:
                todo_list = user.display_todo_list()
                if not todo_list:
                    print()
                    print('Todo list is empty.')
                    print()
                else:
                    print('''         Todo List
    ---------------------------''')
                    for task in todo_list:
                        print(f'{task[0]}. {task[1]} [{task[2]}]')
                    print()       
                user.mark_task()         
                continue
            elif action == 5:
                print('Thank you!')
                sys.exit()
            else:
                raise ValueError
        except ValueError:
            print('Invalid Action. Please Try Again.')
            continue
if __name__ == '__main__':
    main()