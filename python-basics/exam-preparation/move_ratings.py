import sys

number_films =int(input())

average = 0
min_rating = sys.maxsize
max_rating = -sys.maxsize
name_max = ''
name_min = ''

for i in range(0, number_films):
    name = input()
    rating = float(input())
    if max_rating < rating:
        max_rating = rating
        name_max = name

    elif min_rating > rating:
        min_rating = rating

    average += rating / number_films

print(f"{name_max} is with highest rating: {max_rating:.1f}")
print(f"{name} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {average:.1f}")
