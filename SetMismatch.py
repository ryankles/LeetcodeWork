class Solution(object):
    
    nums = [2,2]



    
    def findErrorNums(nums):
        
        hash = set()
        list = []

        #finds repition
        for n in nums:
            if n in hash:
                list.append(n)
            hash.add(n)
        
        #finds missing number
        for i in range(1, len(nums)+1):
            if i not in hash:
                list.append(i)
                break
        return list

        
    print(findErrorNums(nums))
