def containsDuplicate(self, nums: List[int]) -> bool:

    # uses set to store elements

     dups = set()

      for num in nums:
           if num in dups:
                return True
            else:
                dups.add(num)
