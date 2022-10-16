def solution(denum1, num1, denum2, num2):
    ans = []
    if num1//num2 == 0 or num2//num1 == 0:
        if num1 >= num2:
            
    else:
        deresult = (num2*denum1)+(num1*denum2)
        ans.append(deresult)
        result = num1*num2
        ans.append(result)        
    return ans