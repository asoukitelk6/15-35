'''Менеджер задач
Задача: Создай класс Task, который позволяет управлять задачами (делами). У задачи должны
быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих
(не выполненных) задач.'''

class Task():
    def __init__(self):
        self.tasks = []

    def new_task (self, description, term, status=False):#Реализуй функцию для добавления задач,
        task={'description':description,'term':term,'status':status}
        self.tasks.append(task)
        print(f'задача "{description}" добавленна')

    def complete_task (self, description):#отметки выполненных задач
        for task in self.tasks:
            if task['description'] == description:
                task['status'] = True
                print(f'Задача с описанием :"{description}" выполненна')
                break
        else:
            print(f'Задача "{description}" ненайдена')

    def show_current_tasks (self):#вывода списка текущих (не выполненных) задач.
        print(f'Активные задачи:')
        n = 1
        for task in self.tasks:
            if task['status'] == False:
                print(f'{n}) {task["description"]} нужно выполнить до {task["term"]}')
                n += 1

manager = Task()
manager.new_task("Купить молоко", "2025-04-10")
manager.new_task("Купить 1", "2025-05-10")

manager.show_current_tasks()

manager.complete_task("Купить1")
manager.complete_task("Купить 1")

manager.show_current_tasks()