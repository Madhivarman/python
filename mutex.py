import threading,time,random

#python create mutex
mutex = threading.Lock()

class thread_one(threading.Thread):
	def run(self):
		#mutex global
		global mutex
		print("The first thread is sleeping now")
		time_count = random.randint(1,5)
		#time count
		print("Thread_one:" , time_count)
		#sleep
		time.sleep(time_count)	
		print("First thread is finished")
		#release the mutex
		mutex.release()

class thread_two(threading.Thread):
	def run(self):
		#mutex global
		global mutex
		print("The Second thread is sleeping now")
		time_count = random.randint(1,5)
		#time count
		print("Thread_two:",time_count)
		#sleep
		time.sleep(time_count)
		#has to wait until first thread lock is released
		mutex.acquire()
		print("Second Thread takes is finished")

#main thread is acquiring the lock
mutex.acquire()
t1 = thread_one()
t2 = thread_two()
t1.start()
t2.start()