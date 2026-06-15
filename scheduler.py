import heapq

class TaskScheduler:
    def __init__(self):
        self.heap = []
        self.counter = 0  # to handle tasks with same priority

    def add_task(self, name, priority, deadline):
        # Lower priority number = higher importance (1 is most urgent)
        heapq.heappush(self.heap, (priority, self.counter, name, deadline))
        self.counter += 1
        print(f"Added task: '{name}' (priority {priority}, deadline {deadline})")

    def execute_next(self):
        if not self.heap:
            print("No tasks remaining.")
            return None
        priority, _, name, deadline = heapq.heappop(self.heap)
        print(f"Executing: '{name}' (priority {priority}, deadline {deadline})")
        return name

    def view_queue(self):
        if not self.heap:
            print("Queue is empty.")
            return
        print("\nCurrent task queue (in execution order):")
        sorted_tasks = sorted(self.heap)
        for i, (priority, _, name, deadline) in enumerate(sorted_tasks, 1):
            print(f"{i}. '{name}' - Priority: {priority}, Deadline: {deadline}")
        print()


# Demo run
if __name__ == "__main__":
    scheduler = TaskScheduler()

    scheduler.add_task("Submit assignment", priority=1, deadline="2026-06-20")
    scheduler.add_task("Reply to emails", priority=3, deadline="2026-06-18")
    scheduler.add_task("Fix bug in project", priority=2, deadline="2026-06-19")
    scheduler.add_task("Plan weekend trip", priority=5, deadline="2026-06-25")
    scheduler.add_task("Prepare presentation", priority=1, deadline="2026-06-21")

    scheduler.view_queue()

    print("\n--- Executing tasks in priority order ---")
    scheduler.execute_next()
    scheduler.execute_next()
    scheduler.execute_next()

    scheduler.view_queue()
# Interactive run
if __name__ == "__main__":
    scheduler = TaskScheduler()

    print("=== Task Scheduler ===")
    print("Add tasks, then execute them in priority order.\n")

    while True:
        print("\nOptions: [1] Add task  [2] Execute next task  [3] View queue  [4] Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Task name: ")
            priority = int(input("Priority (lower number = more urgent): "))
            deadline = input("Deadline (e.g. 2026-06-20): ")
            scheduler.add_task(name, priority, deadline)

        elif choice == "2":
            scheduler.execute_next()

        elif choice == "3":
            scheduler.view_queue()

        elif choice == "4":
            print("Exiting scheduler. Goodbye!")
            break

        else:
            print("Invalid option, try again.")