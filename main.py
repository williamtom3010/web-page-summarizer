# import langchain
from scrape import scrape_website,split_dom_content,clean_body_content,extract_body_content
import streamlit as st
from parser import parse_with_ollama
import pyttsx3
from summary_model import get_summary

st.title("AI Web scrapper")
url=st.text_input("Enter a web url")
if st.button("Scrap Site"):
    st.write("Scrapping Website...")
    result=scrape_website(url)
    # st.write(result)
    body_content=extract_body_content(result)
    cleaned_content=clean_body_content(body_content)
    st.session_state.dom_content = cleaned_content
    with st.expander("View dom contnt"):
        st.text_area("DOM content",cleaned_content,height=300)
    # st.write(cleaned_content)


if "dom_content" in st.session_state:
    parse_description = st.text_area("Please describe what you want to parse...")

    # Parse Content button
    if st.button("Parse Contnt"):
        st.write("Parsing the content...")
        dom_chunks = split_dom_content(st.session_state.dom_content)
        result = parse_with_ollama(dom_chunks, parse_description)
        st.write(result)
        
        # Set a flag to indicate parsing is done
        st.session_state.parsed_result = result
        st.session_state.parse_done = True  # Set the flag

        

if st.session_state.get("parse_done", False):  # Check if parsing is done
    if st.button("Summarize and Speak"):
        text = st.session_state.parsed_result
        if text.strip():
            # Generate summary
            summary = get_summary(text)
            st.write("Summary:", summary)
            
            # Speak the summary using pyttsx3
            pyttsx3.speak(summary)
        else:
            st.write("Please enter some text to summarize.")