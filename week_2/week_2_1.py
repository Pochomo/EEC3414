# 최대공약수를 계산하는 함수
def gcd(a, b):
    while b > 0:
        temp = a
        a = b
        b = temp % b
    return a

# 최소공배수를 계산하는 함수
def lcm(a, b):
    return a * b // gcd(a, b)

# 두 정수 입력
a, b = map(int, input().split())
# 최대공약수와 최소공배수 출력
print(gcd(a, b), lcm(a, b))