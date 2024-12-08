import argparse
from langchain.vectorstores.chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama
from get_embedding_function import get_embedding_function
import gradio as gr
import os 
import subprocess  # To run external scripts
import shutil
# Get the current script's directory
script_dir = os.path.dirname(os.path.realpath(__file__))

# Get the parent directory of the script's directory
src_dir = os.path.dirname(script_dir)

image_dir = os.path.dirname(src_dir)

CHROMA_PATH = os.path.join(image_dir, "chroma")
PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""


def main():
    # Create CLI.
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    args = parser.parse_args()
    query_text = args.query_text
    query_rag(query_text)


def query_rag(query_text: str):
    # Prepare the DB.
    embedding_function = get_embedding_function()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the DB.
    results = db.similarity_search_with_score(query_text, k=5)

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)
    # print(prompt)

    model = Ollama(model="llama3.1")
    response_text = model.invoke(prompt)

    sources = [doc.metadata.get("id", None) for doc, _score in results]
    formatted_response = f"Response: {response_text}\nSources: {sources}"
    print(formatted_response)
    return response_text

"""def process_pdf(file_path):
    #Trigger the populate_database script when a new PDF is uploaded.
    # Assuming the 'populate_database.py' script is in the same directory
    script_path = "populate_database.py"
    if os.path.exists(script_path):
        # Run the script using subprocess
        subprocess.run(["python", script_path], check=True)  # Reset flag is optional
        return f"Database has been populated with {file_path}"
    else:
        return "Error: 'populate_database.py' script not found.
"""
    



if __name__ == "__main__":
    #main()
    # Create Gradio interface
    interface = gr.Interface(
        fn= gradio_interface,  # Function to call
        inputs=[
            gr.File(label="Upload PDF"),  # PDF file upload component
            gr.Textbox(lines = 2, placeholder="Enter your query"),  # Input component (textbox for user query)
        ],
        outputs=gr.Textbox(label="Response"),  # Output component (textbox to display response)
        live=True  # Optional: Enable live updates as the user types (can be set to False
    )
    interface.launch()