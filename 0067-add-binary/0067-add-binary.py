class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        if len(a) < len(b):
            a, b = b, a
        
        c = ""
        carry = 0

        for i in range(len(b)):
            bit_a = int(a[i])
            bit_b = int(b[i])
            total = bit_a + bit_b + carry

            c += str(total % 2) #add remainder 
            carry = total // 2

        for j in range(len(b), len(a)):
            bit_a = int(a[j])
            total = bit_a + carry

            c += str(total % 2) #add remainder 
            carry = total // 2

        if carry:
            c += str(carry)
        
        c = c[::-1]
        return c