#2s complement signed

#if you are given a number, any number give it to me in 2s complement
#8 bit reader from -256 to 255
#if given an arbitrary number, we should identify if the number is positive or negative
#we should identify the level of greatness or smallness with respect to the sign
#if the number if

class Signed_Complement:
    def __init__(self, number):
        self._number = number

    def

    def grouper(self):
        """
        :param number: input
        :return:
        """
        counter = 1
        next_count = 0
        for value in range(counter, abs(self._number), 2* counter):
            counter *= 2
            if abs(self._number) >= value:
                next_count += 1
                continue
            else:
                return next_count
    def final_product(self):
        number_place = grouper(self._number)
