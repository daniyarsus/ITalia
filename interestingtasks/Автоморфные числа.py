import numba
from numba import jit
@numba.jit(nopython=True)
@numba.jit(fastmath=True)
def aftomorph_numbers(N):
    k = 0
    for i in range(0, N + 1):
        i = i + 1
        k = k + 1
        k_str = str(k)
        k_len = len(k_str)
        i_i = i ** 2
        i_i_str = str(i_i)
        if i_i_str[-k_len:] == k_str:
            print(f'{k_str} * {k_str} = {i_i_str}')
aftomorph_numbers(int(input()))
