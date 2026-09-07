# LangChain Learning Journey 🤖

A hands-on repository documenting my journey of learning **LangChain and LLM application development with Python**.

This repository starts with basic LLM integration and gradually moves toward **dynamic prompts, output parsing, LCEL chains, conversational memory, and chatbot development**.

---

## 📚 Topics Covered

### 1. Basic LangChain with LLMs

**Notebook:** `1_basic_langchain_with_openai.ipynb`

In this notebook, I learned the fundamentals of working with LLMs using LangChain.

#### Concepts Covered

- Connecting LLMs with LangChain
- Working with different LLM providers:
  - Google Gemini
  - OpenAI
  - OpenRouter
  - Groq
- Sending prompts to LLMs
- Invoking LLMs using LangChain
- Handling LLM responses
- Working with static prompts

---

### 2. Prompt Chains and LCEL

**Notebook:** `2_prompt_cains.ipynb`

This notebook focuses on creating more flexible LLM applications using **dynamic prompts and LangChain chains**.

#### Concepts Covered

- Dynamic prompts
- `ChatPromptTemplate`
- System and user messages
- `StrOutputParser`
- Custom transformation functions
- LangChain Chains
- LCEL (LangChain Expression Language)
- Connecting components using the pipe operator `|`

#### Example

```python
chains = prompts | llm | out | transform_case

res = chains.invoke({
    "language": "hinglish",
    "query": "I love LangChain?"
})

```


### 3. Basic Conversational Memory

**Notebook:** `3_basic_memory_with_langchain.ipynb`

This notebook demonstrates how to build a simple conversational LLM application by maintaining the **conversation history** between the user and the AI.

Instead of sending only the current question to the LLM, previous messages are stored and passed along with each new query. This allows the chatbot to maintain context throughout the conversation.

#### Concepts Covered

- Basic conversational memory
- Maintaining conversation history
- Storing user messages
- Storing AI responses
- Passing previous messages to the LLM
- Context-aware conversations
- Building a terminal-based chatbot
- Handling continuous user input
- Implementing exit conditions

#### Conversation History

The conversation history is maintained using a Python list:

python
history = []