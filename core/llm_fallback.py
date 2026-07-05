import os
import re


def has_mistral_api_key() -> bool:
    return bool((os.getenv("MISTRAL_API_KEY") or "").strip())


def split_sentences(text: str) -> list[str]:
    if not text:
        return []
    cleaned = re.sub(r"\s+", " ", text).strip()
    if not cleaned:
        return []
    return [part.strip() for part in re.split(r"(?<=[.!?])\s+", cleaned) if part.strip()]


def fallback_title(transcript: str) -> str:
    words = [word for word in re.split(r"\W+", transcript or "") if word]
    if not words:
        return "Meeting Notes"
    title_words = words[:8]
    title = " ".join(title_words).strip()
    return title.title() if title else "Meeting Notes"


def fallback_summary(transcript: str) -> str:
    sentences = split_sentences(transcript)
    if not sentences:
        return "No transcript available yet."
    if len(sentences) == 1:
        return sentences[0]
    return " ".join(sentences[:3])


def fallback_action_items(transcript: str) -> str:
    sentences = split_sentences(transcript)
    items = []
    for sentence in sentences:
        lowered = sentence.lower()
        if any(keyword in lowered for keyword in [
            "need to", "should", "must", "will", "by ", "tomorrow", "friday",
            "next week", "next month", "follow up", "send", "complete", "prepare", "review"
        ]):
            items.append(sentence)

    if not items and sentences:
        items = [sentences[0]]
    if not items:
        return "No action items found."

    return "\n".join(f"{i + 1}. {item}" for i, item in enumerate(items[:5]))


def fallback_key_decisions(transcript: str) -> str:
    sentences = split_sentences(transcript)
    items = []
    for sentence in sentences:
        lowered = sentence.lower()
        if any(keyword in lowered for keyword in [
            "agreed", "decided", "approved", "confirmed", "will", "plan", "launch",
            "go ahead", "we will"
        ]):
            items.append(sentence)

    if not items and sentences:
        items = [sentences[0]]
    if not items:
        return "No key decisions found."

    return "\n".join(f"{i + 1}. {item}" for i, item in enumerate(items[:5]))


def fallback_questions(transcript: str) -> str:
    sentences = split_sentences(transcript)
    items = []
    for sentence in sentences:
        lowered = sentence.lower()
        if "?" in sentence or any(keyword in lowered for keyword in [
            "what", "when", "where", "who", "why", "how", "whether", "unclear",
            "need to know"
        ]):
            items.append(sentence)

    if not items:
        return "No open questions found."

    return "\n".join(f"{i + 1}. {item}" for i, item in enumerate(items[:5]))


def fallback_answer(transcript: str, question: str) -> str:
    sentences = split_sentences(transcript)
    if not sentences:
        return "I could not find this information in the meeting transcript."

    question_words = [word for word in re.split(r"\W+", question.lower()) if word]
    for sentence in sentences:
        lowered = sentence.lower()
        if any(word in lowered for word in question_words if len(word) > 2):
            return sentence

    return "I could not find this information in the meeting transcript."
