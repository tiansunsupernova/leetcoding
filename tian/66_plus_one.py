class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            next_carry = (digits[i] + carry) // 10
            digits[i] = (digits[i] + carry) % 10
            carry = next_carry
        return digits if not carry else [1] + digits
            
