class BankAccount:
	def __init__(self, customer_id, name, starting_balance=0):
		self.customer_id = customer_id
		self.name = name
		self.balance = starting_balance
		self.transactions = {}
	def print_account_info(self):
		print(f"Customer ID: {self.customer_id}")
		print(f"Name: {self.name}")
		print(f"Balance: ${self.balance:.2f}")
	def deposit(self, amount):
		if amount > 0:
			self.balance += amount
			self.transactions[f"Deposit #{len(self.transactions) + 1}"] = amount
			print(f"Deposited ${amount: .2f}")
		else:
			print("deposit amount must be positive")
	def withdraw(self, amount):
		if amount > 0:
			if amount <= self.balance:
				self.balance -= amount
				self.transactions[f"Withdrawal #{len(self.transactions) + 1}"] = -amount
				print(f"Withdrew ${amount: .2f}]")
			else:
				print("Insufficient balance")
		else:
			print("Withdrawal amount must be postive")
	def print_transactions(self):
		for transaction, amount in self.transactions.items():
			transaction_type = "Deposit" if amount > 0 else "Withdrawal"
			print(f"{transaction_type}: ${abs(amount):.2f}")

