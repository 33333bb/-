import math
def binomial_distribution(n, p):
    distribution = []
    for k in range(n + 1):
        comb = math.comb(n, k)
        probability = comb * (p ** k) * ((1 - p) ** (n - k))
        distribution.append(probability)
    return distribution
def cumulative_distribution(list1):
    list2 = []
    cumulative_sum = 0
    for prob in list1:
        cumulative_sum += prob
        list2.append(cumulative_sum)
    return list2
def compute_list3(list2):
    list3 = []
    for value in list2:
        result = 1 / (value + 0.03)
        list3.append(result)
    return list3
def compute_list4(list2):
    list4 = []
    for value in list2:
        result = 1 / (1.03 - value)
        list4.append(result)
    return list4
def main(n,p,rr):
    list1 = binomial_distribution(n, p)
    list2 = cumulative_distribution(list1)
    list3 = compute_list3(list2)
    list4 = compute_list4(list2)
    print(f"{'k':<10} | {'Over':<10} | {'Under':<10}")
    for k in range(len(list3)):
        if (list3[k] < 1.001 and list4[k] > 9.999) or (list3[k] > 9.999 and list4[k] <1.001):
            continue
        if list3[k] < 1.001:list3_value = 1.001
        elif list3[k] > 9.999:list3_value = 9.999
        else:list3_value = list3[k]
        if list4[k] < 1.001:list4_value = 1.001
        elif list4[k] > 9.999:list4_value = 9.999
        else:list4_value = list4[k]
        print(f"{k + rr + 0.5:<10} | {list4_value:<10.3f} | {list3_value:<10.3f}")

if __name__ == "__main__":
    n = int(input("n: "))
    p = float(input("p: "))
    rr = int(input("rr: "))
    while n>0:
        main(n,p,rr)
        n-=1
        print(f'{n+1} chances are remaining and {rr} success has been achieved.')
        try:tmp=int(input('1?'))
        except:tmp=0
        rr+=tmp
    print(f'all chances are used and {rr} success is the result.')
