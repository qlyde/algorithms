def rabin_karp(text, pattern):
    text_len = len(text)
    pattern_len = len(pattern)
    prime = 101  # A prime number for hashing
    base = 256   # Number of possible characters

    pattern_hash = 0
    text_hash = 0
    h = 1  # Calculate h as (base^(pattern_len-1)) % prime
    for i in range(pattern_len - 1):
        h = (h * base) % prime

    # Calculate initial hash values for pattern and first substring of text
    for i in range(pattern_len):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        text_hash = (base * text_hash + ord(text[i])) % prime

    # Slide the pattern over the text and check hash values
    for i in range(text_len - pattern_len + 1):
        if pattern_hash == text_hash:
            # Check character by character for a match
            if text[i:i + pattern_len] == pattern:
                print("Pattern found at index", i)

        # Update the hash value for the next substring
        if i < text_len - pattern_len:
            text_hash = (base * (text_hash - ord(text[i]) * h) + ord(text[i + pattern_len])) % prime
            if text_hash < 0:
                text_hash += prime

# Example usage:
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
rabin_karp(text, pattern)
