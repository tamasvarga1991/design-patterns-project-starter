import unittest

from budget.budget_planner import BudgetPlanner
from budget.budget_strategy import (
    FiftyThirtyTwentyStrategy,
    SeventyTwentyTenStrategy,
)


class TestBudgetPlanner(unittest.TestCase):

    def test_fifty_thirty_twenty_strategy(self):
        planner = BudgetPlanner(FiftyThirtyTwentyStrategy())

        budget = planner.create_budget(1000)

        self.assertEqual(
            budget,
            {"needs": 500, "wants": 300, "savings": 200},
        )

    def test_seventy_twenty_ten_strategy(self):
        planner = BudgetPlanner(SeventyTwentyTenStrategy())

        budget = planner.create_budget(1000)

        self.assertEqual(
            budget,
            {"needs": 700, "wants": 200, "savings": 100},
        )

    def test_strategy_can_be_changed(self):
        planner = BudgetPlanner(FiftyThirtyTwentyStrategy())
        planner.set_strategy(SeventyTwentyTenStrategy())

        budget = planner.create_budget(1000)

        self.assertEqual(
            budget,
            {"needs": 700, "wants": 200, "savings": 100},
        )


if __name__ == "__main__":
    unittest.main()
