class TreeTraversalConverter:
    def preOrder(self, arr):
        for num in arr:
            print(num, end=" ")
    
    INT_MIN = -2**31
    INT_MAX = 2**31
    
    # preIndex as array of numbers, so that it is passed by reference
    def postOrder(self, arr, minval = -2**31, maxval = 2**31, preIndex = [0]): 
    
        if (preIndex[0] == len(arr)): 
            return
        if (arr[preIndex[0] ] < minval or arr[preIndex[0] ] > maxval): 
            return
        
        val = arr[preIndex[0]]  
        preIndex[0] += 1
    
        # All elements with value between minval and val lie in left subtree.  
        self.postOrder(arr, minval=minval, maxval=val, preIndex=preIndex)  
        # All elements with value between val and maxval lie in right subtree.  
        self.postOrder(arr, minval=val, maxval=maxval, preIndex=preIndex)  
    
        print(val, end = " ") 
                          
# Driver Code 
if __name__ == '__main__': 
    arr = [40, 30, 32, 35, 80, 90, 100, 120] 
  
    treeTrav = TreeTraversalConverter()

    print("PreOrder:")
    treeTrav.preOrder(arr)
    print()
    print("PostOrder:")
    treeTrav.postOrder(arr)
    print()