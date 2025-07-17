# 📱 Social Media Followers Prediction

This project predicts the **future follower count** of a social media account based on engagement metrics and clusters the account into influencer categories such as *Micro, Mid-tier, or Celebrity*. It combines **Regression**, **Clustering**, and **Streamlit-based Web App Deployment** for interactive user predictions.

---

## 🚀 Project Overview

With the rise of influencer marketing, understanding audience growth has become vital. This project leverages machine learning techniques to:
- Predict the number of followers an influencer might have in the future.
- Cluster users based on engagement and post activity.
- Provide personalized predictions via a user-friendly web app.

---

## 📊 Features
- Predict future followers using **Random Forest Regressor**.
- Cluster influencers using **KMeans Clustering**.
- Calculate **60-day engagement rate** from user input.
- Deploy model using **Streamlit** for public use.
- Visualize trends using **Bar chart**, **Pie chart**, **Treemap**, **Histogram**, and **Heatmap**.

---

## 🧠 Algorithms Used
- **Random Forest Regressor** – for predicting followers.
- **KMeans Clustering** – for categorizing user into types.
- **StandardScaler** – for scaling data before training and clustering.

---

## 🗃️ Dataset
- **Source**: Kaggle (Top Instagram Influencers dataset)
- **Rows**: ~200 entries
- **Columns**: Includes name, followers, average likes, engagement rate, category, country, etc.
- Custom synthetic data was also generated for better training and testing.

---

## 🛠️ Libraries & Technologies
- `pandas`, `numpy` – Data manipulation
- `scikit-learn` – Machine Learning models and preprocessing
- `matplotlib`, `seaborn`, `plotly` – Visualization
- `Streamlit` – App deployment
- `pickle` – Model serialization

---

## 📈 Visualizations Included
- **Bar Chart** – Top countries
- **Pie Chart** – Top 5 content categories
- **Histogram** – Followers distribution
- **Heatmap** – Feature correlation
- **Treemap** – Followers by category and country

---

## 🖥️ How to Run the Project

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/social-media-followers-prediction.git
   cd social-media-followers-prediction
   
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   
3. Run the Streamlit app:
   ```bash
   streamlit run streamlit_app.py

4. Upload your follower stats and get predictions in real-time!


---

## 📁 Project Structure

```bash
├── streamlit_app.py                # Streamlit frontend
├── model_training.py               # ML model training code
├── regression_model.pkl            # Saved regression model
├── kmeans_model.pkl                # Saved clustering model
├── scaler.pkl                      # Scaler used during training
├── dataset/                        # Contains original dataset
├── visuals/                        # Screenshots or plot exports
├── README.md                       # Project documentation
└── requirements.txt                # Python dependencies
```
---

## 📌 Future Enhancements

1. Integrate time series forecasting (e.g., ARIMA, Prophet) for monthly/yearly growth predictions.
2. Expand dataset using web scraping or APIs.
3. Improve UI with custom designs and animations.
4. Allow login and profile analytics for multiple users.
---

## 🙋‍♀️ Author
Ruthika Nalajala
AI & Machine Learning Enthusiast | Final Year Engineering Student<br>
🔗 Linkedin: https://www.linkedin.com/in/ruthika-nalajala-73127628b/ <br> 💻 Github: https://github.com/ruthikan

---
## ⭐ Acknowledgements
- Special thanks to Blackbucks Internship Program and Streamlit Community Cloud.
- Dataset courtesy: Kaggle - top_insta_influencers_data.




