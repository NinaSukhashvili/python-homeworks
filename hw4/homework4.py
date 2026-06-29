# # 1. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს და აბრუნებს სტრიქონის UTF-8 დაშიფრულ ვერსიას.

# # text = input()
# # encoded_text = text.encode("utf-8")
# # print(encoded_text)

# # 2. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს.
#     # ჩამოაშორეთ ზედმეტი ინტერვალები.
#     # ყველა სიმბოლო გადაიყვანეთ პატარა ასოებში და
#     # დაუმატეთ ქვესტრიქონი 'Python'.
#     # თუ შეყვანილ სტრიქონში არსებობს სიტყვა "python", ჩაანაცვლეთ "Python"-ით.
#     # მინიშნება: ზედმეტი ინტერვალების ჩამოსაშორებელი მეთოდია .strip().
#     # მაგ.: "  Python is funny     ".strip()   ====>  "Python is funny"


# # text = input()
# # text = text.strip()
# # text = text.lower()
# # text = text.replace("python", "Python")
# # text = text + " Python"

# # print(text)


# # 3. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს.
# # პროგრამამ უნდა დააბრუნოს ახალი სტრიქონი,
# # რომელიც შედგება შეყვანილი სტრიქონის პირველი ნახევრისაგან.

# # text = input()
# # half = len(text) // 2
# # new_text = text[:half]

# # print(new_text)


# # 4. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს.
# # string მოდულის გამოყენებით დაწერეთ შემოწმება.
# # სტრიქონი ვალიდურია მაშინ, როდესაც ის შეიცავს მინიმუმ ერთ ლათინურ ასოსა და
# # მინიმუმ ერთ ციფრს და ამავე დროს არ შეიცავს დამატებით სიმბოლოებს: '!', '~', '#', '$' და ა.შ.

# # import string
# # text = input()
# # has_letter = False
# # has_digit = False
# # is_valid = True

# # for char in text:
# #     if char in string.ascii_letters:
# #         has_letter = True

# #     elif char in string.digits:
# #         has_digit = True

# #     else:
# #         is_valid = False

# # if has_letter and has_digit and is_valid:
# #     print("ვალიდურია")
# # else:
# #     print("არ არის ვალიდური")


# # 5. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს,
# # სტრიქონი გადაყავს ბაიტებში, ბეჭდავს მნიშვნელობას და შემდეგ კი
# # გადაყავს ბაიტებიდან სტრიქონში და ბეჭდავს სტრიქონს.

text = input()
encoded_text = text.encode("utf-8")
print(encoded_text)

decoded_text = encoded_text.decode("utf-8")
print(decoded_text)
















