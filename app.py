import streamlit as st
import requests

# Initialize session state to hold the generated document bytes
if "docx_bytes" not in st.session_state:
    st.session_state.docx_bytes = None

st.title("Bedtime Story Generator")
st.write(
    "Choose from the options below or enter your own values to generate a personalized bedtime story."
)

with st.form(key="story_form"):
    # 1. Age Range
    age_options = ["3-5", "6-8", "9-12"]
    selected_age = st.selectbox("Age Range", age_options, index=0)
    custom_age = st.text_input(
        "Or enter a custom Age Range (e.g., 2-4, 13-15)"
    )
    age_value = custom_age.strip() if custom_age.strip() else selected_age

    # 2. Theme
    theme_options = ["adventure", "friendship", "magic", "space", "bedtime calming"]
    selected_theme = st.selectbox("Theme", theme_options, index=0)
    custom_theme = st.text_input("Or enter a custom Theme")
    theme_value = custom_theme.strip() if custom_theme.strip() else selected_theme

    # 3. Number of Pages
    # We map option labels to their numeric values
    pages_options = {"Short (5)": 5, "Medium (10)": 10, "Long (15)": 15}
    selected_pages_option = st.selectbox("Number of Pages", list(pages_options.keys()), index=1)
    custom_pages = st.text_input(
        "Or enter a custom number of pages", placeholder="e.g. 7"
    )
    if custom_pages.strip():
        try:
            pages_value = int(custom_pages.strip())
        except ValueError:
            st.error("Invalid custom number of pages. Using selected option.")
            pages_value = pages_options[selected_pages_option]
    else:
        pages_value = pages_options[selected_pages_option]

    # 4. Reading Time
    time_options = {"3 min": 3, "5 min": 5, "10 min": 10}
    selected_time_option = st.selectbox("Reading Time", list(time_options.keys()), index=1)
    custom_time = st.text_input(
        "Or enter a custom reading time (in minutes)", placeholder="e.g. 7"
    )
    if custom_time.strip():
        try:
            time_value = int(custom_time.strip())
        except ValueError:
            st.error("Invalid custom reading time. Using selected option.")
            time_value = time_options[selected_time_option]
    else:
        time_value = time_options[selected_time_option]

    # 5. Story Tone
    tone_options = ["fun", "calming", "inspiring", "silly"]
    selected_tone = st.selectbox("Story Tone", tone_options, index=0)
    custom_tone = st.text_input("Or enter a custom Story Tone")
    tone_value = custom_tone.strip() if custom_tone.strip() else selected_tone

    # 6. Setting
    setting_options = ["forest", "ocean", "outer space", "castle"]
    selected_setting = st.selectbox("Setting", setting_options, index=0)
    custom_setting = st.text_input("Or enter a custom Setting")
    setting_value = custom_setting.strip() if custom_setting.strip() else selected_setting

    # 7. Lesson or Moral (optional)
    moral_options = ["None", "kindness", "bravery", "sharing"]
    selected_moral = st.selectbox("Lesson or Moral (optional)", moral_options, index=0)
    custom_moral = st.text_input("Or enter a custom Moral/Lesson (leave blank for none)")
    if custom_moral.strip():
        moral_value = custom_moral.strip()
    elif selected_moral == "None":
        moral_value = ""
    else:
        moral_value = selected_moral

    # 8. Illustration Style
    illustration_options = ["cartoon", "watercolor", "sketch", "none"]
    selected_illustration = st.selectbox("Illustration Style", illustration_options, index=0)
    custom_illustration = st.text_input("Or enter a custom Illustration Style")
    illustration_value = custom_illustration.strip() if custom_illustration.strip() else selected_illustration

    submit_button = st.form_submit_button(label="Generate Story")

# When the form is submitted, build the payload and call the FastAPI endpoint
if submit_button:
    payload = {
        "Age": age_value,
        "Theme": theme_value,
        "Pages": pages_value,
        "Time": time_value,
        "Tone": tone_value,
        "Setting": setting_value,
        "Moral": moral_value,
        "IllustrationStyle": illustration_value,  # Ensure your FastAPI endpoint supports this parameter.
    }

    fastapi_url = "http://localhost:8000/generate-story"  # Update if your endpoint URL differs.

    try:
        with st.spinner("Generating your story, please wait..."):
            response = requests.post(fastapi_url, json=payload)

        if response.status_code == 200:
            st.session_state.docx_bytes = response.content
            st.success("Story generated successfully!")
        else:
            st.error(f"Error {response.status_code}: {response.text}")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# If a document was generated, show a download button
if st.session_state.docx_bytes is not None:
    st.download_button(
        label="Download Your Bedtime Story",
        data=st.session_state.docx_bytes,
        file_name="bedtime_story.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    )
