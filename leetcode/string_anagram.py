def anagram(s1,s2):
    
    if sorted(s1.lower()) == sorted(s2.lower()):
        return True


print anagram("aabA","baaa")    
