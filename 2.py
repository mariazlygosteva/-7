input_str = input("Введите строку: ")
output_str = ""

for i in range(len(input_str)):
    if i % 2 == 1:
        output_str += input_str[i]

print(output_str)