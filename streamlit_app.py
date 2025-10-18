import streamlit as st

# Define your 3 pages
pages = [
    st.Page("pages/indoor_nav.py", title="Indoor Map", icon="🗺️"),
    st.Page("pages/chat.py", title="Chat", icon="💬"),
    st.Page("pages/notices.py", title="Notices", icon="📋"),
    st.Page("pages/test_credentials.py", title="Test Creds", icon="🔐"),
]

# Create navigation
pg = st.navigation(pages, position="sidebar")
pg.run()
