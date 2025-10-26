# 在此文件中实现 PrimeList 函数

def PrimeList(N):
    """
    返回小于 N 的所有质数，以空格分隔    
    参数:    N - 正整数    
    返回:    str - 包含所有小于 N 的质数的字符串，空格分隔
    """
    if N <= 2:
        return ""
    primes = []
    is_prime = [True] * N
    is_prime[0] = is_prime[1] = False
    for i in range(2, N):
        if is_prime[i]:
            primes.append(str(i))
            for j in range(i * i, N, i):
                is_prime[j] = False
    return " ".join(primes)
