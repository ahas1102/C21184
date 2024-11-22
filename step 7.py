class Task:
    def __init__(self, title):
        self.title = title
        self.is_completed = False

    def mark_completed(self):
        self.is_completed = True

    def __str__(self):
        return f"{self.title} ({'Виконано' if self.is_completed else 'Не виконано'})"


tasks = []


tasks.append(Task("Написати програму"))
tasks.append(Task("Здати звіт"))


for task in tasks:
    print(task)


tasks[1].mark_completed()


print("\nОновлений список завдань:")
for task in tasks:
    print(task)