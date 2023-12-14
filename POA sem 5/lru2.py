def pageReplacementLru(pages, n, capacity):
    # set to store the pages of capacity n
    s = set()
    # storing indexes of pages
    indexes = {}
    page_faults = 0
    for i in range(n):
        # check if space left in set for new pages
        if len(s) < capacity:
            
            # if page not already in set (page fault)
            if pages[i] not in s:
                s.add(pages[i])
                page_faults += 1
                print('page fault')
                
            # page hit 
            else:
                print('page hit')
                
            # store the index of the page
            indexes[pages[i]] = i
            
        else:
            # if page not already in set (page fault)
            if pages[i] not in s:
                # replace with least recently used
                lru = float('inf')
                
                # finding the lru page
                for page in s:
                    if indexes[page] < lru:
                        lru = indexes[page]
                        val = page
                
                # removing the lru page
                s.remove(val)
                # adding the new page
                s.add(pages[i])
                page_faults += 1
                print('page fault')
            
            # page hit 
            else:
                print('page hit')
            indexes[pages[i]] = i
        print('Current set of pages:', s)
    
    print("Total page faults:", page_faults)                
                
if __name__ == '__main__':
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    n = len(pages)
    capacity = 4
    pageReplacementLru(pages, n, capacity)