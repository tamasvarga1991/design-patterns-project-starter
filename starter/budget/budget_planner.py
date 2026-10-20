from budget.budget_strategy import BudgetStrategy


class BudgetPlanner:
    """Create budget plans using a selected budgeting strategy."""

    def __init__(self, strategy: BudgetStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: BudgetStrategy):
        """Change the strategy used to create budget plans."""
        self.strategy = strategy

    def create_budget(self, income):
        """Create a budget plan for the given income."""
        return self.strategy.create_budget(income)
