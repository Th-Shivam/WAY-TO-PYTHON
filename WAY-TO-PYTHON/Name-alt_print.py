# def generate_pattern(name1, name2):
#     # Calculate the total length to determine the number of outputs
#     total_length = len(name1) + len(name2)
    
#     # Function to generate one pattern starting from a specific index
#     def generate_single_output(start1, start2):
#         output = []
#         i, j = start1, start2  # Start with the given index for both names
        
#         while i < len(name1) or j < len(name2):
#             if i < len(name1):  # Add a character from name1
#                 output.append(name1[i])
#                 i += 2  # Skip one character
            
#             if j < len(name2):  # Add a character from name2
#                 output.append(name2[j])
#                 j += 2  # Skip one character
        
#         return ''.join(output)
    
#     # Generate all outputs
#     for start in range(total_length):
#         # Alternate starting index between name1 and name2
#         if start < len(name1):
#             print(f"Output {start + 1}: {generate_single_output(start, 0)}")
#         else:
#             print(f"Output {start + 1}: {generate_single_output(0, start - len(name1))}")

# # Input names
# name1 = input("Enter the first name: ")
# name2 = input("Enter the second name: ")

# # Generate and print all outputs
# generate_pattern(name1, name2)

name = input("Enter your name: ")
for i in range(len(name)):
    a = name[i::2]
    print(a)
    n = []
    for j in range(len(a) - 1):  # Loop through indices of `a` up to the second last character
        if a[j] == a[j + 1]:  # Check if the current character is the same as the next one
            n.append('1')
        else:
            n.append('0')
    # Append '0' for the last character since it has no adjacent character to compare
    n.append('0')
    print(''.join(n))
