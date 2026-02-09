import chromadb
from sentence_transformers import SentenceTransformer

class SkladAI:
    def __init__(self):
        # Подключаемся к нашему контейнеру ChromaDB
        self.client = chromadb.HttpClient(host='chromadb', port=8000)
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.collection = self.client.get_or_create_collection("sklad_docs")

    def add_document(self, text, doc_id):
        # Превращаем текст в вектор и сохраняем
        self.collection.add(
            documents=[text],
            ids=[doc_id]
        )

    def ask(self, question):
        # Ищем ответ по смыслу
        results = self.collection.query(query_texts=[question], n_results=1)
        return results['documents'][0]
