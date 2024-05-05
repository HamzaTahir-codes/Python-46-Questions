str_list = ["orchestra", "carthorse", "hen", "cat", "tac", "horsecart", "rat", "tar", "atr", "julie"]

anagram_groups = {}

for word in str_list:

    sorted_word = ''.join(sorted(word))
    # if sorted word exist add it to dictionary
    if sorted_word in anagram_groups:
        anagram_groups[sorted_word].append(word)
    else:
        anagram_groups[sorted_word] = [word]

# Print anagrams and non-anagrams separately
for group in anagram_groups.values():
    if len(group) > 1:
        print(" ".join(group), "<--- Anagram --->")
    else:
        print(f"{group[0]} is not an angram")
