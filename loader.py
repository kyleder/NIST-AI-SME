import os
import glob
import pickle
from os.path import join, dirname
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

load_dotenv(join(dirname(__file__), '.env.loader'))

def vectorize_pdf(pdf):
  if pdf is not None:
      pdf_reader = PdfReader(pdf)
      
      text = ""
      for page in pdf_reader.pages:
          text += page.extract_text()

      text_splitter = RecursiveCharacterTextSplitter(
          chunk_size=1000,
          chunk_overlap=200,
          length_function=len
          )
      chunks = text_splitter.split_text(text=text)

      # # embeddings
      store_name = pdf.name[:-4]
      st.write(f'{store_name}')
      # st.write(chunks)

      if os.path.exists(f"{store_name}.pkl"):
          with open(f"{store_name}.pkl", "rb") as f:
              VectorStore = pickle.load(f)
          # st.write('Embeddings Loaded from the Disk')s
      else:
          embeddings = OpenAIEmbeddings()
          VectorStore = FAISS.from_texts(chunks, embedding=embeddings)
          with open(f"{store_name}.pkl", "wb") as f:
              pickle.dump(VectorStore, f)  

def load_all_files():
  print(os.getenv("KNOWLEDGE_DIRECTORY"))
  for filename in glob.iglob(os.getenv("KNOWLEDGE_DIRECTORY") + '**/*.pdf', recursive=True):

    print(filename)

if __name__ == "__main__":
  load_all_files()