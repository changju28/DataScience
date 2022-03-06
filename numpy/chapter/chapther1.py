# 팔린드롬 문제 ( 반대로 읽어도 똑같은 단어 결과에 따라 True / False 리턴)
def is_palindrome(word):
    for i in range(len(word)//2):
        if word[i] != word[-i-1]:
            return False

    return True

# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))