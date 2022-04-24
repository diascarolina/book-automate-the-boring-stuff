import random

number_of_streaks = 0
heads_tails_list = []

for experiment_number in range(10_000):
    if random.randint(0 ,1):
        heads_tails_list.append('H')
    else:
        heads_tails_list.append('T')


range_size = 6
heads = []
tails = []

for length_range in range(range_size):
    heads.append('H')
    tails.append('T')

heads_tails_list = ''.join(str(e) for e in heads_tails_list)
heads = ''.join(str(e) for e in heads)
tails = ''.join(str(e) for e in tails)

number_of_streaks = heads_tails_list.count(heads or tails)

print(number_of_streaks)