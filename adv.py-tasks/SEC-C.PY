#Count Vowels and Consonants
text = input("Enter a string: ")

vowels = "aeiouAEIOU"
v_count = 0
c_count = 0

for ch in text:
    if ch.isalpha():
        if ch in vowels:
            v_count += 1
        else:
            c_count += 1

print("Vowels:", v_count)
print("Consonants:", c_count)

#10. Count Lines, Words, and Characters in a File

filename = input("Enter file name: ")

with open(filename, 'r') as file:
    content = file.read()

lines = content.split('\n')
words = content.split()
characters = len(content)

print("Lines:", len(lines))
print("Words:", len(words))
print("Characters:", characters)

#11. BankAccount Class
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)

    def check_balance(self):
        print("Current Balance:", self.balance)


acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(300)
acc.check_balance()

#Remove Duplicates and Sort

nums = list(map(int, input("Enter numbers: ").split()))

unique_nums = []
for num in nums:
    if num not in unique_nums:
        unique_nums.append(num)

n = len(unique_nums)
for i in range(n):
    for j in range(0, n-i-1):
        if unique_nums[j] > unique_nums[j+1]:
            unique_nums[j], unique_nums[j+1] = unique_nums[j+1], unique_nums[j]

print("Sorted list without duplicates:", unique_nums)

#13. Write a program using lambda + map + filter:
 #- Square only even num

nums = list(map(int, input("Enter numbers: ").split()))

result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums)))

print("Squared even numbers:", result)