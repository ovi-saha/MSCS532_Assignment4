import heapq

# The Task class will store the details of each task
class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        #Initializing a task with its attributes: task_id, priority, arrival_time, and deadline
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __repr__(self):
        return f"(TaskID: {self.task_id}, Priority: {self.priority})"

# This class will use a max-heap to implement the priority queue operations
class PriorityQueue:
    def __init__(self):
        # Initializing the priority queue with an empty heap and task_map
        self.heap = []
        self.task_map = {}  # Maps task_id to task to support increase_key functionality

    def insert(self, task):
        # Use negative priority for max-heap with heapq (which defaults to a min-heap)
        heapq.heappush(self.heap, (-task.priority, task))
        self.task_map[task.task_id] = task # Store the task in the map for easy access by task_id

    def extract_max(self):
        # Extract the task with the highest priority (the root of the heap).
        if not self.is_empty():
            _, task = heapq.heappop(self.heap) # Pop the task with the highest priority (priority is negated)
            del self.task_map[task.task_id] # Remove the task from the map
            return task
        return None

    def increase_key(self, task_id, new_priority):
        # Increase the priority of a task identified by task_id
        if task_id in self.task_map:
            task = self.task_map[task_id]
            if new_priority > task.priority: #increase if it is greayer than current prioority
                task.priority = new_priority
                # Rebuild the heap by negating the priority and re-applying heapify
                self.heap = [(-t.priority, t) for _, t in self.heap]
                heapq.heapify(self.heap)
        else:
            print(f"Task {task_id} not found.")

    def is_empty(self): #Checking if the priority queue(heap) is empty
        return len(self.heap) == 0

    def __repr__(self):
        return f"PriorityQueue({[t for _, t in self.heap]})"
    
# Using the PriorityQueue class with tasks in main class
def main():
    # Create a priority queue
    pq = PriorityQueue()

    # Insert tasks
    pq.insert(Task(task_id=1, priority=5, arrival_time="10:00", deadline="12:00"))
    pq.insert(Task(task_id=2, priority=3, arrival_time="10:05", deadline="12:30"))
    pq.insert(Task(task_id=3, priority=8, arrival_time="10:10", deadline="11:00"))

    print("Priority Queue after inserts:", pq)

    # Extract max priority task
    max_task = pq.extract_max()
    print("Extracted max priority task:", max_task)
    print("Priority Queue after extracting max:", pq)

    # Increase priority of a task
    pq.increase_key(task_id=2, new_priority=10) #Increasing ID#2 priority
    print("Priority Queue after increasing priority of task 2:", pq)

    # Extract max priority task again
    max_task = pq.extract_max()
    print("Extracted max priority task:", max_task)
    print("Priority Queue after extracting max:", pq)

main()
