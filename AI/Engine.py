import ollama
import requests

class AIEngine:
    """Handles interaction with a local LLM via the official Ollama library."""

    def __init__(self,model_name : str  = "phi3:mini",temperature : float = 0.2, num_predict: int = 200,):
        self.model_name = model_name
        self.url = "http://localhost:11434/api/generate"

        self.options = {"temperature":temperature,"num_predict":num_predict }

    def ask_questions(self,context_chunks:list[str] , question:str) -> str:
 
        """Combines document context chunks with the user question and returns the local LLM answer."""

        full_context = "\n---\n".join(context_chunks)
        prompt = f"""
You are an expert assistant analyzing document context.
Answer the user's question using ONLY the provided document context below.
If the answer is not contained within the context, state clearly: "I cannot find the answer in the provided document."

--- DOCUMENT CONTEXT ---
{full_context}

--- USER QUESTION ---
{question}
"""

        try : 
            response = ollama.chat(
                model=self.model_name,
                messages= [{"role":"user", "content":prompt}],
                options= self.options,
            )
            return response["message"]["content"]
        except Exception as e:
            return f" Local AI Engine Error: {e}"

    def Summarize_document(self,context_chunks:list[str]) ->  str :
        """Summarize The User Document and returns the Local LLM answer"""
        full_context = "\n---\n".join(context_chunks)
        prompt = f"""
        You are an expert assistant Summarize document context.
        Summarize the content  using ONLY the provided document context below.
        The Summarize Content Should be limit to 6 lines.
        The Summarize part should only contain imporatant topics"
        
        --- DOCUMENT CONTEXT ---
        {full_context} """

        try : 
            response = ollama.chat(
            model=self.model_name,
            messages= [{"role":"user", "content":prompt}],
            options= self.options,)
            return response["message"]["content"]

        except Exception as e:
            return f" Local AI Engine Error: {e}"


    def generate(self, prompt):
        response = requests.post(
            self.url,
            json={
                "model": self.model_name,
                "prompt": prompt,
                "stream": False
            }
        )

        response.raise_for_status()
        return response.json()["response"]