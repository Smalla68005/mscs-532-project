class UserTransactionHistory:
    def __init__(self):
        # Dictionary where the key is the user (e.g., user ID or name)
        # and the value is a list of their transactions.
        self.history = {}

    # Method to add a transaction for a specific user.
    def add_transaction(self, user, transaction):
        # Check if the user is not already in the history dictionary.
        if user not in self.history:
            self.history[user] = []
        self.history[user].append(transaction)

    # Method to retrieve the transaction history for a specific user.
    def get_history(self, user):
        return self.history.get(user, [])
