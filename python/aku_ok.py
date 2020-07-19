# def price_system_b(n, perc, ticket):
#     harga = ticket
#     for _ in range(n):
#         harga *= perc
#     return harga

# def movie(card, ticket, perc):
#     n = 1
#     system_a = ticket * 1
#     system_b = card
#     total = 1
# #     first price for system B 
# #     system_b = card + ticket * perc
#     while system_a < system_b:
#         system_a += ticket
#         print(system_a)
#         system_b += price_system_b(n, perc, ticket)
#         print(system_b)
#         n += 1
#         total += 1
#     return total

def movie(card, ticket, perc):
    n = 1
    system_a = ticket * 1
    price = perc * ticket
    system_b = card + price
    total = 1
    while system_a <= system_b:
        n += 1
        system_a += ticket
        price *= perc
        system_b += price
        print(system_b)
        total += 1
    return total

print(movie(500,15,0.9))