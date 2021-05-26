import joblib

name = input("Enter Employee Name		: ", name)
exp = float(input("Enter Employee Experience	: ", name)
model = joblib.load('marks.pk1')

print("\n")
print("Name			: ", name)
print("Year of Experience	: ", exp)
sal = model.predict([[exp]])
print("Salary			: ", sal)
