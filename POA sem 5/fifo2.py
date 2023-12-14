from queue import Queue

def pageReplacementFifo(pages,n,capacity):
    # set to store all the pages
    s = set()
    # to store pages in fifo manner
    indexes = Queue()
    page_faults = 0;
    for i in range(n):
        # if place left in the queue
        if len(s) < capacity : 
            # if not already in queue
            if pages[i] not in s:
                # add the page in the queue
                s.add(pages[i])
                page_faults += 1
                indexes.put(pages[i])
                print("page fault")
            else : 
                print('page hit')
        # if no place left in queue
        else : 
            # if place left in the queue
            if pages[i] not in s:
                # add current page in fifo fashion
                
                val = indexes.queue[0]
                indexes.get()
                s.remove(val)
                s.add(pages[i])
                indexes.put(pages[i])
                page_faults += 1
                print("page fault")
            else : 
                print("page miss")
        print(list(indexes.queue))
            
if __name__ == '__main__':
    pages = [7,0,1,2,0,3,0,4,2,3,0,3,2]
    n = len(pages)
    capacity = 4
    pageReplacementFifo(pages,n,capacity)