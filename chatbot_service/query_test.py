from llama_index.core.schema import TextNode
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings, VectorStoreIndex
from llama_index.llms.groq import Groq
from llama_index.core import StorageContext
from llama_index.core import load_index_from_storage
from llama_index.core.schema import TextNode
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings, VectorStoreIndex


def create_llama_index():
    try:
        index_dir = './index'  # Specify the directory your index will be stored
        
        nodes = [
            TextNode(
                text="Kosiarka spalinowa",
                metadata={
                    "marka": "Stiga",
                    "cena": 1200,
                    "stan magazynowy": 15,
                    "kategoria": "Narzędzia ogrodnicze"
                }
            ),
            TextNode(
                text="Podkaszarka elektryczna",
                metadata={
                    "marka": "Bosch",
                    "cena": 300,
                    "stan magazynowy": 25,
                    "kategoria": "Narzędzia ogrodnicze"
                }
            ),
            TextNode(
                text="Sekator do gałęzi",
                metadata={
                    "marka": "Fiskars",
                    "cena": 70,
                    "stan magazynowy": 40,
                    "kategoria": "Narzędzia ogrodnicze"
                }
            ),
            TextNode(
                text="Ręczny opryskiwacz",
                metadata={
                    "marka": "Gardena",
                    "cena": 45,
                    "stan magazynowy": 50,
                    "kategoria": "Narzędzia ogrodnicze"
                }
            ),
            TextNode(
                text="Grabie metalowe",
                metadata={
                    "marka": "Wolf-Garten",
                    "cena": 30,
                    "stan magazynowy": 35,
                    "kategoria": "Narzędzia ogrodnicze"
                }
            ),
            TextNode(
                text="Pistolet do kleju",
                metadata={
                    "marka": "Yato",
                    "cena": 70,
                    "stan magazynowy": 22,
                    "kategoria": "Narzędzia wykończeniowe"
                }
            ),
            TextNode(
                text="Taśma malarska",
                metadata={
                    "marka": "Tesa",
                    "cena": 10,
                    "stan magazynowy": 100,
                    "kategoria": "Narzędzia wykończeniowe"
                }
            ),
            TextNode(
                text="Szpachla stalowa",
                metadata={
                    "marka": "Condor",
                    "cena": 20,
                    "stan magazynowy": 55,
                    "kategoria": "Narzędzia wykończeniowe"
                }
            ),
            TextNode(
                text="Wałek malarski",
                metadata={
                    "marka": "Hamilton",
                    "cena": 35,
                    "stan magazynowy": 30,
                    "kategoria": "Narzędzia wykończeniowe"
                }
            ),
            TextNode(
                text="Paca z zębami",
                metadata={
                    "marka": "Hardex",
                    "cena": 15,
                    "stan magazynowy": 40,
                    "kategoria": "Narzędzia wykończeniowe"
                }
            ),
            TextNode(
                text="Wkrętarka akumulatorowa",
                metadata={
                    "marka": "Makita",
                    "cena": 500,
                    "stan magazynowy": 20,
                    "kategoria": "Narzędzia warsztatowe"
                }
            ),
            TextNode(
                text="Szlifierka kątowa",
                metadata={
                    "marka": "Bosch",
                    "cena": 250,
                    "stan magazynowy": 18,
                    "kategoria": "Narzędzia warsztatowe"
                }
            ),
            TextNode(
                text="Młotek ślusarski",
                metadata={
                    "marka": "Stanley",
                    "cena": 40,
                    "stan magazynowy": 45,
                    "kategoria": "Narzędzia warsztatowe"
                }
            ),
            TextNode(
                text="Klucz nastawny",
                metadata={
                    "marka": "Neo Tools",
                    "cena": 30,
                    "stan magazynowy": 60,
                    "kategoria": "Narzędzia warsztatowe"
                }
            ),
            TextNode(
                text="Imadło warsztatowe",
                metadata={
                    "marka": "Topex",
                    "cena": 150,
                    "stan magazynowy": 10,
                    "kategoria": "Narzędzia warsztatowe"
                }
            )
        ]
        
        embed_model = HuggingFaceEmbedding( model_name="BAAI/bge-small-en-v1.5")
        index=VectorStoreIndex(nodes, embed_model=embed_model)
        Settings.embed_model = embed_model
        
        index.storage_context.persist(persist_dir=index_dir)

        return print({'result': 'File indexed successfully'})
    except Exception as e:
        return print({'error':  f"An error occurred: {e}"})
    
    
#create_llama_index()


api_key = "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"

llm = Groq(model="llama3-8b-8192", api_key=api_key)

def query_index():
    try:
        
        index_dir = 'final_index'
        Settings.embed_model = HuggingFaceEmbedding(
            model_name="BAAI/bge-small-en-v1.5"
        )
        #data = request.get_json()
        #prompt = data.get('prompt')
        prompt = "A czym jest ten najtanszy produkt w sklepie?"
        
        #chatHistory = data.get('chatHistory')
        
        storage_context = StorageContext.from_defaults(persist_dir=index_dir)
        index = load_index_from_storage(storage_context)
        #query_engine = index.as_query_engine(llm=llm)
        
        chat_engine = index.as_chat_engine(chat_mode="condense_question", llm=llm, verbose=True)

        response_node = chat_engine.chat(prompt)  # chat here
        print({'result':  response_node.response})
        
    except Exception as e:
        return print({'error':  f"An error occurred: {e}"})
    
query_index()