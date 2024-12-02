class CreditCard:
    @staticmethod
    def main():
        number = int(input("Enter a valid number:"))
        if CreditCard.isValid(number):
            print(f"{number} is valid")
        else:
            print(f"{number} is invalid")

    @staticmethod
    def isValid(number):
        size = CreditCard.getSize(number)
        if size < 13 or size > 16:
            return False
        if not (CreditCard.prefixMatched(number, 4) or CreditCard.prefixMatched(number, 5) or CreditCard.prefixMatched(number, 37) or CreditCard.prefixMatched(number, 6)):
            return False
        total_sum = CreditCard.sumOfDoubleEvenPlace(number) + CreditCard.sumOfOddPlace(number)
        return total_sum % 10 == 0
    @staticmethod
    def sumOfDoubleEvenPlace(number):
        sum_even = 0
        num_str = str(number)
        for i in range(len(num_str) - 2, -1, -2):
            doubled_value = int(num_str[i]) * 2
            sum_even += CreditCard.getDigit(doubled_value)
        return sum_even
    @staticmethod
    def getDigit(number):
        if number < 10:
            return number
        return (number // 10) + (number % 10)
    @staticmethod
    def sumOfOddPlace(number):
        sum_odd = 0
        num_str = str(number)
        for i in range(len(num_str) - 1, -1, -2):
            sum_odd += int(num_str[i])
        return sum_odd
    @staticmethod
    def prefixMatched(number, prefix):
        return str(number).startswith(str(prefix))

    @staticmethod
    def getSize(number):
        return len(str(number))

if __name__ == "__main__":
    CreditCard.main()
