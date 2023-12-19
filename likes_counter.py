def likes(names):
    count_likes = len(names)
    if count_likes == 0:
        return "no one likes this"
    elif count_likes == 1:
        return names[0] + " likes this"
    elif count_likes == 2: 
        return names[0] + " and " + names[1] + " like this"
    elif count_likes == 3:
        return names[0] + ", " + names[1] + " and " + names[2] + " like this"
    else:
        return names[0] + ", " + names[1] + " and " + f"{count_likes - 2}" + " others like this"

res = likes(["John", "Bob", "Anna", "Jim"])
print(res)