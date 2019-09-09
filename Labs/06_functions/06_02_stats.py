'''
Write a script that takes in a list and finds the max, min, average and sum.

'''

inp1 = input("Enter a list of numbers: ")
def MinMax(a):
    listN = a.split()
    listN = [float(i) for i in listN]
    max_value = max(listN)
    min_Value = min(listN)
    avg_Value = sum(listN) / len(listN)
    sum_Value = sum(listN)
    print(f"Maximum value is {max_value}, minimum value is {min_Value}, average is {avg_Value}, sum is {sum_Value}")

MinMax(inp1)