"""LLM generation helpers."""

import os

import requests
from openai import OpenAI

from rag.config import DEFAULT_PROVIDER, GEN_MODEL, OLLAMA_BASE_URL
from rag.generation.prompts import answer_prompt, summary_prompt


OLLAMA_TIMEOUT = 120

PRICING = {
    "gpt-4.1-mini": {
        "input": 0.40 / 1_000_000,
        "output": 1.60 / 1_000_000,
    },
    "gpt-4o-mini": {
        "input": 0.15 / 1_000_000,
        "output": 0.60 / 1_000_000,
    },
}


def _calculate_cost(model: str, input_tokens: int, output_tokens: int) -> float:
    """Estimate OpenAI request cost."""
    pricing = PRICING.get(model)
    if pricing is None:
        return 0.0

    return (
        input_tokens * pricing["input"]
        + output_tokens * pricing["output"]
    )


def _generate_with_ollama(prompt: str, model: str) -> dict:
    """Generate text with Ollama."""
    url = f"{OLLAMA_BASE_URL}/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
    }

    try:
        response = requests.post(url, json=payload, timeout=OLLAMA_TIMEOUT)
        response.raise_for_status()
    except requests.RequestException as exc:
        raise RuntimeError(
            f"Failed to connect to Ollama at {OLLAMA_BASE_URL}: {exc}"
        ) from exc

    data = response.json()
    answer = data.get("response")

    if answer is None:
        raise RuntimeError(f"Unexpected Ollama response format: {data}")

    return {
        "answer": answer.strip(),
        "input_tokens": None,
        "output_tokens": None,
        "cost_usd": 0.0,
    }


def _generate_with_openai(prompt: str, model: str) -> dict:
    """Generate text with OpenAI."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not set")

    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )

    usage = response.usage
    input_tokens = usage.prompt_tokens if usage else 0
    output_tokens = usage.completion_tokens if usage else 0

    message = response.choices[0].message.content or ""

    return {
        "answer": message.strip(),
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "cost_usd": _calculate_cost(model, input_tokens, output_tokens),
    }


def _generate(
    prompt: str,
    model: str = GEN_MODEL,
    provider: str = DEFAULT_PROVIDER,
) -> dict:
    """Run selected generation backend."""
    if provider == "ollama":
        return _generate_with_ollama(prompt, model)

    if provider == "openai":
        return _generate_with_openai(prompt, model)

    raise ValueError(f"Unsupported provider: {provider}")


def generate_answer(
    query: str,
    context: str,
    history: str,
    provider: str = DEFAULT_PROVIDER,
    model: str = GEN_MODEL,
) -> dict:
    """Generate answer from context."""
    prompt = answer_prompt(query, context, history)
    return _generate(prompt, model, provider)


def generate_summary(
    topic: str,
    context: str,
    provider: str = DEFAULT_PROVIDER,
    model: str = GEN_MODEL,
) -> dict:
    """Generate summary from context."""
    prompt = summary_prompt(topic, context)
    return _generate(prompt, model, provider)