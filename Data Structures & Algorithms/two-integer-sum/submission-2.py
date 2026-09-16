class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diction = {}
        lijst = []
        for n in range(len(nums)):
            complement = target - nums[n]
            if diction.get(complement) is not None:
                 lijst.append(diction.get(complement))
                 lijst.append(n)

                 return lijst

            diction[nums[n]] = n   

                 

        