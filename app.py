import streamlit as st
import requests
import random
from datetime import date

st.set_page_config(page_title="This Day in History", page_icon="📜")

st.title("📜 This Day in History")
st.subheader("Pick any day and explore history")
st.markdown("### 🎂 Made with love for Anjana ❤️")

# Default date → Feb 21 (birthday)
default_date = date(2026, 2, 21)

selected_date = st.date_input(
    "📅 Choose a day",
    default_date,
    format="DD/MM/YYYY"
)

month = selected_date.month
day = selected_date.day

# Special birthday message
if month == 2 and day == 21:
    st.markdown("## 🎉Happy Birthday from your brother!! ")
    st.success("🎂 Birthday of Anjana — 21st February 2007")
    
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("images/anjana2.jpg", caption="Anjana 💖")

    with col2:
        st.image("images/anjana1.jpg", caption="Birthday Queen 👑")

    with col3:
        st.image("images/anjana3.jpg", caption="World Explorer 🌍")


url = f"https://history.muffinlabs.com/date/{month}/{day}"

if month == 9 and day == 4:
    st.markdown("## 🎉Happy Birthday from your brother!! ")
    st.success("🎂 Birthday of Chikkumanee — 04th September 2013")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.image("images/chikku1.jpg", caption="Attitudee 😎😏")

    with col2:
        st.image("images/chikku2.jpg", caption="mmm..yummyy..👌😹")

    with col3:
        st.image("images/chikku3.jpg", caption="angryyy😡🥵")

url = f"https://history.muffinlabs.com/date/{month}/{day}"

if month == 12 and day == 1:
    st.markdown("## 🎉Happy Birthday Mammoojjii ")
    st.success("🎂 Birthday of Mammoojjii — 1st Decemeber 1987")
    
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("images/mom1.jpg", caption="with chikkumaneei")

    with col2:
        st.image("images/mom2.jpg", caption="again manee!!😹 ")

    with col3:
        st.image("images/mom3.jpg", caption="together without mee!!🥲")

url = f"https://history.muffinlabs.com/date/{month}/{day}"

if month == 6 and day == 4:
    st.markdown("## 🎉Happy Birthday from Myself ")
    st.success("🎂 Birthday of Mee — 04th June 2011")
        
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("images/me1.jpg", caption="styleeii!!🕶🙈")

    with col2:
        st.image("images/me2.jpg", caption="mudi vettatee.! ✂🪮 ")

    with col3:
        st.image("images/me3.jpg", caption="Posingg..✌🤞")


url = f"https://history.muffinlabs.com/date/{month}/{day}"


try:
    response = requests.get(url, timeout=10)
    data = response.json()

    events = data["data"]["Events"]

    st.write(f"## 🗓️ {selected_date.strftime('%B %d')}")

    selected = random.sample(events, min(5, len(events)))

    for event in selected:
        st.markdown("---")
        st.write(f"### {event['year']}")
        st.write(event["text"])

except:
    st.error("Internet problem or API not responding. Please try again later.")
