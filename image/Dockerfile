FROM public.ecr.aws/lambda/python:3.11

# Copy requirements.txt
COPY ./requirements.txt

# Required to make SQLite3 work for Chroma
RUN pip install pysqlite3-binary

# Install the specified packages
RUN pip install -r ./requirements.txt --upgrade

# Install dependencies required to add ollama (like curl)
RUN apt-get update && apt-get install -y curl

# Download and install ollama binary
RUN curl -o /usr/local/bin/ollama https://ollama.com/download/linux && \
    chmod +x /usr/local/bin/ollama

# For local testing
EXPOSE 8000

# Set IS_USING_IMAGE_RUNTIME Environment Variable
ENV IS_USING_IMAGE_RUNTIME=True

# Copy all files in ./src
COPY src/* 
COPY src/langchain-ollama
COPY src/langchain-ollama/chroma
