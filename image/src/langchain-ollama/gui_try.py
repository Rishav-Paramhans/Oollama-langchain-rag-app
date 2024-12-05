import os
import shutil
import gradio as gr
from query_data import *
from populate_database import *

# Gradio interface function
def gradio_interface(file, query_text, progress=gr.Progress(track_tqdm=True)):
    response = ""
    if file:
        # Update the progress bar
        progress(0, "Starting file upload...")
        file_path = handle_file(file)
        progress(25, "File uploaded successfully. Processing PDF...")

        # Step 2: Call the function to process the PDF and populate the database
        populate_message = process_pdf()
        progress(75, "PDF processed successfully.")

        # Log the process message
        print(populate_message)
        progress(100, "Document Indexing Process complete!")

    # Generate response only after full processing
    response = query_rag(query_text)

    return response


# Define the function to handle file upload and copy
def handle_file(file):
    # Define the target directory relative to the current working directory
    target_directory = os.path.join(os.path.dirname(os.getcwd()), "data")
    print("Target directory:", target_directory)

    # Ensure the target directory exists
    os.makedirs(target_directory, exist_ok=True)

    # Use os.path.join to handle file paths in a platform-independent way
    target_path = os.path.join(target_directory, os.path.basename(file.name))
    print("Target path:", target_path)

    # Copy the uploaded file to the target location
    shutil.copy(file.name, target_path)

    # Return a confirmation message
    print(f"File '{file.name}' uploaded and copied to '{target_path}'.")
    return target_path


if __name__ == "__main__":
    # Create Gradio layout
    with gr.Blocks() as interface:
        with gr.Row():
            with gr.Column(scale=1):  # Left column
                file_input = gr.File(label="Upload PDF")  # PDF file upload component
                query_input = gr.Textbox(lines=2, placeholder="Enter your query", label="Query")

            with gr.Column(scale=2):  # Right column
                response_output = gr.Textbox(label="Response")  # Response output field

        # Submit button (centered at the bottom)
        submit_button = gr.Button("Submit")  

        # Event handling for submit button
        submit_button.click(
            fn=gradio_interface,
            inputs=[file_input, query_input],
            outputs=[response_output],
        )

    # Launch Gradio interface
    interface.launch(server_name="0.0.0.0", server_port=8000)
