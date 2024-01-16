class Bank:
    def __init__(self,name,balanse):
        self._name = name 
        self._balanse = balanse


    def MoneyX(self):
        amount = float(input('Введите сумму которую хотите добавить на счет :'))
        self._balanse += amount


    def _kill(self):
        self._balanse = 0

    def _djackpot(self):
        self._balanse *=10


    def _merge_balance(self, other_bank):
        self._balanse += other_bank._balanse
        other_bank._balanse = 0

        
my_account = Bank(name="My Account", balanse=100)
your_account = Bank(name="Your Account", balanse=76767)

print(f"{my_account._name} balanse: {my_account._balanse}")
print(f"{your_account._name} balanse: {your_account._balanse}")

my_account.MoneyX()
print(f"{my_account._name} balance after adding money: {my_account._balanse}")

my_account._djackpot()
print(f"{my_account._name} balance after jackpot: {my_account._balanse}")

my_account._merge_balance(your_account)
print(f"{my_account._name} balance after merging with {your_account._name}: {my_account._balanse}")
print(f"{your_account._name} balance after merging with {my_account._name}: {your_account._balanse}")








class Calculator:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Calculator(self.value + other.value)

    def __sub__(self, other):
        return Calculator(self.value - other.value)

    def __mul__(self, other):
        return Calculator(self.value * other.value)

    def __truediv__(self, other):
        if other.value == 0:
            raise ValueError("Division by zero is not allowed.")
        return Calculator(self.value / other.value)

    def __repr__(self):
        return f"Calculator({self.value})"

# Пример использования:
num1 = Calculator(5)
num2 = Calculator(3)

sum_result = num1 + num2
print(f"Sum: {sum_result}")

difference_result = num1 - num2
print(f"Difference: {difference_result}")

product_result = num1 * num2
print(f"Product: {product_result}")

quotient_result = num1 / num2
print(f"Quotient: {quotient_result}")
