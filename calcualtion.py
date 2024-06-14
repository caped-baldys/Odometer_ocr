import pandas as pd

data = pd.read_csv('output.csv')

real = list(data['Real'])
pred = list(data['Predicted'])

not_correct_pred = 0

for i,j in zip(real,pred):
    if float(i) != float(j) :
        not_correct_pred += 1
    print(i, "   ", j)

print(len(real))
print(not_correct_pred)
print("Accuracy:",not_correct_pred/len(real) * 100)