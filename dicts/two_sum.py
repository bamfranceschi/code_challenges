def twoSum(self, nums: List[int], target: int) -> List[int]:
     pair = {}
      # can check to see if the number is less than the target
      for idx, num in enumerate(nums):
           if target-num in pair and idx != pair[target-num]:
                return [idx, pair[target-num]]
            else:
                pair[num] = idx
