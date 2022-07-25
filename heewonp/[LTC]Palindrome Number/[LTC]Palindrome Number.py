class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        x = str(x)
        if x == x[::-1]:
            return True
        else:
            return False


# int형을 문자열로 바꾼 후 뒤집었을 때 도 같으면 true반환