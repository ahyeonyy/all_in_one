def combination(nums):
    ans = []
    
    def backtrack(start, curr):
        if len(curr) == k:
            ans.append(curr[:])
            return
        for i in range(start,len(nums)) :    
                curr.append(nums[i])
                backtrack(i + 1,curr)
                curr.pop()
    for k in range(len(nums)+1):
        backtrack(start = 0, curr = [])
  
    return ans
print(combination(nums = [1,2,3,4]))