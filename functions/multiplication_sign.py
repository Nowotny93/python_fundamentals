def pos_neg_zero(num_1, num_2, num_3):
    if (num_1 > 0 and num_2 > 0 and num_3 > 0) or (num_1 < 0 and num_2 < 0 and num_3 > 0) or (num_1 < 0 and num_3 < 0 and num_2 > 0) or (num_3 < 0 and num_2 < 0 and num_1 > 0):
        return 'positive'
    elif (num_1 < 0 or num_2 < 0 or num_3 < 0) or (num_1 < 0 and num_2 < 0 and num_3 > 0) or (num_1 < 0 or num_3 < 0 and num_2 > 0) or (num_3 < 0 or num_2 < 0 and num_1 > 0):
        return 'negative'
    elif num_1 == 0 or num_2 == 0 or num_3 == 0:
        return 'zero'

int_1 = int(input())
int_2 = int(input())
int_3 = int(input())
print(pos_neg_zero(int_1, int_2, int_3))