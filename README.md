# Real-Time Data Processing with Pinecone and OpenAI

This project processes real-time data and stores it using Pinecone and OpenAI embeddings. It includes gRPC services for vector management and utilizes various libraries for data cleaning, embedding generation, and storage.

## Prerequisites

- Python 3.8+
- [Pipenv](https://pipenv.pypa.io/en/latest/) or `pip`
- [Pinecone API Key](https://www.pinecone.io/)
- [OpenAI API Key](https://openai.com/api/)

## Installation

1. **Clone the repository**:

   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**

   Create a .env file in the root directory or use the provided .env.example as a template:

   ```
    PINECONE_API_KEY=""
    PINECONE_HOST=""
    PINECONE_REGION=""
    OPENAI_API_KEY=""
   ```

## Usage

1. **Start the gRPC server:**

   ```sh
   python main.py
   ```

2. **Send data to the server** using a gRPC client by making `DataVectorRequest` calls.
