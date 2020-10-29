# libraries needed
import csv
import pprint
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


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

# sentiment analysis
analyzer = SentimentIntensityAnalyzer()
sent_score = []
for i in range(200):
    x = analyzer.polarity_scores(purpose[i]).get('compound')
    sent_score.append(x)

# adding compound score from sentiment analysis to 'result' dataframe
result['Compound_Score'] = sent_score

# finding row with maximum compound score
print("The company with the highest compound score after conducting Sentiment Analysis is: \n")
pprint.pprint(result[result.Compound_Score == result.Compound_Score.max()])
print("\n")

# finding row with minimum compound score
print("The companies with the lowest compound score after conducting Sentiment Analysis is: \n")
pprint.pprint(result[result.Compound_Score == result.Compound_Score.min()])
print("\n")


