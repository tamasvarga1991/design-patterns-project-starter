# Personal Finance Manager — Design Patterns Project

This project is a hands-on exercise in applying Object-Oriented Design Patterns to build a simplified personal finance manager.
You will implement and extend starter code to add functionality such as tracking transactions, adapting external data, observing balance changes, and ensuring proper architectural patterns.

## Getting Started

### Dependencies

Make sure you have python version >= 3.10.x installed on your computer. 


### Installation

1. Clone the repo:

```
bash
git clone https://github.com/udacity/cd14600-project-starter.git
cd cd14600-project-starter/starter
```

2. Run the Program: 
```
python main.py
```

## Testing

This project uses Python’s built-in unittest framework.

To run all tests:

```
python -m unittest discover
```

To run a single test file:
```
python -m unittest balance/test_balance_observer.py
```

### Break Down Tests

- test_balance.py → Verifies correct implementation of the Singleton Balance class.
- test_transaction.py → Confirms transactions update balances correctly.
- test_transaction_adapter.py → Ensures external income data is correctly adapted into Transaction objects.
- test_balance_observer.py → Validates that low-balance alerts are triggered at the correct threshold.

## Project Instructions

1. Implement Singleton Balance Class – Ensure only one balance object exists throughout the app.
2. Complete Transaction Class – Handle income and expense transactions.
3. Implement Adapter Pattern – Adapt external freelance income data into internal Transaction objects.
4. Implement Observer Pattern – Create a low balance observer that triggers an alert when funds drop too low.
5. Add Unit Tests – Write tests for all implemented functionality.
6. Choose and Implement a Fourth Pattern – Pick one additional design pattern (e.g., Strategy, Command, Decorator, etc.) and integrate it into your project.
7. Provide a Reflection – Add a short write-up in your repo (README or separate file) explaining your design choices.

## Reflection

### Design Patterns Used

This project implements four design patterns: Singleton, Observer, Adapter, and Strategy.

### Singleton Pattern

The Singleton pattern was used in the Balance class to ensure that only one balance instance exists throughout the application. This guarantees that all transactions update the same balance and prevents inconsistencies caused by multiple balance objects.

### Observer Pattern

The Observer pattern was implemented using PrintObserver and LowBalanceAlertObserver. Whenever the balance changes, registered observers are notified automatically. This approach keeps notification logic separate from balance management and makes it easy to add new observers in the future.

### Adapter Pattern

The Adapter pattern was implemented through TransactionAdapter. It converts ExternalFreelanceIncome objects into the internal Transaction format used by the system. This makes it possible to integrate external data sources without modifying existing business logic.

### Strategy Pattern

The Strategy pattern was implemented using BudgetPlanner and multiple budgeting strategies. Different budgeting rules, such as the 50/30/20 strategy and the 70/20/10 strategy, can be selected dynamically at runtime. This allows budgeting behavior to change without modifying the planner itself.

### Trade-offs and Challenges

The main challenge was selecting a fourth design pattern that fit naturally within a personal finance application. The Strategy pattern was chosen because budgeting rules represent interchangeable algorithms and provide a clear demonstration of runtime behavior changes. Overall, the use of design patterns improved modularity, maintainability, and flexibility while keeping the code easy to understand.

## Built With

* [Python](https://www.python.org/) – Main programming language
* [unittest](https://docs.python.org/3/library/unittest.html) – Testing framework
* [PEP8](https://peps.python.org/pep-0008/) – Style guide for Python code

## License

[License](LICENSE.txt)
