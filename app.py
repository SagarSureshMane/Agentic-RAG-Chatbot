import streamlit as st
import os

from agents.graph import build_agent
from langchain_core.messages import HumanMessage
from rag.ingest import ingest_document

# ===================================
# BUILD AGENT
# ===================================

agent = build_agent()

THREAD_ID = "streamlit_user"

# ===================================
# PAGE CONFIG
# ===================================

st.set_page_config(
    page_title="Agentic RAG Chatbot",
    layout="wide"
)

st.title("Agentic RAG Chatbot")

# ===================================
# SIDEBAR
# ===================================

with st.sidebar:

    st.header("Upload Documents")

    uploaded_file = st.file_uploader(
        "Upload",
        type=["pdf", "docx", "txt", "xlsx"]
    )

    if uploaded_file:

        os.makedirs("uploads", exist_ok=True)

        save_path = os.path.join(
            "uploads",
            uploaded_file.name
        )

        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        with st.spinner("Creating embeddings..."):
            ingest_document(save_path)

        st.success("Document Added To RAG")

# ===================================
# CHAT HISTORY
# ===================================

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ===================================
# USER INPUT
# ===================================

prompt = st.chat_input("Ask anything...")

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
     try:

        config = {
            "configurable": {
                "thread_id": THREAD_ID
            }
        }

        response = agent.invoke(
            {
                "messages": [
                    HumanMessage(content=prompt)
                ]
            },
            config=config
        )

        # ==========================
        # Final Answer
        # ==========================

        final_response = response["messages"][-1].content

        st.markdown(final_response)

        # ==========================
        # Tool Tracking
        # ==========================

        tools_used = []

        tool_outputs = []

        for msg in response["messages"]:

            # ToolMessage
            if msg.__class__.__name__ == "ToolMessage":

                tool_name = getattr(
                    msg,
                    "name",
                    "Unknown Tool"
                )

                tools_used.append(tool_name)

                tool_outputs.append(
                    {
                        "tool": tool_name,
                        "output": msg.content
                    }
                )

        # ==========================
        # Show Tools Used
        # ==========================

        if tools_used:

            st.divider()

            st.markdown(
                "### 🔧 Tools Used"
            )

            for tool in set(tools_used):

                st.success(tool)

        # ==========================
        # Show Tool Outputs
        # ==========================

        if tool_outputs:

            with st.expander(
                "🔍 View Tool Outputs"
            ):

                for item in tool_outputs:

                    st.markdown(
                        f"**Tool:** {item['tool']}"
                    )

                    st.code(
                        item["output"][:1000]
                    )

        # ==========================
        # Save Chat History
        # ==========================

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": final_response
            }
        )

    
     except Exception as e:

        import traceback

        st.error(str(e))
        st.code(
            traceback.format_exc()
        )