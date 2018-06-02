# Rabin Karp implementation

seed = 101


def pattern_found(input_str, pattern):
    input_len = len(input_str)
    str_len = len(pattern)

    pattern_hash = compute_hash(pattern, str_len)
    input_hash = compute_hash(input_str, str_len)
    if pattern_hash == input_hash:
        return is_match(input_str, pattern, 0, str_len)

    for i in range(1, input_len - str_len + 1):
        input_hash = compute_rolling_hash(input_str, i, str_len, input_hash)
        if pattern_hash == input_hash:
            return is_match(input_str, pattern, i, str_len)

    return False


def is_match(input_str, pattern, offset, str_len):
    i = 0
    while offset < offset + str_len and i < str_len:
        if input_str[offset] != pattern[i]:
            return False
        offset += 1
        i += 1
    return True


def compute_hash(str_param, str_len):
    hash_value = 0
    for i in range(str_len):
        hash_value += (ord(str_param[i]) - ord('a')) * seed ** i
    return hash_value


def compute_rolling_hash(str, offset, str_len, prev_hash):
    prev_hash -= ord(str[offset - 1]) - ord('a')
    prev_hash /= seed
    prev_hash += (ord(str[offset + str_len - 1]) - ord('a')) * seed ** (str_len - 1)
    return prev_hash


def main():
    print(pattern_found("abcdefasbcagsa", "asb"))
    print(pattern_found("abcgabcflmxyz", "gab"))
    print(pattern_found("abcgabcflmxyz", "xyz"))
    print(pattern_found("abcgabcflmxyz", "aba"))


main()
