import time

def square_func(ranges, n):
    print("job from process:{}".format(n))
    for i in range(ranges):
        s = i*i
    
    print("Job completed from process:{}".format(n))

if __name__ == '__main__':
    ranges = [1000000, 100, 3000, 200000000]
    start = time.perf_counter()

    for idx, i in enumerate(ranges):
        square_func(i, idx)
    
    finish = time .perf_counter()
    print("Finished executing in {} second(s)".format(round(finish -  start, 2)))