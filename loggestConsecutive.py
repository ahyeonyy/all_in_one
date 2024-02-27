def longestConsecutive(nums):
        nums.sort()
        nums_dict = {}
        
        longgest = 0
        for i in nums:
            nums_dict[i] = i + 1
        
        for n in nums:
            if n - 1 not in nums_dict:
                target = n
                cnt = 1
                while target in nums_dict:
                    cnt +=1
                    target+=1
            longgest = max(longgest, cnt)
        return longgest
longestConsecutive([100,4,200,1,3,2])