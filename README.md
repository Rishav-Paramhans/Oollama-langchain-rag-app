# RAG_with_Oollama-langchain-rag-appLLAMA_and_Langchain
This is a basic RAG application using Ollama (open source LLMs) and Langchain for the pipeline components, deployable on AWS

### How to Build (On Local Machine)
1. Install Ollama - https://ollama.com/ for Window/Mac
2. Check if Ollama is installed correctly by writting ollama on your local machine terminal- If it lists the available commands from Ollama- Installation is successful
3. Launch the Ollama client on your local machine and pull/run the relevant embeddings and LLM model with the command -
    ollama pull nomic-embed-text
    ollama pull llama3.1
    ollama run llama3.1
4. run the gui.py file- opens up a Gradio bases GUI where the user can upload document and run the prompt to get the RAG up and running

### Running Directly through the Docker image
#### On Local Machine (Windows/Linux)
1. Install Docker Desktop on Local Machine
2. Check if the docker installtion was successful
   sudo yum update -y
   sudo yum install docker
   sudo docker --version
3. Start the docker service
   sudo service docker start
4. Pull the Docker image from the Docker hub
   sudo docker pull rishavparamhans/mvp_rag_app:03
5. Run the docker container:
   sudo docker --rm -d -p 80:8000 rishavparamhans/mvp_rag_app:03
6. Once the docker container is up and running, access the RAG APP
   http://localhost:8000/

#### on AWS EC2 Instance
1. First create an EC2 instace with correctly configured Security Group and Network inbound rules 
2. Follow the same steps as on local machine and access the app with
   http://<your public ipv4>:8000/

## Contact
For questions reagrding the project, feel free to post here or directly contact the author at rishavkrparamhans@gmail.com