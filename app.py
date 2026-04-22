import os
import streamlit as st
import pandas
import matplotlib
import seaborn

from langchain_groq import ChatGroq
from langchain_experimental.agents import create_pandas_dataframe_agent

# ---- PAGE CONFIG ----
st.set_page_config(page_title="MY_csv Agent", page_icon="🤖", layout="wide")

st.title("🤖 MY_csv Agent (Groq + LangChain)")

# ---- SIDEBAR ----
st.sidebar.header("⚙️ Configuration")

api_key = st.sidebar.text_input("1. Enter GROQ API Key", type="password")
uploaded_file = st.sidebar.file_uploader("2. Upload your CSV file", type=["csv"])
temperature = st.sidebar.slider("Model Temperature", 0.0, 1.0, 0.0)

st.sidebar.divider()
st.sidebar.info("This agent uses Llama-3.3-70b to analyze and visualize your data.")

# ---- MAIN CONTENT ----
if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)

        # Tabs MUST be inside this block
        tab1, tab2 = st.tabs(["💬 Chat with Data", "🎨 AI Visualizations"])

        # -------- TAB 1 --------
        with tab1:
            st.subheader("📄 Data Preview")
            st.dataframe(df.head(5))
            st.divider()

            user_input = st.text_area(
                "🗨️ Ask a question about this data:",
                placeholder="e.g., What is the average value of the sales column?"
            )

            if st.button("Generate Answer"):
                if not api_key:
                    st.warning("⚠️ Please enter your GROQ API key in the sidebar.")
                elif not user_input:
                    st.warning("⚠️ Please ask a question first.")
                else:
                    try:
                        os.environ["GROQ_API_KEY"] = api_key
                        llm = ChatGroq(
                            model="llama-3.3-70b-versatile",
                            temperature=temperature
                        )
                        agent = create_pandas_dataframe_agent(
                            llm, df, verbose=True, allow_dangerous_code=True
                        )

                        with st.spinner("🤖 Thinking..."):
                            response = agent.run(user_input)
                            st.success("✅ Answer:")
                            st.write(response)

                    except Exception as e:
                        st.error(f"Error: {str(e)}")

        # -------- TAB 2 --------
        with tab2:
            st.subheader("📊 Chat to Generate Charts")
            st.write("Ask for a chart (e.g., 'Show a bar chart of the top 10 categories')")

            viz_input = st.text_input("Describe your visualization:", key="viz_input")

            if st.button("Generate Visualization"):
                if not api_key:
                    st.warning("⚠️ Please enter your GROQ API key.")
                elif not viz_input:
                    st.warning("⚠️ Please describe a visualization.")
                else:
                    try:
                        os.environ["GROQ_API_KEY"] = api_key

                        llm = ChatGroq(
                            model="llama-3.3-70b-versatile",
                            temperature=0
                        )

                        agent = create_pandas_dataframe_agent(
                            llm, df, verbose=True, allow_dangerous_code=True
                        )

                        with st.spinner("📈 Creating your chart..."):
                            full_prompt = (
                                f"Create a visualization for: {viz_input}. "
                                "Instruction: Use matplotlib and seaborn. "
                                "Define the figure using 'fig, ax = plt.subplots()'. "
                                "Do not call plt.show()."
                            )

                            agent.run(full_prompt)

                            st.pyplot(plt.gcf())
                            plt.close('all')

                    except Exception as e:
                        st.error(f"Error generating plot: {str(e)}")

    except Exception as e:
        st.error(f"Error loading file: {str(e)}")

else:
    st.info("📁 Please upload a CSV file to get started.")
