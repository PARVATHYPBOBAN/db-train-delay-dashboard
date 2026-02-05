import os
import pandas as pd
import streamlit as st

st.set_page_config(page_title="DB Train Delay Dashboard", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("DBtrainrides_1000.csv")

df = load_data()

st.title("🚆 Deutsche Bahn Train Delay Analysis")

pages = ["Overview"] + [f"Q{i:02d}" for i in range(1, 16)]
page = st.sidebar.radio("Navigation", pages)

questions = {
    "Q01": "What percentage of train stops experience an arrival delay?",
    "Q02": "Which stations have the highest average arrival delay?",
    "Q03": "At what time of day do arrival delays occur most often?",
    "Q04": "How do arrival delays vary across station categories?",
    "Q05": "Do longer arrival delays tend to occur at certain times of the day?",
    "Q06": "How does the arrival delay rate differ between large and small stations?",
    "Q07": "How does the average arrival delay differ by train line?",
    "Q08": "Which train lines have the highest percentage of delayed arrivals?",
    "Q09": "How does the average arrival delay change by hour of the day?",
    "Q10": "How does the average arrival delay vary by day of the week?",
    "Q11": "How does the average arrival delay vary by month?",
    "Q12": "How does the average arrival delay differ between peak and off-peak hours?",
    "Q13": "Is there a relationship between planned arrival time and arrival delay?",
    "Q14": "What proportion of trains are on-time vs delayed?",
    "Q15": "How does the arrival delay distribution look overall?"
}

results = {
    "Q01": [
        "Around 30% of train stops experienced an arrival delay.",
        "That is nearly 1 in 3 trains arriving late."
    ],
    "Q02": [
        "A few stations show much higher average delays than others.",
        "Likely reasons: high traffic, operational complexity, or frequent disruptions."
    ],
    "Q03": [
        "Delays are more common during morning and late-afternoon peak hours.",
        "Late-night and early-morning periods have fewer delays."
    ],
    "Q04": [
        "Delays increase as station size decreases.",
        "Smaller and mid-sized stations have more delayed arrivals than major stations."
    ],
    "Q05": [
        "Longer delays occur during daytime and early evening.",
        "Late-night and early morning show shorter average delays."
    ],
    "Q06": [
        "Smaller stations have a higher percentage of delayed arrivals.",
        "Larger stations handle arrivals more reliably."
    ],
    "Q07": [
        "Some train lines have much higher average delays than others.",
        "These routes can be prioritized to improve scheduling and reduce delays."
    ],
    "Q08": [
        "A few train lines show consistently higher delay rates.",
        "These routes are less reliable and should be prioritized for improvement."
    ],
    "Q09": [
        "Average delay severity varies across different hours of the day.",
        "Busier periods have higher delays; quieter hours run more smoothly."
    ],
    "Q10": [
        "Average arrival delays are higher on weekdays than on weekends.",
        "Weekends generally run more smoothly with fewer delays."
    ],
    "Q11": [
        "The data covers only one month (July), so analysis is only for this period.",
        "Seasonal patterns need multiple months of data."
    ],
    "Q12": [
        "Average delays are higher during peak hours.",
        "Off-peak hours run more smoothly with fewer delays."
    ],
    "Q13": [
        "Delays occur at all arrival times with no strong linear pattern.",
        "Higher delays cluster during busy daytime/evening hours."
    ],
    "Q14": [
        "About 70% of trains arrive on time or early; around 30% are delayed.",
        "Most delays are short; severe delays are relatively rare."
    ],
    "Q15": [
        "Most arrival delays are small (typical delays are minor).",
        "A few large outliers show that major delays happen occasionally."
    ]
}
plot_files = {
    "Q01": "Q01_arrival_delay_distribution.png",
    "Q02": "Q02_avg_delay_by_station.png",
    "Q03": "Q03_hourly_arrival_delays.png",
    "Q04": "Q04_delays_by_station_category.png",
    "Q05": "Q05_avg_delay_by_hour.png",
    "Q06": "Q06_delay_rate_by_station_category.png",
    "Q07": "Q07_avg_delay_by_line.png",
    "Q08": "Q08_delay_rate_by_line.png",
    "Q09": "Q09_avg_delay_by_hour.png",
    "Q10": "Q10_avg_delay_by_weekday.png",
    "Q11": "Q11_avg_delay_by_month.png",
    "Q12": "Q12_avg_delay_peak_vs_offpeak.png",
    "Q13": "Q13_delay_vs_arrival_time.png",
    "Q14": "Q14_delay_histogram_red.png",
    "Q15": "Q15_arrival_delay_distribution_line.png"
}

def show_plot(qid):
    if qid in plot_files:
        path = os.path.join("Figs", plot_files[qid])
        if os.path.exists(path):
            st.image(path, use_container_width=True)
        else:
            st.warning("Plot file not found in Figs folder.")
    else:
        st.info("No plot mapped for this question yet.")

if page == "Overview":
    st.subheader("Dataset Overview")
    st.write("This dashboard presents an analysis of Deutsche Bahn train arrival delays.")
    st.write(f"Total records: {len(df)}")

    preview = df.head().copy()
    preview = preview.fillna("—")
    st.dataframe(preview)

else:
    st.subheader(page)
    st.markdown(f"**Question:** {questions[page]}")

    st.markdown("### Plot")
    show_plot(page)

    st.markdown("### Result")
    for line in results[page]:
        st.write(f"• {line}")

