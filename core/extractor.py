#Actionableitems , decision , questions 

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
import os 

from core.llm_fallback import (
    fallback_action_items,
    fallback_key_decisions,
    fallback_questions,
    has_mistral_api_key,
)


def get_llm():
    if not has_mistral_api_key():
        raise RuntimeError("MISTRAL_API_KEY is not set")
    return (
        RunnablePassthrough() | RunnableLambda(lambda x : {"text" : x}) |ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human","{text}"),
    ]) | llm |StrOutputParser()
    )

def extract_action_items(transcript:str)->str:
    try:
        chain = build_chain(
             "You are an expert meeting analyst. From the meeting transcript, "
            "extract all action items. For each provide:\n"
            "- Task description\n"
            "- Owner (who is responsible)\n"
            "- Deadline (if mentioned, else write 'Not specified')\n\n"
            "Format as a numbered list. If none found say 'No action items found.'"
        )

        return chain.invoke(transcript)
    except Exception:
        return fallback_action_items(transcript)


def extract_key_decisions(transcript: str) -> str:
    try:
        chain = build_chain(
            "You are an expert meeting analyst. From the meeting transcript, "
            "extract all key decisions made. Format as a numbered list. "
            "If none found say 'No key decisions found.'"
        )
        return chain.invoke(transcript)
    except Exception:
        return fallback_key_decisions(transcript)


def extract_questions(transcript: str) -> str:
    try:
        chain = build_chain(
            "From the meeting transcript, extract all unresolved questions "
            "or topics needing follow-up. Format as a numbered list. "
            "If none found say 'No open questions found.'"
        )
        return chain.invoke(transcript)
    except Exception:
        return fallback_questions(transcript)