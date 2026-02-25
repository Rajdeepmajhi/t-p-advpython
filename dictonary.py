list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

common = set(list1) & set(list2)
print(common)



sentence = "python is easy and python is powerful"
words = sentence.split()

unique_words = set(words)
result = " ".join(unique_words)

print(result)



s1 = "listen"
s2 = "silent"

if set(s1) == set(s2) and len(s1) == len(s2):
    print("Anagram")
else:
    print("Not Anagram")




list1 = [1, 2, 3, 4]
list2 = [3, 4, 5]

result = set(list1) - set(list2)
print(result)



s = "python"

if len(s) == len(set(s)):
    print("All characters are unique")
else:
    print("Duplicate characters found")



lst = [1, 2, 2, 3, 4, 4, 5]

distinct_count = len(set(lst))
print(distinct_count)



set1 = {1, 2, 3}
set2 = {3, 4, 5}

result = set()

for i in set1:
    if i not in set2:
        result.add(i)

for i in set2:
    if i not in set1:
        result.add(i)

print(result)



s1 = "abcdef"
s2 = "cdefgh"

common = set(s1) & set(s2)

res1 = "".join([c for c in s1 if c not in common])
res2 = "".join([c for c in s2 if c not in common])

print(res1)
print(res2)



set1 = {1, 2}
set2 = {1, 2, 3, 4}

is_subset = True

for i in set1:
    if i not in set2:
        is_subset = False
        break

if is_subset:
    print("Set1 is subset of Set2")
else:
    print("Set1 is not subset of Set2")



lst = [1, 2, 3, 2, 4, 1, 5]

seen = set()
repeated = set()

for i in lst:
    if i in seen:
        repeated.add(i)
    else:
        seen.add(i)

print(repeated)




