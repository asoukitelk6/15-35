'''Менеджер задач
Задача: Создай класс Task, который позволяет управлять задачами (делами). У задачи должны
быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих
(не выполненных) задач.'''

class Task():
    def __init__(self):
        self.tasks = []

    def new_task (self, opis, time, status=False):#Реализуй функцию для добавления задач,
        task={'opis':opis,'time':time,'status':status}
        self.tasks.append(task)
        print(f'задача "{opis}" добавленна')

    def otmetka (self, opis):#отметки выполненных задач
        for task in self.tasks:
            if task['opis'] == opis:
                task['status'] = True
                print(f'Задача с описанием :"{opis}" выполненна')
                break
        else:
            print(f'Задача "{opis}" ненайдена')

    def itog_task (self):#вывода списка текущих (не выполненных) задач.
        print(f'Активные задачи:')
        n = 1
        for task in self.tasks:
            if task['status'] == False:
                print(f'{n}) {task["opis"]} нужно выполнить до {task["time"]}')
                n += 1

manager = Task()
manager.new_task("Купить молоко", "2025-04-10")
manager.new_task("Купить 1", "2025-05-10")

manager.itog_task()

manager.otmetka("Купить1")
manager.otmetka("Купить 1")

manager.itog_task()