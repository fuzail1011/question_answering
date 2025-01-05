# Simple Question Answering app

Uses open source Transformers model `deepset/roberta-base-squad2` for question answering <br>
RAG setup using FAISS vector store for retrieval

## Steps to run :

1. Create a virual environment -
   `python -m venv env`

2. Activate your virtual environment <br>
   For Windows - `.\env\Scripts\activate` <br>
   For Linux - `source venv/bin/activate`

3. Run the command - `streamlit run main.py`

## If you want to run the app through containerization with Docker, follow the steps below :

1. Build the docker image <br>
   `docker-compose up --build`

2. Starting the container <br>
   `docker-compose up`

3. Stopping the container <br>
   `docker-compose down`

4. Access the app through the below link : <br>
   `http://localhost:8501`
