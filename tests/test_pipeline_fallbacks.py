import os
import unittest
from unittest.mock import patch

from core.summarizer import summarize, generate_title
from core.extractor import extract_action_items, extract_key_decisions, extract_questions
from core.rag_engine import build_rag_chain, ask_question


class PipelineFallbackTests(unittest.TestCase):
    def test_summarize_and_title_work_without_llm(self):
        transcript = (
            "We discussed the launch timeline for the new product. "
            "The team agreed to finalize the budget by Friday and share updates in the next meeting."
        )
        with patch.dict(os.environ, {"MISTRAL_API_KEY": ""}, clear=False):
            summary = summarize(transcript)
            title = generate_title(transcript)

        self.assertTrue(summary.strip())
        self.assertTrue(title.strip())

    def test_extractors_return_content_without_llm(self):
        transcript = (
            "We need to send the budget draft by Friday. "
            "The team agreed to launch next month. "
            "What about the onboarding timeline?"
        )
        with patch.dict(os.environ, {"MISTRAL_API_KEY": ""}, clear=False):
            action_items = extract_action_items(transcript)
            decisions = extract_key_decisions(transcript)
            questions = extract_questions(transcript)

        self.assertTrue(action_items.strip())
        self.assertTrue(decisions.strip())
        self.assertTrue(questions.strip())

    def test_rag_chain_answers_questions_without_llm(self):
        transcript = "The launch will happen on Friday and the marketing team will prepare the campaign."
        with patch.dict(os.environ, {"MISTRAL_API_KEY": ""}, clear=False):
            rag_chain = build_rag_chain(transcript)
            answer = ask_question(rag_chain, "When will the launch happen?")

        self.assertTrue(answer.strip())


if __name__ == "__main__":
    unittest.main()
