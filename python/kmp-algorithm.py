def compute_lps_array(pattern):
    length = 0
    i = 1
    lps = [0] * len(pattern)

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = compute_lps_array(pattern)

    i = j = 0  # i for text index, j for pattern index

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
            if j == m:
                print("Pattern found at index", i - j)
                j = lps[j - 1]  # Partial match found, update j
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

# Example usage:
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
kmp_search(text, pattern)
