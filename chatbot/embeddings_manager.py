from langchain_ollama import OllamaEmbeddings
from langchain_openai import OpenAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from utils.config import * 
from huggingface_hub import login
class EmbeddingsManager:
    def __init__(self, model_name=None):
        self.model_name = model_name or DEFAULT_EMBEDDING_MODEL
        self.embeddings = self._load_embeddings()

    def _hf_login(self):
        """
        Log in to the Hugging Face Hub using the API token, If HuggingFace is selected.

        """
        try:
            login(token=HUGGINGFACE_API_TOKEN)
            print("Logged in to Hugging Face Hub successfully.")
        except Exception as e:
            print(f"Failed to log in to Hugging Face Hub: {e}")
            raise

    def _load_embeddings(self):
        """
        Load the specified embedding model.
        
        Args:
            modelname: Contains the embedding model to be used.
        
        Returns: 
            Vector embeddings of the PDF

        Raises:
            ValueError: Unsupported embedding model

        """
        # Retrieve the configuration for the selected model
        config = EMBEDDING_MODELS_CONFIG.get(self.model_name)
        if not config:
            raise ValueError(f"Unsupported embedding model: {self.model_name}")
        
        if self.model_name == "openai":
            open_ai_embeddings = OpenAIEmbeddings(**config)
            return open_ai_embeddings
        
        elif self.model_name == "huggingface":
            self._hf_login()
            hf_embeddings = HuggingFaceEmbeddings(**config)
            return hf_embeddings
        
        elif self.model_name == "ollama":
            ollama_embeddings = OllamaEmbeddings(**config)
            return ollama_embeddings
        else:
            raise ValueError(f"Unsupported embedding model: {self.model_name}")

    def get_embeddings(self):
        return self.embeddings