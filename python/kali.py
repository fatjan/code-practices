def price_system_b(n, perc, ticket):
    harga = ticket
    for _ in range(n):
        harga *= perc
    return harga

def movie(card, ticket, perc):
    n = 1
    system_a = ticket
    system_b = card
    total = 1
#     first price for system B 
#     system_b = card + ticket * perc
    while system_a > system_b:
        system_a *= ticket
        system_b += price_system_b(n, perc, ticket)
        n += 1
        total += 1
    return total

# def movie(card, ticket, perc):
#     n = 1
#     system_a = ticket * 1
#     system_b = card
#     total = 1
# #     first price for system B 
# #     system_b = card + ticket * perc
#     while system_a > system_b:
#         system_a = ticket * n
#         system_b += price_system_b(n, perc, ticket)
#         n += 1
#         total += 1
#     print(total)

# print(price_system_b(2,0.8,50))
print(movie(500,15,0.9))