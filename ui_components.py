import streamlit as st

def setup_page():
    """Sets up the webpage title and layout."""
    st.set_page_config(page_title="NEXUS 6.0", page_icon="🏭", layout="wide")
    st.title("🏭 NEXUS 6.0: Smart Factory Copilot")
    st.caption("Industry 6.0 • Human-AI Collaboration Workspace")
    st.divider()

def render_sidebar():
    """Creates the sidebar switch to trigger simulated failure."""
    with st.sidebar:
        st.header("🕹️ Demo Control Panel")
        st.info("Use this toggle during the presentation to trigger an alert.")
        simulate_failure = st.toggle("🚨 Inject Machine 03 Anomaly", value=False)
        return simulate_failure

def render_machine_grid(machine_states):
    """Displays 4 machine status boxes at the top of the dashboard."""
    st.subheader("Factory Floor Status")
    col1, col2, col3, col4 = st.columns(4)
    
    cols = [col1, col2, col3, col4]
    for idx, (name, data) in enumerate(machine_states.items()):
        with cols[idx]:
            if data["status"] == "CRITICAL":
                st.error(f"### {name}\n🔴 CRITICAL\nScore: {data['score']}%")
            else:
                st.success(f"### {name}\n🟢 NORMAL\nScore: {data['score']}%")

def render_copilot_panel(m3_data, ai_text, is_anomaly):
    """Displays live temperature metrics on the left, and AI advice on the right."""
    st.divider()
    left_col, right_col = st.columns(2)
    
    # Left Box: Live Numbers
    with left_col:
        st.subheader("📊 Live Telemetry (Machine 03)")
        st.metric(label="Temperature", value=f"{m3_data['temp']} °C")
        st.metric(label="Vibration Level", value=f"{m3_data['vib']} Hz")
        st.metric(label="Pressure", value=f"{m3_data['press']} PSI")

    # Right Box: AI Recommendation & Buttons
    with right_col:
        st.subheader("🤖 AI Copilot Diagnostics")
        if is_anomaly:
            st.error(ai_text)
            st.write("---")
            st.markdown("**Operator Decision Required:**")
            
            b1, b2 = st.columns(2)
            if b1.button("✅ Approve Inspection", type="primary"):
                st.success("Action Recorded: Machine 03 powered down for safety inspection.")
            if b2.button("❌ Reject Alert"):
                st.info("Action Recorded: Alert dismissed by operator.")
        else:
            st.success(ai_text)

def render_learning_card(is_anomaly):
    """Displays a short learning module at the bottom when an alert happens."""
    if is_anomaly:
        st.divider()
        st.subheader("🧠 Operator Micro-Learning")
        with st.expander("🎓 30-Second Lesson: Why did vibration spike?", expanded=True):
            st.write("A spike in vibration along with rising temperature usually indicates motor bearing friction.")
            st.radio("Quick Check: What causes high friction?", ["Worn out bearings", "Slow internet"])
            if st.button("Submit Answer"):
                st.balloons()