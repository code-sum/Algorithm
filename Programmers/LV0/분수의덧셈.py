from fractions import Fraction

def solution(denum1, num1, denum2, num2):
    answer = Fraction(denum1, num1) + Fraction(denum2, num2)
    return [answer.numerator, answer.denominator]

# Fraction : 유리수 연산에 쓰임. Fraction(분자, 분모) 는 분자/분모 형태의 유리수
# 유리수 : 분자와 분모가 서로소이고, 소수에서 소수점 이하의 수가 반복적인 순환소수를 포함하는 수
# a.numerator : a 라는 분수의 분자 출력
# a.denominator : a 라는 분수의 분모 출력