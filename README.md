# 🎬 Movie Recommender System

A content-based movie recommendation system built using **Python**, **Pandas**, and **Streamlit**.  
It suggests similar movies based on a selected title using cosine similarity on movie features.

## 📌 Features
- ✅ Recommend top 5 similar movies for any given movie title.
- ✅ Uses **content-based filtering** (based on genres, keywords, cast, crew).
- ✅ Interactive **Streamlit web app**.
- ✅ Preprocessed data for faster recommendations.

---

## 📂 Project Structure
├── movie_dict.pkl # Preprocessed movie dataset
├── similarity.pkl # Precomputed similarity matrix
├── app.py # Main Streamlit app
├── requirements.txt # Python dependencies
├── README.md # Project documentation


---

🛠 How It Works

1.Data Preprocessing
 Reads movie metadata and cleans it.
 Extracts important features like genres, keywords, cast, and crew.
 Creates a combined feature string for each movie.

2. Vectorization & Similarity
Converts text data into numerical vectors using CountVectorizer.
Computes similarity between movies using cosine similarity.

3. Recommendation Function
Finds the movie in the dataset.
Sorts other movies by similarity score.

****Returns the top 5 most similar movies****

🖼 Example

Input: Avatar

Output:
Guardians of the Galaxy
Star Trek
Star Wars: The Force Awakens
John Carter
The Avengers

📦 Requirements
Python 3.8+
pandas
numpy
scikit-learn
streamlit
pickle
