class ToCheckSubset:
    def __init__(self, array1, array2):
        self.arr1 = array1
        self.arr2 = array2
    def check(self):
        for num in self.arr2:
            if num not in self.arr1:
                return False
        return True

array1 = [10, 5, 2, 23, 19]
array2 = [19, 5, 3] 
obj = ToCheckSubset(array1, array2)
print(obj.check())

# TC - (m)
 