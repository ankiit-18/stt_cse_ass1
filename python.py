# Function to check if one string can be formed by shuffling the other
def can_shuffle(str1, str2):
    # If lengths differ, they can never be anagrams
    if len(str1) != len(str2):
        return "No , they cannot be made by shuffling."

    # Create frequency arrays for ASCII characters (256 possible)
    freq1 = [0] * 256
    freq2 = [0] * 256

    # Count frequency of each character in str1
    for ch in str1:
        freq1[ord(ch)] += 1

    # Count frequency of each character in str2
    for ch in str2:
        freq2[ord(ch)] += 1

    # Compare frequencies
    for i in range(256):
        if freq1[i] != freq2[i]:
            return "No , they cannot be made by shuffling."

    return "Yes , one string can be made by shuffling the other."


# Example usage
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

print(can_shuffle(s1, s2))
