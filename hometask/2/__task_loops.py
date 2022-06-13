# 1. Fill the missing pieces
# Fill the ____ parts in the code below.

words = ['PYTHON', 'JOHN', 'chEEse', 'hAm', 'DOE', '123']
upper_case_words = []

for upper_cased in words:
    if upper_cased.isupper():
        upper_case_words.append(upper_cased)
assert upper_case_words == ['PYTHON', 'JOHN', 'DOE']

# 2. Calculate the sum of dict values
# Calculate the sum of the values in magic_dict by taking only into account numeric values (hint: see isinstance).

magic_dict = dict(val1=44, val2='secret value', val3=55.0, val4=1)
# Your implementation
sum_of_values = sum(num for num in magic_dict.values() if type(num)!= str)
assert sum_of_values == 100

# 3. Create a list of strings based on a list of numbers
# The rules:

# If the number is a multiple of five and odd, the string should be 'five odd'
# If the number is a multiple of five and even, the string should be 'five even'
# If the number is odd, the string is 'odd'
# If the number is even, the string is 'even'

numbers = [1, 3, 4, 6, 81, 80, 100, 95]
# Your implementation
my_list = []
for num in numbers:
    if num % 5 == 0 and num % 2 == 1:
        my_list.append('five odd')
    elif num % 5 == 0 and num % 2 == 0:
        my_list.append('five even')
    elif num % 2 == 1:
        my_list.append('odd')
    elif num % 2 == 0:
        my_list.append('even')
        
assert my_list == ['odd', 'odd', 'even', 'even', 'odd', 'five even', 'five even', 'five odd']