def compute_summary(transactions):
    income = sum(t.amount for t in transactions if t.type == "income")
    expense = sum(t.amount for t in transactions if t.type =="expense")
    return{
        "income": income,
        "expense": expense,
        "balance": income - expense
    }