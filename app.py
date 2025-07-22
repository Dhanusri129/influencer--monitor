import torch
import streamlit as st
from transformers import pipeline

st.title("📲 Influencer Monitoring for Brand Teams")
st.subheader("Track & Summarize Influencer Content")

query = st.text_input("Enter influencer handle or hashtag (e.g., @elonmusk or #AI)")

# Mocked sample posts
def fetch_mock_posts(query):
    return [
        f"{query} launched a new product with XYZ.",
        f"{query} shared a reel about AI content tools.",
        f"{query} attended a tech event in Mumbai.",
    ]

# Load summarizer
summarizer = pipeline("summarization",model="sshleifer/distilbart-cnn-12-6")

# Summarize fetched posts
def summarize(posts):
    full_text = " ".join(posts)
    if len(full_text) > 1024:
        full_text = full_text[:1024]
    return summarizer(full_text, max_length=100, min_length=30, do_sample=False)[0]['summary_text']

if st.button("Get Trend Summary"):
    if not query.strip():
        st.warning("Enter a valid handle or keyword.")
    else:
        with st.spinner("Fetching posts..."):
            posts = fetch_mock_posts(query)
            st.success("Posts Fetched:")
            for i, post in enumerate(posts, 1):
                st.markdown(f"**Post {i}:** {post}")
            summary = summarize(posts)
            st.markdown("### 🧠 AI Summary")
            st.info(summary)
