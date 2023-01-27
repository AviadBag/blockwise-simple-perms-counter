from typing import List

N = 7


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
    for i in range(len(s) - 1):
        comp.append(second - first)
        first = second
        second = s[i + 1]

    comp.append(N - second)

    return comp


def main():
    print(f"---------- Running for N={N} ----------")
    no_of_comps = 1 << (N - 1)  # 2 ** (N-1)
    print(f"There are {no_of_comps} compositions")

    comps = []
    for c in range(no_of_comps):
        s = bin_to_set(c)
        comp = set_to_comp(s)
        comps.append(comp)
        print(f"C={bin(c)[2:].zfill(N - 1)} ({c}), Set={s}, Composition={comp}")


if __name__ == '__main__':
    main()
