def lcm(number1, number2): # imperative
    if (number1 > number2):
        max = number1
    else:
        max = number2
        while (True):
            if (max % num1 == 0 and max % num2 == 0):
                break
            max = max + 1
    return max

class LCM:
    def innit (self, num1, num2):
        self.number1 = num1
        self.number2 = num2

    def call(self):
        if self.num1 > self.num2:
            max = self.num1

        else:
            max = self.num
        while (True):
            if (max % self.num1 == 0 and max % self.num2 == 0):
                break
            max = max + 1
        return max


def run():
