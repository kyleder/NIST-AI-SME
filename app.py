import streamlit as st

with st.sidebar:
  st.title("🤖 Marvin")
  st.markdown('''
    ## The NIST 800-171 SME
    Marvin is your friendly(ish) SME that knows a whole lot about NIST 800-171 compliance and that's about it.
    ''')


def main():
  st.header("🤔 Got NIST 800-171 questions? Me too.")

if __name__ == "__main__":
  main()