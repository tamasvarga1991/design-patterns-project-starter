import unittest
from contextlib import redirect_stdout
from io import StringIO

from transaction.transaction import Transaction
from transaction.transaction_category import TransactionCategory
from balance.balance import Balance
from balance.balance_observer import LowBalanceAlertObserver


class TestLowBalanceAlertObserver(unittest.TestCase):

    def setUp(self):
        self.balance = Balance.get_instance()
        self.balance.reset()

    def test_alert_prints_warning_below_threshold(self):
        observer = LowBalanceAlertObserver(threshold=50)
        output = StringIO()

        with redirect_stdout(output):
            observer.update(49.99, None)

        self.assertEqual(output.getvalue(), "Low balance alert: $49.99\n")
        self.assertTrue(observer.alert_triggered)

    def test_alert_does_not_print_warning_at_or_above_threshold(self):
        observer = LowBalanceAlertObserver(threshold=50)
        output = StringIO()

        with redirect_stdout(output):
            observer.update(50, None)
            observer.update(60, None)

        self.assertEqual(output.getvalue(), "")
        self.assertFalse(observer.alert_triggered)

    def test_alert_triggers_on_low_balance(self):
        observer = LowBalanceAlertObserver(threshold=50)
        self.balance.register_observer(observer)

        self.balance.apply_transaction(
            Transaction(100, TransactionCategory.INCOME)
        )
        self.assertFalse(observer.alert_triggered)

        self.balance.apply_transaction(
            Transaction(60, TransactionCategory.EXPENSE)
        )
        self.assertTrue(observer.alert_triggered)

        self.balance.apply_transaction(
            Transaction(100, TransactionCategory.INCOME)
        )
        self.assertFalse(observer.alert_triggered)

        self.balance.apply_transaction(
            Transaction(60, TransactionCategory.EXPENSE)
        )
        self.assertFalse(observer.alert_triggered)

        self.balance.apply_transaction(
            Transaction(60, TransactionCategory.EXPENSE)
        )
        self.assertTrue(observer.alert_triggered)


if __name__ == "__main__":
    unittest.main()
