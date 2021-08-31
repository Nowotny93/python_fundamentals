string = input()

digits = [int(i) for i in string if i.isdigit()]
chars = [j for j in string if not j.isdigit()]
take_list = [digits[t] for t in range(len(digits)) if t % 2 == 0]
skip_list = [digits[s] for s in range(len(digits)) if s % 2 == 1]


