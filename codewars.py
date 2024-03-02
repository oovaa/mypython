def quadrant(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x > 0 and y < 0:
        return 4
    elif x < 0 and y < 0:
        return 3


print(quadrant(1, -2))


# JadenCased= "How can mirrors be real if our eyes aren't real"
# s = [x.capitalize() for x in JadenCased.split()]
# ans = " ".join(s)

# print(ans)

#     #   print(JadenCased[i+1].upper())
# # print(JadenCased)
# o='omer'
# o=o.capitalize()
# print(o)
