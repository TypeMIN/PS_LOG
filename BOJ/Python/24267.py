n = int(input())

# 코드1의 수행 횟수 출력
# 코드1은 입력 n(n-1)(n-2)/6 번 실행
print(n * (n - 1) * (n - 2) // 6)
# 코드1의 수행 횟수를 다항식으로 나타내었을 때, 최고차항의 차수 출력
# 코드1의 수행 횟수 = n(n-1)(n-2)/6 은 3차식이므로 최고차항의 차수 = 3
print("3")