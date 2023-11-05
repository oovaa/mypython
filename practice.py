import random as rd


def randf(s, d):
    def f(s, d):
        return s + d

    def a(s, d):
        return s - d

    def c(s, d):
        return s * d

    funs = [f, a, c]

    return rd.choice(funs)(s, d)


print(randf(3, 4))
