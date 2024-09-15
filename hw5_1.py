# .1 כתוב תוכנית בפייטון הקולטת מהמשתמש אורך סרט בדקות ומדפיסה כמה שעות, וכמה דקות
# נמשך הסרט . לדוגמא :
# - אם אורך הסרט שנקלט הוא - ,70 אז התשובה תהיה 1 שעה ו- 10 דקות
# - אם אורך הסרט שנקלט הוא - ,160 אז התשובה תהיה 2 שעות ו- 40 דקות
# - אם אורך הסרט שנקלט הוא - ,180 אז התשובה תהיה 3 שעות ו- 0 דקות
# - וכו'

movie_length_in_minutes: int = int(input("How long is the movie minutes? "))
movie_length_in_hours: int = movie_length_in_minutes // 60
minutes_left: int = movie_length_in_minutes % 60
print(f"the movie screening time is: {movie_length_in_hours}:{minutes_left}")