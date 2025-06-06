import streamlit as st

st.set_page_config(page_title="Conflict Style Adventure", page_icon="🧭")

# Session state initialization
if "step" not in st.session_state:
    st.session_state.step = "intro"

st.title("🧭 Conflict Style Adventure")
st.markdown("### A leadership and teamwork simulation")
st.write(
    "You're preparing a high-stakes team presentation. You believe your idea is the best, "
    "but your teammate Jordan strongly disagrees. The deadline is near, and tension is rising. "
    "What do you do?"
)

# === Decision Logic ===

def reset():
    st.session_state.step = "intro"

def next_step(choice):
    st.session_state.step = choice

# === Step Router ===

def show_intro():
    if st.button("A. Push your idea forward (Competing)"):
        next_step("competing")
    if st.button("B. Delay the conversation (Avoiding)"):
        next_step("avoiding")
    if st.button("C. Let Jordan lead (Accommodating)"):
        next_step("accommodating")
    if st.button("D. Explore both ideas (Collaborating)"):
        next_step("collaborating")
    if st.button("E. Suggest a blended idea (Compromising)"):
        next_step("compromising")

def show_competing():
    st.subheader("🔥 You chose Competing.")
    st.write("Jordan looks frustrated. The team is tense. What do you do?")
    if st.button("A1. Double down"):
        st.warning("🔻 You win the idea but lose Jordan's trust. The team morale drops.")
    elif st.button("A2. Pause and hear Jordan out"):
        next_step("d1")
    elif st.button("A3. Ask your manager to decide"):
        st.info("😐 The manager decides, but you seem unable to resolve conflicts yourself.")
    elif st.button("A4. Apologize and shift to collaboration"):
        st.success("👏 You regain trust and build a stronger solution with Jordan.")

def show_avoiding():
    st.subheader("😶 You chose Avoiding.")
    st.write("You delay the conversation as the deadline approaches.")
    if st.button("B1. Leave it unresolved"):
        st.error("⚠️ The issue festers. The final product suffers.")
    elif st.button("B2. Let Jordan take over"):
        st.warning("😞 You’re sidelined, and your expertise is missed.")
    elif st.button("B3. Quietly make your own version"):
        st.error("❌ Last-minute confusion causes chaos.")

def show_accommodating():
    st.subheader("🤐 You chose Accommodating.")
    st.write("You let Jordan lead to avoid tension.")
    if st.button("C1. Say nothing"):
        st.warning("😬 The project struggles. You feel regret.")
    elif st.button("C2. Support Jordan’s plan"):
        st.info("🙂 Peace is preserved, but you feel overlooked.")
    elif st.button("C3. Speak up later"):
        st.success("💡 You address things constructively post-project.")

def show_collaborating():
    st.subheader("🤝 You chose Collaborating.")
    st.write("You suggest exploring both ideas thoroughly.")
    if st.button("D1. Find a third, stronger solution"):
        st.success("🎯 You and Jordan combine ideas and create something better together.")
    elif st.button("D2. Spend too long discussing"):
        st.warning("⏳ Great ideas, but missed the deadline.")
    elif st.button("D3. Discover deeper team issues"):
        st.info("🔍 You resolve deeper team tensions, strengthening long-term trust.")

def show_compromising():
    st.subheader("⚖️ You chose Compromising.")
    st.write("You offer a blended solution to move forward.")
    if st.button("E1. Accept a clunky combo"):
        st.warning("😐 The presentation is fine but unremarkable.")
    elif st.button("E2. Adjust slightly and align"):
        st.success("👍 Respect maintained, good enough result.")
    elif st.button("E3. Agree but feel disappointed"):
        st.error("😕 Outward agreement, inner frustration.")

def show_d1():
    st.subheader("✅ Outcome: Collaborating Win")
    st.success("You and Jordan combine the best of both ideas. Team morale is high. The project shines.")
    st.button("🔁 Restart", on_click=reset)

# === Page Routing ===

if st.session_state.step == "intro":
    show_intro()
elif st.session_state.step == "competing":
    show_competing()
elif st.session_state.step == "avoiding":
    show_avoiding()
elif st.session_state.step == "accommodating":
    show_accommodating()
elif st.session_state.step == "collaborating":
    show_collaborating()
elif st.session_state.step == "compromising":
    show_compromising()
elif st.session_state.step == "d1":
    show_d1()

# === Footer ===
st.markdown("---")
st.button("🔁 Restart Adventure", on_click=reset)
