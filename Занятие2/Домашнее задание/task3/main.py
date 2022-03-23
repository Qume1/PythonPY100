A = int(input())
B = int(input())
C = int(input())
# A_cond = A < 45 and B >= 45 and C >= 0
# B_cond = A >= 45 and B < 45 and C >= 45
# C_cond = A >= 45 and B >= 45 and C < 45
if (A < 45 and B >= 45 and C >= 0) or (A >= 45 and B < 45 and C >= 45) or (A >= 45 and B >= 45 and C < 45):
    print(True)
else:
    print(False)