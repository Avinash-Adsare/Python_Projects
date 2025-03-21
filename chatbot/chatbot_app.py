import streamlit as st
from transformers import AutoModelForQuestionAnswering, AutoTokenizer
import torch

@st.cache_resource
def load_model():
    # Using a robust open-source model for question answering
    model_name = "deepset/roberta-base-squad2"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForQuestionAnswering.from_pretrained(model_name)
    return tokenizer, model

def get_answer(context, question, tokenizer, model):
    # Tokenize input
    inputs = tokenizer.encode_plus(question, context, add_special_tokens=True, return_tensors="pt")
    input_ids = inputs["input_ids"].tolist()[0]

    # Get model predictions
    outputs = model(**inputs)
    answer_start_scores = outputs.start_logits
    answer_end_scores = outputs.end_logits

    # Find the start and end of the answer
    answer_start = torch.argmax(answer_start_scores)
    answer_end = torch.argmax(answer_end_scores) + 1

    # Decode the answer
    answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(input_ids[answer_start:answer_end]))
    return answer

def main():
    st.title("Context-Based Conversational Chatbot")
    st.markdown("""
    Welcome! This chatbot provides answers based on a given context. Enter a context and ask questions about it!
    """)

    tokenizer, model = load_model()

    # Input context and question
    context = st.text_area("Provide Context:", height=200)
    question = st.text_input("Your Question:")

    if st.button("Get Answer") and context and question:
        answer = get_answer(context, question, tokenizer, model)
        st.markdown(f"**Answer:** {answer}")

if __name__ == "__main__":
    main()
