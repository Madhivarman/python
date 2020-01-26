import argparse
import time
import multiprocessing

start = time.perf_counter()

def do_something(seconds):
    print("Sleeping in {} second(s)".format(seconds))
    time.sleep(seconds)
    print('Done Sleeping:{}'.format(seconds))


#with multiprocessing the program executes for 25.09 seconds

def with_mulithread():
    """    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [1 for x in range(100)]
        results = executor.map(do_something, secs)
        print(results)
    """
    processes = []
    for i in range(1000):
        p1 = multiprocessing.Process(target=do_something, args=[1.5]) 
        p2 = multiprocessing.Process(target=do_something, args=[2.0])

        p1.start()
        p2.start()

        processes.append(p1)
        processes.append(p2)
    
    for process in processes:
        process.join()

#without multiprocessing the program exectues for 100.05 seconds
def without_multihread():
    print("entered without multithread option")
    for i in range(100):
        result = do_something(1)
        print(result)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--with_multithread',
        default=True,
        help="To run the Function with Multithread or without Multithreading"
    )

    arguments = parser.parse_args()
    if arguments.with_multithread == 'True':
        with_mulithread()
    else:
        without_multihread()
    
    finish = time.perf_counter()
    print("Finished executing in {} second(s)".format(round(finish -  start, 2)))


if __name__ == '__main__':
    main()