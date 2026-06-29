# 1. დაწერეთ პითონის პროგრამა, რომელიც დასაწყისში შექმნის ცარიელ სიას ([]), თუ მომხარებელი შეიყვანს სიმბოლო 'a'-ს, ნიშნავს რომ უნდა დაამატოთ სიაში რიცხვი; თუ აკრიფა 'r', სიიდან უნა წაიშალოს რიცხვი; 'e'-ს შეტანისას პროგრამამ უნდა დაასრულოს მუშაობა. მიღებული შედეგი დაბეჭდეთ კონსოლში.
# a – append
# r – remove
# e – exit
# გამოიყენეთ მხოლოდ ეს ბრძანებები და მოახდინეთ სიაზე ზემოქმედება.


# my_list = []
# while True:
#     choice = input(" append(a - append, r - remove, e - exit): ")

#     if choice == 'a':
#         number = int(input("number: "))
#         my_list.append(number)
#         print(f" {number} {my_list}")

#     elif choice == 'r':
#         if len(my_list) == 0:
#             print("სია ცარიელია!")
#         else:
#             number = int(input())
#             if number in my_list:
#                 my_list.remove(number)
#                 print(f" {number}  {my_list}")
#             else:
#                 print(f" {number} სიის ვერ მოიძებნა!")

#     elif choice == 'e':
#         print(f"\n დასრულდა. საბოლოო სია: {my_list}")
#         break

#     else:
#         print(" გთხოვთ გამოიყენოთ 'a', 'r' ან 'e'.")



# 2. დაწერეთ პითონის პროგრამა, რომელიც შექმნის სიას my_list_1 = [43, '22', 12, 66, 210, ["hi"]], და შეასრულებს შემდეგ ნაბიჯებს:

# a. დაბეჭდავს 210-ის ინდექსს;
 
# b. დაამატებს ბოლო ელემენტში ტექსტს "hello";

# c. წაშლის მეორე ინდექსზე მდგომ ელემენტს და დაბეჭდავს სიას;

# d. შექმენით ახალი სია my_llist_2, რომელსაც ექნება my_llist_1-ის მნიშვნელობა, გაასუფთავეთ my_llist_2-ის მნიშვნელობა და დაბეჭდეთ ორივე სია.

# მინიშნება: სიის გასუფთავება – arr.clear()



# my_list_1 = [43, '22', 12, 66, 210, ["hi"]]

# # a
# print(my_list_1.index(210))

# # b
# my_list_1[-1].append("hello")
# print(my_list_1)

# # c
# my_list_1.pop(2)
# print(my_list_1)

# # d
# my_list_2 = my_list_1.copy()
# my_list_2.clear()

# print(my_list_1)
# print(my_list_2)



# 3. დაწერეთ პითნის პროგრამა, რომელიც მიიღებს ტელეფონის ნომერს და regex-ით შეამოწმებს შეყვანილი ნომერი იცავს თუ არა "(123) 456-789" ფორმატს, თუ იცავს დააბრუნეთ შეყნვაილი ტელეფონის ნომერი, წინააღმდეგ შემთხვევაში გამოიტანეთ "Invalid format" ტექსტი.

# მინიშნება: სრული დამთხვევისთვის გამოიყენეთ .fullmatch() მეთოდი re მოდულიდან.

import re

phone = input("შეიყვანე ნომერი: ")

pattern = r"\(\d{3}\) \d{3}-\d{3}"

if re.fullmatch(pattern, phone):
    print(phone)
else:
    print("Invalid format")

