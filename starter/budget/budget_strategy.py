class BudgetStrategy:
    """Interface for calculating a budget from an income amount."""

    def create_budget(self, income):
        """Return an allocation of income across budget categories."""
        raise NotImplementedError("Subclasses must implement create_budget.")


class FiftyThirtyTwentyStrategy(BudgetStrategy):
    """Allocate income as 50% needs, 30% wants, and 20% savings."""

    def create_budget(self, income):
        return {
            "needs": income * 0.50,
            "wants": income * 0.30,
            "savings": income * 0.20,
        }


class SeventyTwentyTenStrategy(BudgetStrategy):
    """Allocate income as 70% needs, 20% wants, and 10% savings."""

    def create_budget(self, income):
        return {
            "needs": income * 0.70,
            "wants": income * 0.20,
            "savings": income * 0.10,
        }
