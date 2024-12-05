# Use the official Python image with the desired version
FROM python:3.12.4-slim

# Set environment variables to avoid Python buffering logs
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the application files into the container
COPY ./src/data/* /app/src/data/
COPY ./src/langchain-ollama/* /app/src/langchain-ollama/
COPY ./src/langchain-ollama/chroma/* /app/src/langchain-ollama/chroma/
COPY ./requirements.txt /app/
# Install required packages for SQLite3 support
RUN pip install pysqlite3-binary

# Install Python dependencies from requirements.txt
RUN pip install -r requirements.txt --upgrade

# Install dependencies required to add Ollama (like curl)
RUN apt-get update && apt-get install -y curl


# Download and install Ollama binary (ensure the URL is correct for Linux)
RUN curl -fsSL https://ollama.com/install.sh | sh 

# Check if Ollama is installed correctly
RUN /usr/local/bin/ollama --version

# Add a script to run Ollama and the Gradio app
COPY ./src/langchain-ollama/entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Set the entrypoint to run Ollama and the Python script
ENTRYPOINT ["/app/entrypoint.sh"]

ENV OLLAMA_HOST http://0.0.0.0:11434

# Expose the port used by the Gradio interface
EXPOSE 8000


# Command to run the GUI (Gradio interface)
CMD ["python", "../app/src/langchain-ollama/gui.py"]
