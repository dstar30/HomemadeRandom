from HomemadeRandom import Random

print("=====Starting Goodness-of-Fit Test=====")
print("alpha=0.05, k=5")
print("chi-squared with alpha of 0.05 and 5 degrees of freedom -> 9.49 (from the Chi-square Table)")
print("======================================")

chi_squared_thres = 9.49

def calculate_chi_square(O):
    expected = 20000
    chi_squared = 0    
    for o in O:
        chi_squared += ((o-expected)**2)/expected
    
    return chi_squared

for i in range(10):
    seed = (i+7) * 105
    RV = Random(seed=seed)
    O_i = [0,0,0,0,0]
    
    for _ in range(100000):
        n = RV.random()
        if 0 <= n < 0.2:
            O_i[0] += 1
        elif 0.2 <= n < 0.4:
            O_i[1] += 1
        elif 0.4 <= n < 0.6:
            O_i[2] += 1
        elif 0.6 <= n < 0.8:
            O_i[3] += 1
        else:
            O_i[4] += 1
    
    chi_squared = calculate_chi_square(O_i)
    
    if chi_squared < chi_squared_thres:
        print("Observed chi_squared: " + str(chi_squared))
        print("Fail to reject null hypothese -> observations are approxmiately uniform")
        print("======================================")
    else:
        print("Observed chi-square higher than threshold, reject null hypothese -> observations are NOT approxmiately uniform")
        print("======================================")