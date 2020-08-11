# segment tree

class segment_tree:
    def __init__(self,n):
        self.length=2*n+1
        self.array=[0 for _ in range(2*n+1)] # array is 1-based
        u=self.length
    
    def sum(self,i,j,ind,start,end) : # gives the sum of elements in array
        ''' it computes sum of elements from index i to j      # from index i to j  
            ind should be 1
            start should be 1
            end should be the length of array
        '''
        if start > j or i>end : # not overlap
            return 0
        if i<=start and j>= end : # the segment in node is compeletly in the segment we want to calculate the sum of
            return  (self.array[ind])
        mid=(start+end) >> 1  # overlaping
        return(self.sum(i,j,2*ind,start,mid)+self.sum(i,j,2*ind+1,mid+1,end))
    
    def add(self,i,val,ind,start,end):
        ''' it adds val to index i
            ind should be 1
            start should be 1
            end should be the length of array
        '''
        if ind > self.length :  # we have reached the leaf
            return
        self.array[ind]+=val
        mid=(start+end) >> 1
        if  start <= i <= mid :   
            self.add(i,val,2*ind,start,mid)  # going to the left child
        else:
            self.add(i,val,2*ind+1,mid+1,end)  # going to the right child

if __name__ == '__main__' : # just for a test :)

    xxx=segment_tree(10)

    xxx.add(6,1,1,1,10)
    xxx.add(2,10,1,1,10)
    xxx.add(9,33,1,1,10)
    xxx.add(5,-4,1,1,10)
    xxx.add(1,9,1,1,10)
    xxx.add(10,-76,1,1,10)
    print(xxx.sum(1,5,1,1,10))
    print(xxx.sum(2,5,1,1,10))
    print(xxx.sum(1,10,1,1,10))
    print(xxx.sum(4,9,1,1,10))
    