from queue import Queue
	
def hot_potato(name_list,limit)	:
	'''A general simulation of Hot Potato problem'''
	
	q = Queue()
	for name in name_list:
		q.enqueue(name)
		
	while q.size() >1 :
		for count in range(limit):
			# simulate circle
			q.enqueue(q.dequeue())
		q.dequeue()
		
	return q.dequeue()

# Testing
print(hot_potato(["A","B","C","D","E","F"],7))
