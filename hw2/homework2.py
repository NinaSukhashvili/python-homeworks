#1. შექმენით სია num_list [44, 63, 11, 8, 28, 56, 43, 55], in-ის გამოყენებით დაწერეთ პროგრამა რომელიც შეამოწმებს თქვენს მიერ შეტანილი რიცხვი არის თუ არა სიაში.


# num_list = [44, 63, 11, 8, 28, 56, 43, 55]
# number = int(input("რიცხვი: "))
# if number in num_list:
#     print("სიაში არის.")
# else:
#     print("სიაში არ არის.")

#2. დაწერეთ პროგრამა რომელიც შეამოწმებს თქვენს მიერ შეყვანილი რიცხვის ლუწობასა და კენტობას. თუ რიცხვი ლუწია გამოიტანეთ ტექსტი 'even' თუ კენტია 'odd'.


# number = int(input("რიცხვი: "))

# if number % 2 == 0:
#     print("even")
# else:
#     print("odd")


#3.შექმენით ორი სტრინგის ტიპის ცვლადი st1 და st2, შეადარეთ ისინი is-ის გამოყენებით, თუ ემთხვევა გამოიტანეთ ტექსტი "Same object", წინააღმდეგ შემთხვევაში "Different object"

# st1 = "Python1"
# st2 = "Python"

# if st1 is st2:
#     print("Same object")
# else:
#     print("Different object")


#4. შექმენით სია num_list [44, 23, 11, 8, 20, 56, 33, 55], შეიტანეთ რიცხვი და დაწერეთ შემდეგი პირობა:

# * თუ შეტანილი რიცხვი მეტია სიაში არსებულ მე-3 ელემენტზე და ნაკლებია ბოლო ელემენტზე გამოიტანეთ ტექსტი "More than list elements";

# * თუ შეტანილი რიცხვი უდრის სიის მე-6 ელემენტს გამოიტანეთ ტექსტი "Equal";

# * სხვა ნებისმიერ შემთხვევაში გამოიტანეთ ტექსტი "None of the conditions were met".

# რიცხვის შეტანის ოპერაციისთვის გამოიყენეთ input მეთოდი.

num_list = [44, 23, 11, 8, 20, 56, 33, 55]

number = int(input("Enter a number: "))

if number > num_list[2] and number < num_list[-1]:
    print("More than list elements")
elif number == num_list[5]:
    print("Equal")
else:
    print("None of the conditions were met")



