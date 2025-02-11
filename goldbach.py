def sieve_of_eratosthenes(n):
    """n 이하 모든 소수를 리스트로 반환하는 에라토스테네스의 체 구현"""
    sieve = [True] * (n+1)
    sieve[0], sieve[1] = False, False
    
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    
    return [x for x in range(2, n+1) if sieve[x]]

def can_be_expressed_as_sum_of_three_primes(n, primes_set, primes_list):
    """
    n이 3개의 소수 합으로 표현 가능한지 확인.
    primes_set: 소수 여부 빠른 체크용 set
    primes_list: 소수 리스트
    """
    # 간단하게 3중 반복 (비효율적일 수 있음)
    for i in range(len(primes_list)):
        p1 = primes_list[i]
        if p1 > n:
            break
        for j in range(i, len(primes_list)):
            p2 = primes_list[j]
            if p1 + p2 > n:
                break
            p3 = n - (p1 + p2)
            # p3가 소수인지 빠르게 체크
            if p3 in primes_set:
                return True
    return False

def check_goldbach_weak_conjecture_up_to(max_n):
    """
    홀수 n(7 이상 max_n 이하)에 대해,
    n = p1 + p2 + p3 형태로 표현 가능한지 전부 확인.
    """
    # max_n 이하 소수를 전부 구함
    primes_list = sieve_of_eratosthenes(max_n)
    primes_set = set(primes_list)  # membership 체크 빠르게 하려고 set 사용
    
    # 7부터 max_n까지 홀수만 검사
    for odd_n in range(7, max_n+1, 2):
        # 약간의 최적화: 작으면 건너뛰어도 되지만 여기서는 단순히 진행
        if not can_be_expressed_as_sum_of_three_primes(odd_n, primes_set, primes_list):
            print(f"[실패] {odd_n}은(는) 3개의 소수 합으로 나타낼 수 없는 것처럼 보임.")
            return  # 하나라도 실패 시 그 즉시 종료
    print(f"[성공] 7부터 {max_n}까지 모든 홀수는 3개의 소수 합으로 표현 가능함을 확인!")

if __name__ == "__main__":
    # 예시: 7부터 1만까지 테스트
    max_check = 10_000
    print(f"골드바흐의 약한 추측을 {max_check}까지 실험적으로 확인합니다.")
    check_goldbach_weak_conjecture_up_to(max_check)
