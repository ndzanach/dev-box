import streamlit as st
import requests


st.set_page_config(page_title="API Tools", layout="centered")

apps = [
    {
        "name": "Http Request",
        "description": "Test your endpoints.",
        "icon": "🎙️",
        "endpoint": "http://api:8000/api/hello_get",
        "type": "message",
    },
]
# --- Part 1: Sidebar Buttons (UI triggers only) ---
st.sidebar.title("🚀 API Tools")

if "active_tool" not in st.session_state:
    st.session_state.active_tool = None

for app in apps:
    if st.sidebar.button(f"{app['icon']} {app['name']}", key=app["name"]):
        st.session_state.active_tool = app["name"]

for app in apps:
    if st.session_state.active_tool == app["name"]:
        st.markdown(f"## {app['icon']} {app['name']}")
        st.caption(app["description"])

        if app["type"] == "message":
            if st.button(f"Get {app['name']}", key=f"btn_get_{app['name']}"):
                with st.spinner("Calling API..."):
                    try:
                        res = requests.get(
                            "http://api:8000/api/hello_get"
                        )
                        if res.ok:
                            result = res.json()
                            st.toast("✅ Request complete!")
                            st.text_area(
                                "📋 Response body",
                                value=result['response'],
                                height=100,
                            )
                        else:
                            st.error(f"❌ Error: {res.status_code} - {res.text}")
                    except Exception as e:
                        st.error(f"⚠️ Request failed: {e}")
                            
            user_input = st.text_input(
                f"Enter Your Message for {app['name']}", key=f"url_{app['name']}"
            )  
            if st.button(f"POST {app['name']}", key=f"btn_post_{app['name']}"):
                if not user_input.strip():
                    st.warning("⚠️ Please enter a valid YouTube URL.")
                else:
                    with st.spinner("Calling API..."):
                        try:
                            res = requests.post(
                                "http://api:8000/api/hello_post", json={"message": user_input.strip()}
                            )
                            if res.ok:
                                result = res.json()["data"]
                                full_text = f"📺 Message: {result['message']}\n\n📝 Subject: {result['subject']}"
                                result = res.json()
                                st.toast("✅ Request complete!")
                                st.text_area(
                                    "📋 Response body",
                                    value=full_text,
                                    height=150,
                                )
                            else:
                                st.error(f"❌ Error: {res.status_code} - {res.text}")
                        except Exception as e:
                            st.error(f"⚠️ Request failed: {e}")
        st.divider()
