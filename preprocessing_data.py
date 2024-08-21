import csv
import pymongo

class User:
    def __init__(self, age, gender, total_income, expenses):
        self.age = age
        self.gender = gender
        self.total_income = total_income
        self.expenses = expenses

    def to_dict(self):
        return {
            "age": self.age,
            "gender": self.gender,
            "total_income": self.total_income,
            "expenses": self.expenses
        }

def fetch_data():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["survey_db"]
    collection = db["user_data"]
    return list(collection.find())

def save_to_csv(data, filename="user_data.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Age", "Gender", "Total Income", "Utilities", "Entertainment", "School Fees", "Shopping", "Healthcare"])
        for item in data:
            writer.writerow([
                item['age'],
                item['gender'],
                item['total_income'],
                item['expenses'].get('utilities', 0),
                item['expenses'].get('entertainment', 0),
                item['expenses'].get('school_fees', 0),
                item['expenses'].get('shopping', 0),
                item['expenses'].get('healthcare', 0)
            ])

if __name__ == "__main__":
    data = fetch_data()
    save_to_csv(data)
