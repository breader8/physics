class Numbers:

    """
    The Errors class is used to define
    a number using its significant digits.
    """

    def __init__(self, number):
        """
        It initializes the object and
        get the significant digits
        following the established rules
        during physics conventions.
        """
        significant_digits = 0
        new_number = ''
        zero_encountered = False
        for digit in str(number):
            if digit is '.':
                new_number += '.'
                continue
            if zero_encountered:
                significant_digits += 1
                new_number += digit
            elif digit != '0' and not zero_encountered:
                zero_encountered = True
                significant_digits += 1
                new_number += digit

        self.significant_digits = significant_digits
        self.number = float(new_number)

    def __isub__(self, other_number):
        """
        That function is used to
        estabilish the result of
        a Subtraction, using significant
        digits.
        """
        if isinstance(other_number, Numbers):
            if other_number.significant_digits > self.significant_digits:
                return Numbers(round((self.number - other_number.number), self.significant_digits))
            else:
                return Numbers(round((self.number - other_number.number), other_number.significant_digits))

        else:
            x = Numbers(int(other_number))
            if x.significant_digits > self.significant_digits:
                return Numbers(round((self.number - x.number), self.significant_digits))
            else:
                return Numbers(round((self.number - x.number), x.significant_digits))

    def __rsub__(self, other_number):
        """
        That function is used to
        estabilish the result of
        a Subtraction, using significant
        digits.
        """
        if isinstance(other_number, Numbers):
            if other_number.significant_digits > self.significant_digits:
                return Numbers(round((self.number - other_number.number), self.significant_digits))
            else:
                return Numbers(round((self.number - other_number.number), other_number.significant_digits))

        else:
            x = Numbers(int(other_number))
            if x.significant_digits > self.significant_digits:
                return Numbers(round((self.number - x.number), self.significant_digits))
            else:
                return Numbers(round((self.number - x.number), x.significant_digits))

    def __sub__(self, other_number):
        """
        That function is used to
        estabilish the result of
        a Subtraction, using significant
        digits.
        """
        if isinstance(other_number, Numbers):
            if other_number.significant_digits > self.significant_digits:
                return Numbers(round((self.number - other_number.number), self.significant_digits))
            else:
                return Numbers(round((self.number - other_number.number), other_number.significant_digits))

        else:
            x = Numbers(int(other_number))
            if x.significant_digits > self.significant_digits:
                return Numbers(round((self.number - x.number), self.significant_digits))
            else:
                return Numbers(round((self.number - x.number), x.significant_digits))

    def __iadd__(self, other_number):
        """
        That function is used to
        estabilish the result of
        an Addition, using significant
        digits.
        """
        if isinstance(other_number, Numbers):
            if other_number.significant_digits > self.significant_digits:
                return Numbers(round((self.number + other_number.number), self.significant_digits))
            else:
                return Numbers(round((self.number + other_number.number), other_number.significant_digits))

        else:
            x = Numbers(int(other_number))
            if x.significant_digits > self.significant_digits:
                return Numbers(round((self.number + x.number), self.significant_digits))
            else:
                return Numbers(round((self.number + x.number), x.significant_digits))

    def __radd__(self, other_number):
        """
        That function is used to
        estabilish the result of
        an Addition, using significant
        digits.
        """
        if isinstance(other_number, Numbers):
            if other_number.significant_digits > self.significant_digits:
                return Numbers(round((self.number + other_number.number), self.significant_digits))
            else:
                return Numbers(round((self.number + other_number.number), other_number.significant_digits))

        else:
            x = Numbers(int(other_number))
            if x.significant_digits > self.significant_digits:
                return Numbers(round((self.number + x.number), self.significant_digits))
            else:
                return Numbers(round((self.number + x.number), x.significant_digits))

    def __add__(self, other_number):
        """
        That function is used to
        estabilish the result of
        an Addition, using significant
        digits.
        """
        if isinstance(other_number, Numbers):
            if other_number.significant_digits > self.significant_digits:
                return Numbers(round((self.number + other_number.number), self.significant_digits))
            else:
                return Numbers(round((self.number + other_number.number), other_number.significant_digits))

        else:
            x = Numbers(int(other_number))
            if x.significant_digits > self.significant_digits:
                return Numbers(round((self.number + x.number), self.significant_digits))
            else:
                return Numbers(round((self.number + x.number), x.significant_digits))

    def __rfloordiv__(self, other_number):
        """
        That function is used to
        estabilish the result of
        a Division, using significant
        digits.
        """
        if isinstance(other_number, Numbers):
            if other_number.significant_digits > self.significant_digits:
                return Numbers(round((self.number / other_number.number), self.significant_digits))
            else:
                return Numbers(round((self.number / other_number.number), other_number.significant_digits))

        else:
            return Numbers(round((self.number / other_number), self.significant_digits))

    def __ifloordiv__(self, other_number):
        """
        That function is used to
        estabilish the result of
        a Division, using significant
        digits.
        """
        if isinstance(other_number, Numbers):
            if other_number.significant_digits > self.significant_digits:
                return Numbers(round((self.number / other_number.number), self.significant_digits))
            else:
                return Numbers(round((self.number / other_number.number), other_number.significant_digits))

        else:
            return Numbers(round((self.number / other_number), self.significant_digits))

    def __floordiv__(self, other_number):
        """
        That function is used to
        estabilish the result of
        a Division, using significant
        digits.
        """
        if isinstance(other_number, Numbers):
            if other_number.significant_digits > self.significant_digits:
                return Numbers(round((self.number / other_number.number), self.significant_digits))
            else:
                return Numbers(round((self.number / other_number.number), other_number.significant_digits))

        else:
            return Numbers(round((self.number / other_number), self.significant_digits))

    def __itruediv__(self, other_number):
        """
        That function is used to
        estabilish the result of
        a Division, using significant
        digits.
        """
        if isinstance(other_number, Numbers):
            if other_number.significant_digits > self.significant_digits:
                return Numbers(round((self.number / other_number.number), self.significant_digits))
            else:
                return Numbers(round((self.number / other_number.number), other_number.significant_digits))

        else:
            return Numbers(round((self.number / other_number), self.significant_digits))

    def __rtruediv__(self, other_number):
        """
        That function is used to
        estabilish the result of
        a Division, using significant
        digits.
        """
        if isinstance(other_number, Numbers):
            if other_number.significant_digits > self.significant_digits:
                return Numbers(round((self.number / other_number.number), self.significant_digits))
            else:
                return Numbers(round((self.number / other_number.number), other_number.significant_digits))

        else:
            return Numbers(round((self.number / other_number), self.significant_digits))

    def __truediv__(self, other_number):
        """
        That function is used to
        estabilish the result of
        a Division, using significant
        digits.
        """
        if isinstance(other_number, Numbers):
            if other_number.significant_digits > self.significant_digits:
                return Numbers(round((self.number / other_number.number), self.significant_digits))
            else:
                return Numbers(round((self.number / other_number.number), other_number.significant_digits))

        else:
            return Numbers(round((self.number / other_number), self.significant_digits))

    def __mul__(self, other_number):
        """
        That function is used to
        estabilish the result of
        a Multiplication, using significant
        digits.
        """
        if isinstance(other_number, Numbers):
            if other_number.significant_digits > self.significant_digits:
                return Numbers(round((self.number * other_number.number), self.significant_digits))
            else:
                return Numbers(round((self.number * other_number.number), other_number.significant_digits))

        else:
            return Numbers(round((self.number * other_number), self.significant_digits))

    def __rmul__(self, other_number):
        """
        That function is used to
        estabilish the result of
        a Multiplication, using significant
        digits.
        """
        if isinstance(other_number, Numbers):
            if other_number.significant_digits > self.significant_digits:
                return Numbers(round((self.number * other_number.number), self.significant_digits))
            else:
                return Numbers(round((self.number * other_number.number), other_number.significant_digits))

        else:
            return Numbers(round((self.number * other_number), self.significant_digits))

    def __imul__(self, other_number):
        """
        That function is used to
        estabilish the result of
        a Multiplication, using significant
        digits.
        """
        if isinstance(other_number, Numbers):
            if other_number.significant_digits > self.significant_digits:
                return Numbers(round((self.number * other_number.number), self.significant_digits))
            else:
                return Numbers(round((self.number * other_number.number), other_number.significant_digits))

        else:
            return Numbers(round((self.number * other_number), self.significant_digits))

    def __abs__(self):
        """
        That function is used to
        obtain the absolute value
        of the number.
        """
        return abs(self.number)

    def __neg__(self):
        """
        That function is used to
        return the negative value
        of the chosen number.
        """
        return -(abs(self.number))

    def __pos__(self):
        """
        That function is used to
        return the positive value
        of the chosen number.
        """
        return abs(self.number)

    def __invert__(self):
        """
        That function is used to
        return the inverted value
        of the chosen number.
        """
        return ~self.number

    def __len__(self):
        """
        That function is used to
        return the number of
        digits of the
        chosen number.
        """
        return len(str(self.number))

    def __int__(self):
        """
        That function is used to
        return the integer
        of the chosen number.
        """
        return self.number

    def __str__(self):
        """
        That function is used to
        return a string rappresentation
        of the chosen number.
        """
        return str(self.number)

    def __float__(self):
        """
        That function is used to
        return the float
        of the chosen number.
        """
        return float(self.number)

    def __round__(self, digits=0):
        """
        That function is used to
        round the chosen number.
        """
        return round(self.number, digits)

    def __lt__(self, other_number):
        """
        That function is used to
        compare two numbers
        using "<".
        """
        if isinstance(other_number, Numbers):
            if (self.nu < other_number.number):
                return True
            else:
                return False
        else:
            return self < Numbers(other_number)

    def __le__(self, other_number):
        """
        That function is used to
        compare two numbers
        using "<=".
        """
        if isinstance(other_number, Numbers):
            if (self.number <= other_number.number):
                return True
            else:
                return False
        else:
            return self <= Numbers(other_number)

    def __eq__(self, other_number):
        """
        That function is used to
        compare two numbers
        using "==".
        """
        if isinstance(other_number, Numbers):
            if (self.significant_digits ==
                other_number.significant_digits) and (self.number ==
               other_number.number):
                return True
            else:
                return False
        else:
            return self == Numbers(other_number)

    def __ne__(self, other_number):
        """
        That function is used to
        compare two numbers
        using "!=".
        """
        if isinstance(other_number, Numbers):
            if (self.significant_digits !=
                other_number.significant_digits) and (self.number !=
               other_number.number):
                return True
            else:
                return False
        else:
            return self != Numbers(other_number)

    def __gt__(self, other_number):
        """
        That function is used to
        compare two numbers
        using ">".
        """
        if isinstance(other_number, Numbers):
            if (self.number > other_number.number):
                return True
            else:
                return False
        else:
            return self > Numbers(other_number)

    def __ge__(self, other_number):
        """
        That function is used to
        compare two numbers
        using ">=".
        """
        if isinstance(other_number, Numbers):
            if (self.number >= other_number.number):
                return True
            else:
                return False
        else:
            return self >= Numbers(other_number)
