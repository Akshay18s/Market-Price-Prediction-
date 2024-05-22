import streamlit as st
import joblib
import pandas as pd
from tensorflow.keras.models import load_model
import numpy as np
from datetime import date, timedelta
import requests
from bs4 import BeautifulSoup
from sklearn.linear_model import LinearRegression
import streamlit as st
import matplotlib.pyplot as plt

def scrape_headlines_with_onion_only_for_display():
      news = []
      urls = [
      'https://www.thehindu.com/topic/Agriculture/',
      'https://krishijagran.com/news',
      'https://economictimes.indiatimes.com/news/economy/agriculture?from=mdr',
      'https://www.agriwatch.com/news']
      for url in urls:
          response = requests.get(url)
          parsed_html = BeautifulSoup(response.content, 'html.parser')

          if 'thehindu' in url:
              headlines = parsed_html.find_all('h3')
          elif 'krishijagran' in url:
              headlines = parsed_html.find_all('h2')
          elif 'economictimes' in url:
              headlines = parsed_html.find_all('h1')
          elif 'agriwatch' in url:
              headlines = parsed_html.find_all('h1')

          for headline in headlines:
              if "onion" in headline.text.lower():
                  news.append(headline.text.strip())
      for i in news:
        st.write(i)
def lstm_predictions(next_days):
    def scrape_headlines_with_onion_only():
      news = []
      urls = [
      'https://www.thehindu.com/topic/Agriculture/',
      'https://krishijagran.com/news',
      'https://economictimes.indiatimes.com/news/economy/agriculture?from=mdr',
      'https://www.agriwatch.com/news']
      for url in urls:
          response = requests.get(url)
          parsed_html = BeautifulSoup(response.content, 'html.parser')

          if 'thehindu' in url:
              headlines = parsed_html.find_all('h3')
          elif 'krishijagran' in url:
              headlines = parsed_html.find_all('h2')
          elif 'economictimes' in url:
              headlines = parsed_html.find_all('h1')
          elif 'agriwatch' in url:
              headlines = parsed_html.find_all('h1')

          for headline in headlines:
              if "onion" in headline.text.lower():
                  news.append(headline.text.strip())
      return news
    
    def scrap_headlines_and_analyse_sentiment(scrapped_headlines):
      if len(scrapped_headlines)!=0:
        model = joblib.load("/content/sentiment_analyzer_news.pkl")
        count_sentiment = []
        feature_extraction = joblib.load("/content/features_of_text_again.pkl")
        for i in range(len(scrapped_headlines)):
          x = [scrapped_headlines[i]]
          input_data_features = feature_extraction.transform(x)
          prediction = model.predict(input_data_features)
          count_sentiment.append(prediction[0])
        emo = ["Negative","Neutral","Positive"]
        sentiment = [0,0,0]
        for i in range(len(count_sentiment)):
          if count_sentiment[i] == -1:
            sentiment[0]+=1
          if count_sentiment[i] == 0:
            sentiment[1]+=1
          else:
            sentiment[2]+=1
        max_ind = sentiment.index(max(sentiment))
        print("sentiments",sentiment)
        return emo[max_ind]
      else:
        return "Neutral"
    def scrap_values():
        today = date.today()
        days_ago = today - timedelta(days=40)
        today_formatted = today.strftime("%d-%b-%Y")
        days_ago_formatted = days_ago.strftime("%d-%b-%Y")
        req = requests.get(
            f"https://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity=23&Tx_State=MH&Tx_District=14&Tx_Market=172&DateFrom={days_ago_formatted}&DateTo={today_formatted}&Fr_Date={days_ago_formatted}&To_Date={today_formatted}&Tx_Trend=0&Tx_CommodityHead=Onion&Tx_StateHead=Maharashtra&Tx_DistrictHead=Pune&Tx_MarketHead=Pune")
        soup = BeautifulSoup(req.content, "html.parser")
        scrapped_text = soup.get_text()
        scrapped_text = scrapped_text.split("\n")
        scrapped_text = [item for item in scrapped_text if item != '' and len(item) <= 7]

        faq = [index for index, item in enumerate(scrapped_text) if item == 'FAQ']
        modal_prices = []
        for i in range(len(faq)):
            modal_prices.append(scrapped_text[faq[i] + 3])
        modal_prices = modal_prices[1:]
        modal_prices = modal_prices[::-1]
        while (len(modal_prices) != 20):
            modal_prices.pop(0)
        for i in range(len(modal_prices)):
            modal_prices[i] = float(modal_prices[i]) / 100
        return modal_prices

    mod = load_model('onion_lstm_model.h5')
    sc = joblib.load('onion_scaler.pkl')
    news = scrape_headlines_with_onion_only()
    X = scrap_values()
    X = np.asarray(X)
    df_for_training = X.astype(float)
    n_rows = len(df_for_training)
    df_for_training = df_for_training.reshape(n_rows, -1)
    scaler = sc
    scaler = scaler.fit(df_for_training)
    df_for_training_scaled = scaler.transform(df_for_training)
    trainX = []
    trainY = []

    n_future = 1  # Number of days we want to look into the future based on the past days.
    n_past = 14  # Number of past days we want to use to predict the future.
    n_days_for_prediction = 6
    for i in range(n_past, len(df_for_training_scaled) - n_future + 1):
        trainX.append(df_for_training_scaled[i - n_past:i, 0:df_for_training.shape[1]])
        trainY.append(df_for_training_scaled[i + n_future - 1:i + n_future, 0])
    trainX, trainY = np.array(trainX), np.array(trainY)
    prediction = mod.predict(
        trainX[-n_days_for_prediction:])  # shape = (n, 1) where n is the n_days_for_prediction
    prediction_copies = np.repeat(prediction, 1, axis=-1)
    y_pred_future = sc.inverse_transform(prediction_copies)[:, 0]
    for i in range(0, int(next_days / n_days_for_prediction)):
        for j in range(0, 6):
            X = np.delete(X, 0)
        for j in range(len(y_pred_future)):
            X = np.append(X, y_pred_future[i])
        df_for_training = X.astype(float)
        n_rows = len(df_for_training)
        df_for_training = df_for_training.reshape(n_rows, -1)
        scaler = sc
        scaler = scaler.fit(df_for_training)
        df_for_training_scaled = scaler.transform(df_for_training)
        trainX = []
        trainY = []

        for i in range(n_past, len(df_for_training_scaled) - n_future + 1):
            trainX.append(df_for_training_scaled[i - n_past:i, 0:df_for_training.shape[1]])
            trainY.append(df_for_training_scaled[i + n_future - 1:i + n_future, 0])
        trainX, trainY = np.array(trainX), np.array(trainY)
        prediction = mod.predict(
            trainX[-n_days_for_prediction:])  # shape = (n, 1) where n is the n_days_for_prediction
        prediction_copies = np.repeat(prediction, 1, axis=-1)
        y_pred_future = np.append(y_pred_future, sc.inverse_transform(prediction_copies)[:, 0])
    sentiment = scrap_headlines_and_analyse_sentiment(news)
    sa_score = 0
    if sentiment == "Negative":
      sa_score = -1
    elif sentiment == "Neutral":
      sa_score = 0
    elif sentiment == "Positive":
      sa_score = 1
    input_values = []
    final_vals = []
    lr_model = joblib.load("/content/Linear_Reg_for_SA.pkl")
    print(y_pred_future)
    bias = -20
    if len(y_pred_future)>=60:
      for j in range(0,60):
        x = [sa_score,y_pred_future[j]]
        x = np.asarray(x)
        x = x.reshape(1,-1)
        prediction = lr_model.predict(x)
        final_vals.append(prediction[0])
      for j in range(60,len(y_pred_future)):
        x = [0,y_pred_future[j]]
        x = np.asarray(x)
        x = x.reshape(1,-1)
        prediction = lr_model.predict(x)
        final_vals.append(prediction[0]) 
    elif len(y_pred_future)<60:
      for j in range(len(y_pred_future)):
        x = [sa_score,y_pred_future[j]]
        x = np.asarray(x)
        x = x.reshape(1,-1)
        prediction = lr_model.predict(x)
        final_vals.append(prediction[0])
    for i in range(len(final_vals)):
      final_vals[i]+=bias
    while(len(final_vals)!=next_days):
      final_vals.pop(len(final_vals)-1)
    # print("lebn",len(final_vals))
    # print(final_vals)
    # map_findings(final_vals)
    # st.write("Length of prediction array:", len(final_vals))
    st.write("Predicted prices:")
    for i in range(len(final_vals)):
      st.write(final_vals[i])
    # map_findings(y_pred_future)
    # return final_vals
    st.success("Prediction Successful!")
    st.subheader("Predicted Prices:")
    min_price = min(final_vals)
    max_price = max(final_vals)
    y_min = min(final_vals)
    y_max = max(final_vals)
    days = []
    for i in range(0,next_days):
      days.append(i+1)
    df = pd.DataFrame({'Values': final_vals,'Next Days':days})
# Display the bar chart
    
    fig, ax = plt.subplots()
    ax.bar(df['Next Days'], df['Values'])
    ax.set_xlabel('Next Days')
    ax.set_ylabel('Prices')
    ax.set_title('Prices for Next Days')

    # Displaying plot in Streamlit
    st.pyplot(fig)
    # st.bar_chart(df, use_container_width=False)

# Set the range for the y-axis
    # st.line_chart(final_vals, use_container_width=False, ylim=(y_min, y_max))
    st.write(f"Minimum Price: {min_price:.2f}")
    st.write(f"Maximum Price: {max_price:.2f}")
def calculate_additional_costs(q,d):
  bags = q/50  
  no_of_vehicles = 0
  if bags%70==0:
    no_of_vehicles = (bags/70)
  else:
    no_of_vehicles = int(bags/70)+1
  transportation_cost = d*27*no_of_vehicles
  labour_fee = q*0.5
  addmission_fee = 350*no_of_vehicles
  st.write(f"Total number of tempos required: {no_of_vehicles}")
  st.write(f"The total transportation cost will be: ₹ {transportation_cost}")
  st.write("+")
  st.write(f"The total labour cost will be: ₹ {labour_fee}")
  st.write("+")
  st.write(f"The total addmission cost to APMC market will be: ₹ {addmission_fee}")
  st.write("-------------------------------------------------------------------")
  st.write(f"The Net cost is: ₹ {(addmission_fee+transportation_cost+labour_fee)}")

page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
background-image: url("https://images.unsplash.com/photo-1566373655527-94386d8a5d5a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
background-size: cover;
}
</style>
"""
st.markdown(page_bg_img,unsafe_allow_html = True)
st.title('Onion Price Prediction')
quantity = st.number_input('Enter the amount in kgs: ', min_value=1, step=1, value=100)
distance = st.number_input('Enter the approx distance to the APMC Market: ', min_value=1, step=1, value=10)
next_days = st.number_input('Enter the number of days for prediction', min_value=1, step=1, value=8)

if st.button('Predict'):
    lstm_predictions(next_days)
if st.button('Check Net Cost for APMC Market'):
    calculate_additional_costs(quantity,distance)
if st.button('Latest Onion News'):
    scrape_headlines_with_onion_only_for_display()

# st.markdown(
#     """
#     <style>
#     body {
#         background-image: url('https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pexels.com%2Fsearch%2Fcrop%2F&psig=AOvVaw1cZJnIpGbBaZcQ57RrX157&ust=1714552214766000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCOjexfHC6YUDFQAAAAAdAAAAABAT');
#         background-size: cover;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )