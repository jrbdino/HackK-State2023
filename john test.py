from SortedPriorityQueue import SortedPriorityQueue

my_queue = SortedPriorityQueue()
my_queue.add(0, 'Homework 1')
my_queue.add(2, 'Homework 2')
my_queue.add(4, 'Homework 3')
my_queue.add(-1, 'Homework 4')



for item in my_queue._data:
    print(item)

print(my_queue.min())