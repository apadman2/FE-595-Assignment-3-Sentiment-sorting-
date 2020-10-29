# libraries needed
import csv
import pandas as pd
from collections import Counter


# creating two empty lists
name = []
purpose = []

# reading my csv file
with open('Assignment3_question2.csv') as q1:
    q1_data = csv.reader(q1)
    for row in q1_data:
        if row[1] != "Name":
            x = row[1]
            y = row[2]
            name.append(x)
            purpose.append(y)

# creating data frame
result = pd.DataFrame({"Name": name, "Purpose": purpose}, index=range(1, 201))

# creating list of tokens
token = {}
def frequent_token(text):
    words = text
    words = words.split()
    for t in words:
        if t not in token:
            token[t] = 0
        token[t] += 1
    return token
for i in purpose:
    frequent_token(i)

frequent = Counter(token)
top_ten = frequent.most_common(10)

print("10 most common words:")

for i in top_ten:
    print(i[0], "-", i[1], " ")
