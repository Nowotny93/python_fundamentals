days = int(input())
d_p = int(input())
expected_plunder = float(input())

gained_plunder = 0

for i in range(1, days + 1):
    gained_plunder = gained_plunder + d_p
    if i % 3 == 0:
        gained_plunder = gained_plunder + d_p * 0.5
    if i % 5 == 0:
        gained_plunder -= gained_plunder * 0.3

if gained_plunder >= expected_plunder:
    print(f'Ahoy! {gained_plunder:.2f} plunder gained.')
else:
    collected_percentage = (gained_plunder / expected_plunder) * 100
    print(f'Collected only {collected_percentage:.2f}% of the plunder.')