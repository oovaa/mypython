from math import sqrt


def pickGifts(gifts: list[int], k: int) -> int:
    gifts = sorted(gifts, reverse=True)
    for i in range(min(len(gifts),k)):
        i = gifts.index(max(gifts))
        gifts[i] = int(sqrt(gifts[i]))
    # print((gifts))
    return sum(gifts)


gifts = [56,41,27,71,62,57,67,34,8,71,2,12,52,1,64,43,32,42,9,25,73,29,31]
k = 52

print(pickGifts(gifts, k))
