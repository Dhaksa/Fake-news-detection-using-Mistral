import streamlit as st
from fake_news_detector import check_fake_news

st.set_page_config(page_title="🧠 Fake News Detector", layout="centered")
st.title("Fake News Detection ")
st.write("Analyze any news article or paragraph to detect if it may be fake or misleading.")

article_input = st.text_area("📰 Paste the news article or paragraph here:", height=300)

if st.button("🔍 Analyze"):
    if article_input.strip() == "":
        st.warning("Please paste a news article or text to analyze.")
    else:
        with st.spinner("Analyzing with Ollama..."):
            result = check_fake_news(article_input)

        score = result.get("credibility_score", 50)
        explanation = result.get("explanation", "No explanation available.")

        st.metric("🧾 Credibility Score", f"{score} / 100")
        
        if score >= 85:
            st.success("✅ This article appears highly credible.")
        elif score >= 60:
            st.warning("⚠️ This article may have some bias or issues.")
        else:
            st.error("❌ This article is likely not credible or may be fake.")

        st.markdown("**📝 Explanation:**")
        st.write(explanation)
