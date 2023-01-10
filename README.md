# Crypto_Prediction
The main objective of our project is to predict the price range of top 5 crypto currencies. We have analyzed the dataset and performed several EDA operations on it like Candlestick, Trend Plots.

We have made 5 different notebooks for each crytocurrency

### Brief Description
***
Here is a breif description of how I trained my dataset :
*  Import the required libraries and dataset
*  Perform some basic data pre-processing and visualize the data
*  Check for null values
*  Plot Candlesticks
*  Plot Histogram
*  Plot Moving Average
*  Monthwise record of the data
*  Plot the monthwise data
*  Split the model into train and test model using sklearn.model_selection
*  Feature scaling of the model – MinMaxScalar (sklearn.preprocessing)
*   Build the model – LSTM
*  Fit the model
*  Predict the values
*  Visualize the predicted values


There are various types of neural network architectures. Depending on our task, the data we have at hand and the output we want to generate, we can choose or create different network architectures and design patterns. If our dataset contains images or pixels, then a Convolutional Neural Networks could be what you need. If we are trying to train a network on a sequence of inputs, then a Recurrent Neural Networks (RNN) might work. 
RNNs are a kind of artificial neural network that achives really good results when your goal is to recognize patterns in sequences of data. And when working with text data any model that calculates the probability of the next character given the previous character is called a language model 1
RNNs are very useful if our input is, for example, a corpus of text or a musical composition and we are trying to predict meaningful sequences out of it. Long Short-Term Memory networks, or LSTMs, are just a special type of RNN that can perform better when learning about “long-term dependencies".
We have used LSTM to train our model
We have also tried to predict the values using RandomForestTree.RandomForestTree returns doesn't return great accuracy like LSTM for our dataset.So we have chosen LSTM as our base for training the model

### Prediction Model
![image](https://user-images.githubusercontent.com/73640313/211518795-ab0fa419-daba-4f3d-9828-b491abe23e9a.png)

### Prediction Output
![image](https://user-images.githubusercontent.com/73640313/211518871-c0248be1-29a3-479f-be1b-716ba30510c1.png)

### Exploratory Data Analysis of prediction of Top 5 CryptoCurrencies
[Crypto CURRENCY PRICE PREDICTION.pdf](https://github.com/adithya-vedhamani/Crypto_Prediction/files/10381326/Crypto.CURRENCY.PRICE.PREDICTION.pdf)

### Demo Video of Exploratory Data Analysis of prediction of Top 5 CryptoCurrencies
https://user-images.githubusercontent.com/73640313/211520637-2312fdd1-1c14-496f-9faf-2645ff68e016.mp4

