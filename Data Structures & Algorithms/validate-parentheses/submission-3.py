class Solution:
    def isValid(self, s: str) -> bool:
        output_ = [")","}","]"]
        stack = []
        input_ = ["(","{","["]

        for element in s :
            if element in output_ : 
                if stack :
                    if stack[-1] != input_[output_.index(element)]:
                        return False
                    else : 
                        stack.pop()
                else :
                    return False
            else : 
                stack.append(element)
        if len(stack) > 0 :
            return False
        else : 
            return True