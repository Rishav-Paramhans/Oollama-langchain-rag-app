#!/bin/bash

# Start Ollama service in the background
/usr/local/bin/ollama start &

# Wait for Ollama to initialize properly (adjust sleep time if necessary)
sleep 5

# Pull the required models
/usr/local/bin/ollama pull nomic-embed-text
/usr/local/bin/ollama pull mistral
/usr/local/bin/ollama run mistral

# Run the main Gradio interface
exec "$@"
