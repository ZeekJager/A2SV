class Solution: 
    def selectionSort(self, arr):
        for i in range(len(arr)):
            m=i
            for j in range(i+1, len(arr)):
                if arr[m]>=arr[j]:
                    m=j
            arr[m], arr[i] = arr[i], arr[m]
            
        return arr