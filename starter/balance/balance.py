# balance.py

from transaction.transaction_category import TransactionCategory

class Balance:
    """Singleton to track the balance."""

    _instance = None

    def __init__(self):
        """Initialize the balance. Prevent direct instantiation."""
        self._balance = 0.0
        self._observers = []

    @classmethod
    def get_instance(cls):
        """Return the single Balance instance."""
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def reset(self):
        """Reset the net balance to zero."""
        self._balance = 0.0

    def add_income(self, amount):
        """Add income to the balance."""
        self._balance += amount

    def add_expense(self, amount):
        """Subtract expense from the balance."""
        self._balance -= amount

    def apply_transaction(self, transaction):
        """
        Apply a Transaction object to update the balance.

        Args:
            transaction (Transaction): The transaction to apply.
        """
        if transaction.category == TransactionCategory.INCOME:
            self.add_income(transaction.amount)
        elif transaction.category == TransactionCategory.EXPENSE:
            self.add_expense(transaction.amount)
        else:
            raise ValueError(f"Unsupported transaction category: {transaction.category}")

        for observer in self._observers:
            observer.update(self._balance, transaction)

    def register_observer(self, observer):
        """Register an observer for transaction updates."""
        self._observers.append(observer)

    def get_balance(self):
        """Get the current net balance."""
        return self._balance

    def summary(self):
        """Return a summary string of the net balance."""
        return f"Balance: ${self._balance:.2f}"
    
