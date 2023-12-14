def bestFit(blocksizes,m,processsize,n):
    allocation=[-1]*n
    for i in range(n):
        bestIndex=-1

        for j in range(m):
            if blocksizes[j]>processsize[i]:
                if bestIndex == -1:
                    bestIndex = j
                
                elif blocksizes[bestIndex]>=blocksizes[j]:
                    bestIndex = j
                
            
        if bestIndex !=-1:
            allocation[i]=bestIndex
            blocksizes[bestIndex] -= processsize[i]

    print("PNo     Psize     BNum")
    for i in range(n):
        print(i+1,"    ",processsize[i],end="   ")
        if(allocation[i]!= -1):
            print(allocation[i]+1)
        else:
            print("not allowed")




if __name__ == "__main__":
    blocksizes = [100,500,200,300,600]
    processsize = [212,417,112,426]
    m=len(blocksizes)
    n=len(processsize)

    bestFit(blocksizes,m,processsize,n)