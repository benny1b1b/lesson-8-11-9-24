# בתרגילים הבאים פתור באמצעות לולאת for, או לולאת while, או לולאת break-true-white:


#קלוט מהמשתמש את גובהו עשרוני , עד אשר יתקבל גובה בין 0.4 לבין 2.5
# בכל פעם שיתקבל גובה שלא בטווח הזה, הדפס : input wrong

height: float = float(input("what is your height? "))
while not 0.4 <= height <= 2.5:
    print(f"You are out of range, input wrong {height}")
    height =  float(input("what is your height? "))
print(f"{height}, you are in range.")


# קלוט מהמתשתמש 2 מספרים שלמים . והדפס את המספרים השלמים ביניהם.
# לדוגמא אם נקלט 1 ו- 5 ה דפס: 1 2 3 4 .5 שים לב: המספר הראשון שנקלט לא בהכרח
# קטן מהמספר השני שנקלט. כלומר אם נקלט 5 ו- ,1 אז יודפס: 5 4 3 2 1
#
num1: int= int(input("enter your first number: "))
num2: int= int(input("enter your second number: "))
if num1 > num2:
    for i in range(num1,num2 -1, -1):
        print(i, end=" ")
    print()
else: #num1 < num2:
    for i in range(num1 ,num2 +1, +1):
        print(i, end=" ")
    print()


# ערכו של פאי pie הוא .3.14 שאל את המשתמש כמה שווה פאי? וקלוט את תשובתו
# בלולאה עד אשר יקליד את התשובה הנכונה. יש למשתמש 3 נסיונות בלבד .
# אם הצליח בתוך 3 נסיונות או פחות, הדפס: "correct are you"
# אם נכשל 3 פעמים צא מהלולאה והדפס: " 3.14 is pie "
#
pai: float = 3.14
counter: int = 1
x: float = float(input("enter your pai:"))

while x != pai and counter < 3:
    counter += 1
    x: float = float(input(f"{x}, is not pai, try again: "))
if counter == 3:
    print("3.14 is pie")
else:
    print("are you correct")


# קלוט מהמשתמש 3 מספרים בלולאה עד אשר :
# המספר הראשון שנקלט יהיה בין ,0-10
# + וגם המספר השני שנקלט יהיה בין ,10-60
# + וגם המספר השלישי שנקלט יהיה בין .60-100
# + וגם המספר השני שנקלט יהיה ממוצע של שלושת המספרים.
# לדוגמא : 10 50 90
# קלוט בלולאה את 3 המספרים שוב ושוב ... עד אשר כל התנאים יתקיימו

while True:
    num1: int = int(input("enter first number: "))
    num2: int = int(input("enter second number: "))
    num3: int = int(input("enter third number: "))

    avg_num: int = (num1 + num2 + num3) / 3
    print(f"{avg_num:.2f}")

    if 0 <= num1 <= 10 and 11 <= num2 <= 60 and 61 <= num3 <= 100 and avg_num == num2:

        print("There is no deviation")
        break
    else:
        print("invalid input,There is a deviation")


# *אתגר: יש בפאב 10 בירות . מותר להעניק בירה רק למי שמלאו לו 18 שנה. קלוט
# מהמשתמש את גילו. רק אם למשתמש מלאו 18 שנה הענק לו בירה. חזור על התהליך עד
# שחולקו כל 10 הבירות


beer: int= 10
age: int = int(input("hello, what your age? "))

while beer != 0:
    if age >= 18:
        print("grate, you deserve a deer! ")
        beer -=1
        print(f"{beer} beers left. ")
        age: int = int(input("hello, what your age? "))
    else:
        print("you're not old enough.")
        age: int = int(input("hello, what your age? "))
if beer == 0:
    print("sorry we're out for beer.")
