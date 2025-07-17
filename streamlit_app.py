import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt

# Load models
follower_model = pickle.load(open('regression_model.pkl', 'rb'))
likes_model = pickle.load(open('likes_model.pkl', 'rb')) 
scaler = pickle.load(open('scaler.pkl', 'rb'))
kmeans = pickle.load(open('kmeans_model.pkl', 'rb'))

# Title and Description
st.title("📱 Social Media Growth Predictor")
st.markdown("""
Welcome! This app predicts your **future followers** and **likes**, and clusters your influencer type based on your activity and engagement.

👇 Please enter your social media stats to get started.
""")

# User Inputs
st.header("🔢 Enter Your Social Media Stats")
avg_likes = st.number_input("1️⃣ Average likes per post", step=1, min_value=0)
new_post_avg_like = st.number_input("2️⃣ Average likes on recent posts", step=1, min_value=0)
posts = st.number_input("3️⃣ Total number of posts", step=1, min_value=1)

st.subheader("📈 Engagement Rate Estimation")
total_engagements = st.number_input("4️⃣ Total likes + comments in the last 60 days", step=1, min_value=0)
followers_60 = st.number_input("5️⃣ Current number of followers", step=1, min_value=1)
posts_60 = st.number_input("6️⃣ Number of posts in last 60 days", step=1, min_value=1)

# Calculate 60-Day Engagement Rate
if followers_60 > 0 and posts_60 > 0:
    eng_rate = (total_engagements / (followers_60 * posts_60)) * 100
    st.success(f"📊 Estimated 60-Day Engagement Rate: {eng_rate:.2f}%")
else:
    eng_rate = 0

# Prediction Trigger
# 📆 User selects how many years ahead they want to predict
st.subheader("📅 Select Prediction Range (Years)")
years = st.slider("Predict followers after how many years?", min_value=1, max_value=5, value=3)

# Prediction button
if st.button("🚀 Predict Followers, Likes & Cluster"):
    input_data = pd.DataFrame([[avg_likes, new_post_avg_like, posts, eng_rate]],
                              columns=['avg_likes', 'new_post_avg_like', 'posts', '60_day_eng_rate'])

    # Predict followers and likes using respective models
    predicted_followers = follower_model.predict(input_data)[0]
    predicted_likes = likes_model.predict(input_data)[0]

    # Scale predictions proportionally to selected year 
    scaled_followers = int((predicted_followers / 10) * years)
    scaled_likes = int((predicted_likes / 10) * years)

    max_reasonable_followers = followers_60 * (2 * years)  # dynamic cap
    final_followers = min(scaled_followers, max_reasonable_followers)

    max_reasonable_likes = int((followers_60 * (eng_rate / 100)) * years)
    final_likes = min(scaled_likes, max_reasonable_likes)


    # Clustering
    input_scaled = scaler.transform(input_data)
    cluster_label = kmeans.predict(input_scaled)[0]

    # Cluster label mapping
    label_map = {0: 'Micro Influencer', 1: 'Mid-tier', 2: 'Celebrity'}
    cluster_name = label_map.get(cluster_label, f"Group {cluster_label}")

    # Display results
    st.subheader("📊 Prediction Result")
    st.success(f"📈 Estimated Followers After {years} Year(s): {final_followers:,}")
    st.success(f"💖 Estimated Likes After {years} Year(s): {final_likes:,}")
    st.info(f"Influencer Category: {cluster_name}")

    st.warning("""
📌 **Note:** Your predicted followers and likes are based on your current statistics such as engagement, post activity, and follower count.  
However, social media growth also heavily depends on **content quality**, **consistency**, and **creativity**.

📣 If you're aiming for better growth, consider improving your content style, using trending formats, and engaging actively with your audience!
""")

    # Recommendations
    st.subheader("📌 Personalized Recommendations")

    if cluster_name == 'Micro Influencer':
        st.markdown("""
    - 📸 **Post more frequently** to increase visibility.
    - 💬 **Engage more with your audience** through replies and comments.
    - 🎯 Try **targeted content strategies** to boost engagement.
    - 📈 Focus on **growing authentic followers** through niche value.
    """)
    elif cluster_name == 'Mid-tier':
        st.markdown("""
    - 🤝 **Collaborate with other creators or brands** to expand your reach.
    - 📊 Analyze your top-performing content and **replicate that style**.
    - 🎥 Try experimenting with **new formats (Reels, Stories)**.
    - ⏱️ Maintain **consistent posting schedules**.
    """)
    elif cluster_name == 'Celebrity':
        st.markdown("""
    - 🔄 Continue **high-quality content delivery** to retain your audience.
    - 🌐 Consider expanding to **other platforms** for wider reach.
    - 💡 Invest in **personal branding and storytelling**.
    - 🧠 Use data insights to **understand what your audience loves most**.
    """)
    else:
        st.markdown("📋 Unable to generate recommendations for this category.")


    # Visual Summary
    user_data = {
        'Average Likes': avg_likes,
        'Recent Post Likes': new_post_avg_like,
        'Total Posts': posts,
        '60-Day Engagements': total_engagements,
        'Followers': followers_60,
        'Posts in 60 Days': posts_60
    }

    st.subheader("📊 Your Input Summary")
    st.bar_chart(pd.DataFrame.from_dict(user_data, orient='index', columns=['Values']))
