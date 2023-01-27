from typing import List

N = 15
SIMPLE_PERMS_COUNT = {
    1: 0,
    2: 0,
    3: 0,
    4: 2,
    5: 6,
    6: 46,
    7: 338,
    8: 2926,
    9: 28146,
    10: 298526,
    11: 3454434,
    12: 43286526,
    13: 583835650,
    14: 8433987582,
    15: 129941213186
}
BLOCKWISE_PERMS_COUNT = {
    1: 1,
    2: 0,
    3: 0,
    4: 2,
    5: 6,
    6: 46,
    7: 354,
    8: 3034,
    9: 29246,
    10: 309174,
    11: 3563562,
    12: 44471970,
    13: 597510374,
    14: 8601860622,
    15: 132135606242
}


# Converts the given binary number into a set
def bin_to_set(n: int) -> List[int]:
    bin_str = bin(n)[2:].zfill(N - 1)
    bits_arr = [int(digit) for digit in bin_str]
    s = []
    for i in range(0, len(bits_arr)):
        if bits_arr[i] == 1:
            s.append(i + 1)

    return s


def set_to_comp(s: List[int]) -> List[int]:
    if len(s) == 0:
        return [N]

    comp = []

    first = 0
    second = s[0]
    for i in range(len(s)):
        comp.append(second - first)
        first = second

        try:
            second = s[i + 1]
        except IndexError:
            comp.append(N - first)

    return comp


def generate_compositions() -> List[List[int]]:
    no_of_comps = 1 << (N - 1)  # 2 ** (N-1)
    print(f"There are {no_of_comps} compositions")

    comps = []
    for c in range(no_of_comps):
        s = bin_to_set(c)
        comp = set_to_comp(s)
        comps.append(comp)

    return comps


def count_blockwise_simp_perms() -> int:
    comps = generate_compositions()

    # Run from 4 to N
    count = 0
    for l in range(4, N + 1):
        # Run on every composition whose size is l
        for comp in [comp for comp in comps if len(comp) == l]:
            t = 1
            for lam in comp:
                t *= BLOCKWISE_PERMS_COUNT[lam]

            t *= SIMPLE_PERMS_COUNT[l]
            count += t

    return count


def main():
    print(f"---------- Running for N={N} ----------")
    print(f"Result is {count_blockwise_simp_perms()}")


if __name__ == '__main__':
    main()
