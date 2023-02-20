
#Step 1: reading the inputs
std__test__cases = input()
special_array = []
ele__count__list =[]
for i in range(0, int(std__test__cases)):
    str_input = int(input())
    array_ele = input()
    splitted_array_ele = array_ele.split(' ')
    mapped_array = list(map(int,splitted_array_ele))
    special_array.append(mapped_array)
    ele__count__list.append(str_input)

#Step 2: Generating the subsequences
def subsets(nums):
	b = []
	if not nums:#to check not empty
		b.append(nums)
	else:
		first = nums[0]
		second = nums[1:]
		for x in subsets(second):
			b.append(x)
			c = [first] + x
			b.append(c)
	return b



#Step 3: Performing Bitwise XOR and sum calculations

def bitwise_xor(arr):
    xor__init = 0
    for i in range(0,len(arr)):
        xor__init = xor__init ^ arr[i]
    return xor__init 

#Step 4 : Getting XOR and sum calculations

def final__operations(arr):
    result__count=0
    for i in range(1, len(arr)):
        xor__oper = bitwise_xor(arr[i])
        array_sum = sum(arr[i])
        if(array_sum == xor__oper):
            result__count += 1
    return result__count


#Step5: Generating result for multiple nested list
def nested__list():
    actual__count = []
    
    for i in special_array:
        subset_array= subsets(i)
        result = final__operations(subset_array)
        actual__count.append(str(result))

    return '\n'.join(actual__count)
    

output = nested__list()
print(output)


#Optimied Dynamic Programming
#Step 1: reading the inputs
std_test_cases = int(input())
inputs = []
for i in range(std_test_cases):
    str_input = int(input())
    array_ele = [int(x) for x in input().split()]
    inputs.append((str_input, array_ele))

#Step 2: Performing Bitwise XOR and sum calculations
def calculate_results(array):
    result_count = 0
    for i in range(1, 2 ** len(array)):
        xor_init = 0
        array_sum = 0
        for j in range(len(array)):
            if (i >> j) & 1:
                xor_init ^= array[j]
                array_sum += array[j]
        if array_sum == xor_init:
            result_count += 1
    return result_count


#Step 3: Generating result for multiple nested list
def nested_list():
    actual_count = []
    for str_input, array_ele in inputs:
        result = calculate_results(array_ele)
        actual_count.append(str(result))
    return '\n'.join(actual_count)


output = nested_list()
print(output)


Test cases :
2
3
2 1 6
2
4 5

Ouput:
5 
2



