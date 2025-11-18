input_num = int(input("Enter a number: "))
all_numbers = [num for num in range(1, input_num)]
odd_numbers = [num for num in range(1, input_num) if num % 2 != 0]
print(f"All numbers under {input_num}: {all_numbers}")
print(f"Odd numbers under {input_num}: {odd_numbers}")