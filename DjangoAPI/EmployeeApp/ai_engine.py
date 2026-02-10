"""import chromadb
from sentence_transformers import SentenceTransformer

class SkladAI:
    def __init__(self):
        # Подключаемся к контейнеру ChromaDB по внутренней сети Docker
        self.client = chromadb.HttpClient(host='chromadb', port=8000)
        # Загружаем легкую модель для векторизации
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        # ИСПОЛЬЗУЕМ ТО ЖЕ ИМЯ, ЧТО В load_docs.py
        self.collection = self.client.get_or_create_collection("sklad_knowledge")

    def ask(self, question):
        # Поиск наиболее похожего текста по смыслу
        results = self.collection.query(query_texts=[question], n_results=1)
        # Возвращаем найденный документ (инструкцию)
        if results['documents'] and len(results['documents']) > 0:
            return results['documents'][0][0] 
        return "Инструкции не найдены."""

