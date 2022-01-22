#2s complement signed

#if you are given a number, any number give it to me in 2s complement
#8 bit reader from -256 to 255
#if given an arbitrary number, we should identify if the number is positive or negative
#we should identify the level of greatness or smallness with respect to the sign
#if the number if
#
#class Signed_Complement:
#    def __init__(self, number):
#        self._number = number
#
#    def
#
#    def grouper(self):
#        """
#        :param number: input
#        :return:
#        """
#        counter = 1
#        next_count = 0
#        for value in range(counter, abs(self._number), 2* counter):
#            counter *= 2
#            if abs(self._number) >= value:
#                next_count += 1
#                continue
#            else:
#                return next_count
#    def final_product(self):
#        number_place = grouper(self._number)


#Alien Integer Problem A
# represent data in a set of sets
#number_given = [2,4]
#number_line = {{0},{1},{2},{3},{4},{5},{6},{7},{8},{9}}
#def sets(number_line):
#    if len(number_line) > 1024:
#        break
#    else:
#        for set in number_line:
#            number_line.append{num}
#            return sets(number_line)

#def numbers(number_given, set_of_sets):
#    closeness = 0
#    for idx in range(0,9):
#        if idx in number_given:
#            closeness += 1
#    return closeness
#Mult!
#lst_1 = [10,8,3,12,6,24,14,12,9,70,5]
#def mult(lst):
#    special_num = lst[1]
#    for idx in range(2,len(lst)):
#        while lst[idx] > 0:
#            lst[idx] -= special_num
#            if lst[idx] == 0 and idx == (len(lst_1) -1):
#                return idx
#            else:
#                return mult(lst[idx:])
#
#def other(idx, pencil):
#    return pencil[idx]

#def mult(lst):
#    special_num = lst[1]
#    for idx in range(2, len(lst)-1):
#        while lst[idx] > 0:
#            lst[idx] -= special_num
#            if lst[idx] == 0 and idx == (len(lst_1)-1):
#print(mult(lst_1))

#MRcodeformatgrader Problem G
#input = [100, 10, 2, 3, 5, 10, 11, 12, 25, 26, 88, 89]

#def mr_code_format(input):
#    address_log = {}
#    errors = []
#    correct = []
#    for number in range(input[0]):
#        address_log[number] = False
#    for idx in range(2, len(input[1:]) + 1):
#        address_log[input[idx]] = True
#    key_list = list(address_log.keys())
#    value_list = list(address_log.values())
#    for key in key_list:
#        if address_log[key] == True:
#            errors.append(key)
#        if address_log[key] == False:
#            correct.append(key)
#    for count in range(len(errors)-1):
#        if errors[count] == errors[count + 1]:
#            errors.pop(count)
#            together = errors[(count - count + 1)]
#            errors[count] = errors[together]
#    return 'Errors:', errors, 'Correct:', correct
#
#print(mr_code_format(input))
#
#hey = [2, 3, 4, 8]
#bye = [99,100,101,102,103,104,109]
#
#def function(errors):
#    count = 1
#    for idx in range(len(errors)-1):
#        for index in range(len(errors)-1):
#            count = 1
#            while errors[idx] + count == errors[index]:
#                count += 1
#                errors[idx + count] =errors[idx]," - ",errors[idx + count]
#                errors.pop(idx + count)
#            break
#    return errors
#
#def frick(correct):
#    for idx in range(len(correct)-1):
#        for index in range(len(correct)-1):
#            count = 1
#            while correct[idx] + count == correct[index]:
#                count += 1
#                correct[idx + count] = correct[idx]," - ",correct[idx + count]
#                correct.pop(idx + count)
#    return correct
#print(function(hey))
#print(frick(hey))

#match = ["peppers", "if spinach and olives then tomatoes", "spinach", "olives"]
#def pizza(input):
#    """
#    :param input: We are trying to stay under the amount of toppings in the first item of the list.
#    rest are either statements or if then statements
#    or absolutes
#    :return: toppings required
#    """
#    absolute = []
#    propositions = []
#    counter = 0
#    for item in input:
#        if 6 < len(item) > 10:
#            absolute.append(item)
#        else:
#            propositions.append(item)
#    for idx in range(1,len(propositions)-1):
#        if len(input[idx]) < 10:
#            counter += 1
#        else:
#            if 'and' in input[idx]: #contains an 'and':
#                if str(input[idx])[3:13] and str(input[idx])[13:23]:#two items before and after are in the input:
#                    counter += 1
#            if 'or' in input[idx]:
#                if str(input[idx])[3:13] or str(input[idx])[13:23]:
#                    counter += 1
#    return counter
#print(pizza(match))