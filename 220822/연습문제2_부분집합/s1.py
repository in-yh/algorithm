# 연습문제2_부분집합
# 2022-08-22

def f(i, N):
	if i == N:
		s = 0 # 부분 집합의 합
		for i in range(N):
			if bit[i] == 1:
				s += A[i]
		if s == 10:
			for i in range(N):
				if bit[i]:
					print(A[i], end=' ')
			print()
	else:
		bit[i] = 1
		f(i+1, N)
		bit[i] = 0
		f(i+1, N)

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0] * 10
f(0, 10)