def frequencySort(self, nums: List[int]) -> List[int]:
        
        s= Counter(nums)           #counting
        def frequency(n1, n2):
            
            return s[n1] - s[n2] if s[n1] != s[n2] else n2 - n1
        
        nums.sort(key = cmp_to_key(frequency))  # comparing nums

        return nums


frequencySort([-1,1,-6,4,5,-6,1,4,1])