class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        for digit in digits:
            number =  number * 10 + digit
        
        number+=1
        return [int(d) for d in str(number)]



