from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
    
def sentimentanalysis():
    file=pd.read_csv('C:/Users/lenovo/Documents/FE595-HW3/all.csv')
    
    # Call vader sentiment
    vad=SentimentIntensityAnalyzer()
    
    # Created a new column to record sentiment analysis result
    file["score"]=file["purpose"].apply(lambda x:vad.polarity_scores(x)['compound'])
    
    # Find the company with the max and min score
    max=file.iloc[file["score"].idxmax()]["name"]
    min=file.iloc[file["score"].idxmin()]["name"]
    print("Best business idea:",max)
    print("Worst business idea:",min)

if __name__ == "__main__":
    sentimentanalysis()
