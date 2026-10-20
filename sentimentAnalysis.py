import streamlit as st
from transformers import pipeline
@st.cache_resource
def load_model():
    model_name = "cardiffnlp/twitter-roberta-base-sentiment-latest"

    return pipeline(
        "text-classification",
        model=model_name,
        tokenizer=model_name
    )

st.divider()
st.write("enter any comment: ")
st.set_page_config(
    page_title="Sentiment Analyzer",
    page_icon="💬",
    layout="wide"
)
user_comment = st.text_area(
    "Enter your comment here: ",
    placeholder="Example: The camera is amazing!",
    height=200,
    key= "comment_input"
)
if st.button("Analyze comment " , key = "analyze_comment"):
    if not user_comment.strip():
        st.warning("please enter a comment first !")
    else:
        try :
            model = load_model()
            result = model(user_comment.strip())[0]
            raw_label = result ["label"].strip().lower()
            confidence = result["score"]*100
            # Convert model labels into readable sentiment names
            label_mapping = {
                "label_0": "Negative",
                "label_1": "Neutral",
                "label_2": "Positive",
                "negative": "Negative",
                "neutral": "Neutral",
                "positive": "Positive"
            }
            sentiment = label_mapping.get(
                raw_label,
                raw_label.title()
            )

            # Display the prediction
            st.subheader("Analysis Result")
            #display the prediction 
            st.subheader("Analysis result")
            if sentiment =="Positive":
                st.success(f"Sentiment : {sentiment}")
            elif sentiment == "Negative":
                st.error(f"sentiment : { sentiment}")
            elif sentiment == "Neutral":
                st.info(f"sentiment:{sentiment}")
            else:
                st.write(f"sentiment :{sentiment}")
            st.metric(
                "Model Confidence",
                f"{confidence:.2f}%"
            )   

        except Exception as e:
            st.error(f"Could not analyze the comment: {e}")
    