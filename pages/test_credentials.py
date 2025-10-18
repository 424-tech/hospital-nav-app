import streamlit as st

st.title("🔐 Credentials Test")

try:
    supabase_url = st.secrets["supabase"]["url"]
    supabase_key = st.secrets["supabase"]["key"]
    
    st.success("✅ Supabase URL found!")
    st.success("✅ Supabase key found!")
    st.info(f"**Supabase URL:** {supabase_url}")
    
    st.warning("⏳ Situm credentials pending - will add in Week 2")
    
except Exception as e:
    st.error(f"❌ Error loading credentials: {e}")
