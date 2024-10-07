def tribonacci(n):
    cache_tr = {1: 1, 2: 1, 3: 1}
    def tribonacci_rec(n):
        result = cache_tr.get(n)
        if result is None:
            result = tribonacci_rec(n - 3) + tribonacci_rec(n - 2) + tribonacci_rec(n - 1)
            cache_tr[n] = result
        return result
    return tribonacci_rec(n)

# # INPUT DATA:
#
# # TEST_1:
# print(tribonacci(1))
#
# # TEST_2:
print(tribonacci(7))
#
# # TEST_3:
# print(tribonacci(4))
#
# # TEST_4:
# print(tribonacci(3))
#
# # TEST_5:
# print(tribonacci(10))
#
# # TEST_6:
# print(tribonacci(2))
#
# # TEST_7:
# print(tribonacci(300))
#
# # TEST_8:
# print(tribonacci(100))