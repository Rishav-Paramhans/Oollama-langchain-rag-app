import gradio as gr
import shutil
from query_data import *
from populate_database import *

# Gradio interface function
def gradio_interface(file, query_text, query_rag = query_rag):
    # Step 1: Process the uploaded PDF
    DATA_FOLDER_PATH = r"D:/Project/Oollama-langchain-rag-app/data"
    if file:
        file_path = handle_file(file)
        # Step 2: Call the function to process the PDF and populate the database
        populate_message = process_pdf()
        print(populate_message)

    # Step 3: Query the database after processing
    return query_rag(query_text)


# Define the function to handle file upload and copy
def handle_file(file):
    # Specify the target location where the file will be copied
    target_directory = r"D:/Project/Oollama-langchain-rag-app/data/"
    target_path = target_directory + ("{}".format(file.name)).split("\\")[-1]
    print("target path", target_path)
    
    # Copy the uploaded file to the target location
    shutil.copy(file.name, target_path)
    
    # Return a confirmation message
    print(f"File '{file.name}' uploaded and copied to '{target_path}'.")
    return target_path


if __name__ == "__main__":
    # Gradio Interface
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
