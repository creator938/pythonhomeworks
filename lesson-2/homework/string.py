name = input("Python")
birth_year = int(input("2000"))
current_year = datetime.now().year
age = current_year - birth_year
print(f"{name}, you are {age} years old.\n")
txt1 = 'LMaasleitbtui'
car1 = txt1[1::2] 
print(f"Extracted car name from '{txt1}': {car1}")

txt2 = 'MsaatmiazD'
car2 = txt2[::2] 
print(f"Extracted car name from '{txt2}': {car2}\n")
txt3 = "I'am John. I am from London"
area = txt3.split("from")[-1].strip()
print(f"Residence area: {area}\n")

user_string = input("Hello world")
print(f"Reversed string: {user_string[::-1]}\n")

string_input = input("aeiouAEIOU")
vowels = "aeiouAEIOU"
count = sum(1 for char in string_input if char in vowels)
print(f"Number of vowels: {count}\n")

numbers = list(map(int, input("Enter a list of numbers separated by space: ").split()))
print(f"Maximum value: {max(numbers)}\n")

word = input(" my name is john ")
is_palindrome = word == word[::-1]
print(f"'{word}' is a palindrome: {is_palindrome}\n")

email = input("johnson090@gmailcom")
domain = email.split('@')[-1]
print(f"Email domain: {domain}\n")

length = int(input("john123443 "))
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))
print(f"Generated password: {password}")
