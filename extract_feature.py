from multiprocessing import Process, Queue
import argparse
import pandas as pd 
import cv2
import time

start = time.perf_counter()

#helper function to preprocess the image
def preprocess(filename):
    img = cv2.imread(filename)
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #edge detection
    edges = cv2.Canny(grayscale, CANNY_THRES_1, CANNY_THRES_2)
    edges = cv2.dilate(edges, None)
    edges = cv2.erode(edges, None)
    
    #find contours in the edge area
    contour_info = []
    _,contours, hierarchy = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE) 
    
    for c in contours:
        contour_info.append((c, cv2.isContourConvex(c), cv2.contourArea(c)))
    
    contour_info = sorted(contour_info, key=lambda c:c[2], reverse=True)
    max_contour = contour_info[0]
        
    #create empty mask, draw filled polygon on its corresponding contour
    mask = np.zeros(edges.shape)
    cv2.fillConvexPoly(mask, max_contour[0],(255))
    
    #smoothing the images
    mask = cv2.dilate(mask, None, iterations=MASK_DILATE_ITER)
    mask = cv2.erode(mask, None, iterations=MASK_ERODE_ITER)
    mask = cv2.GaussianBlur(mask, (BLUR, BLUR), 0)
    
    img[mask <= 100] = 0
    return img

#helper function to get the Feature vector from the image
def get_feature_vec():

    print("Blah.... Blah..")
    time.sleep(1)
    print("Ending Blah... Blah")

    return "msg"


def submit_job(df, list_items, q):
    a = []
    for items in list_items:
        oneitemdf = df[df['MinorCategory'] == items]['FilePath'].values.tolist()
        oneitemdf = [x for x in oneitemdf if x.endswith('.png')]
        result = get_feature_vec()
        if result == 'error_occured':
            pass
        else:
            a.append(result)
        
    q.put(a)


if __name__ == '__main__':
    parameters = argparse.ArgumentParser()
    parameters.add_argument("--filepath",
        default="/Users/whitewolf/workprojects/multiviewclassification/data/processed/train.csv", 
        type=str)

    passed_vals = parameters.parse_args()
    filepath = passed_vals.filepath
    df = pd.read_csv(filepath, sep=",")
    
    #get unique catgories, just testing first 40 categories
    minor_categories = list(df.MinorCategory.value_counts().to_dict().keys())[:120]

    start_time = time.perf_counter()
    
    #shared memory
    as_batches = []
    start, end = 0, len(minor_categories)

    #queue results
    q = Queue()

    while(start < end):
        as_batches.append(minor_categories[start:start+10])
        start += 10
    
    process_tracker = 0

    while(len(as_batches) > 0):

        p1 = Process(target=submit_job, args=(df, as_batches[0], q))
        p2 = Process(target=submit_job, args=(df, as_batches[1], q))
        p3 = Process(target=submit_job, args=(df, as_batches[2], q))
        p4 = Process(target=submit_job, args=(df, as_batches[3], q))
        
        #start the process
        p1.start()
        p2.start()
        p3.start()
        p4.start() 

        #join all the process once it is completed
        p1.join()
        p2.join()
        p3.join()
        p4.join()

        process_tracker += 4
        as_batches = as_batches[process_tracker:]

    while not q.empty():
        print(q.get())
    
    finish_time = time.perf_counter()
    print("Finished executing in {} second(s)".format(round(finish_time -  start_time, 2)))
    

