import timeit

# Підв'язуємо текстові файли
with open('three_main.py\Стаття 1.txt', 'r', encoding='utf-8') as file:
    text1 = file.read()

with open('three_main.py\Стаття 2.txt', 'r', encoding='utf-8') as file:
    text2 = file.read()

# Алгоритм Боєра-Мура
def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)

    if m == 0:
        return 0

    # Використовуємо словник для bad_char
    bad_char = {}

    for i in range(m):
        bad_char[pattern[i]] = i

    s = 0
    while s <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        if j < 0:
            return s
        else:
            s += max(1, j - bad_char.get(text[s + j], -1))
    
    return -1

# Алгоритм Кнута-Морріса-Пратта
def kmp_search(text, pattern):
    def compute_lps(pattern):
        m = len(pattern)
        lps = [0] * m
        j = 0
        i = 1
        while i < m:
            if pattern[i] == pattern[j]:
                j += 1
                lps[i] = j
                i += 1
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)
    i = 0
    j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

# Алгоритм Рабіна-Карпа
def rabin_karp(text, pattern):
    d = 256
    q = 101
    n = len(text)
    m = len(pattern)
    h = pow(d, m - 1) % q
    p = 0
    t = 0

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for s in range(n - m + 1):
        if p == t:
            if text[s:s + m] == pattern:
                return s
        if s < n - m:
            t = (d * (t - ord(text[s]) * h) + ord(text[s + m])) % q
            if t < 0:
                t += q

    return -1

# Вимірюємо час виконання
patterns = ["алгоритм", "вигаданийпідрядок"]

def measure_time(algorithm, text, pattern):
    start_time = timeit.default_timer()
    result = algorithm(text, pattern)
    elapsed = timeit.default_timer() - start_time
    return elapsed, result

results = {}
for pattern in patterns:
    results[pattern] = {}
    for alg_name, algorithm in [("Boyer-Moore", boyer_moore), ("KMP", kmp_search), ("Rabin-Karp", rabin_karp)]:
        time1, _ = measure_time(algorithm, text1, pattern)
        time2, _ = measure_time(algorithm, text2, pattern)
        results[pattern][alg_name] = (time1, time2)

# Виводимо результати
for pattern in patterns:
    print(f"Results for pattern '{pattern}':")
    for alg_name in results[pattern]:
        time1, time2 = results[pattern][alg_name]
        print(f"  {alg_name}:")
        print(f"    Text 1: {time1:.6f} seconds")
        print(f"    Text 2: {time2:.6f} seconds")
    print()

