---
type: summary
source: 01_Raw/github/anthropics/claude-cookbooks/capabilities/README.md
source_url: https://github.com/anthropics/claude-cookbooks/blob/main/capabilities/README.md
title: "Claude Cookbooks — capabilities/ README"
summarized_at: 2026-05-05
entities_referenced: [Structured-outputs]
concepts_referenced: []
---

The `capabilities/` directory of the Claude Cookbooks groups guides that showcase specific capabilities where Claude excels. Each guide explores one capability in depth — use cases, prompt-engineering techniques to optimize results, and approaches for evaluating Claude's performance.

**Guides:**

- **Classification with Claude** (`classification/guide.ipynb`) — classification tasks especially in scenarios with complex business rules and limited training data. Walks through data preparation, prompt engineering with retrieval-augmented generation (RAG), testing, and evaluation.
- **Retrieval Augmented Generation with Claude** (`retrieval_augmented_generation/guide.ipynb`) — building a RAG system from scratch, optimizing performance, and creating an evaluation suite. Covers techniques like summary indexing and re-ranking and how they improve precision, recall, and accuracy in QA tasks.
- **Retrieval Augmented Generation with Contextual Embeddings** (`contextual-embeddings/guide.ipynb`) — adds relevant context to each chunk before embedding to address the limited-context-per-chunk problem. Demonstrates contextual embeddings with semantic search, BM25, and reranking.
- **Summarization with Claude** (`summarization/guide.ipynb`) — multi-shot, domain-based, and chunking summarization techniques; strategies for long-form content and multiple documents; evaluation as art-plus-method.
- **Text-to-SQL with Claude** (`text_to_sql/guide.ipynb`) — generating complex SQL from natural language with prompting techniques, self-improvement, and RAG. Includes evals for syntax, data correctness, row count, and more.
- **Knowledge Graph Construction with Claude** (`knowledge_graph/guide.ipynb`) — end-to-end knowledge-graph build: named entity recognition, relation extraction, entity resolution, multi-hop querying. Uses structured outputs for schema-validated extraction and Claude-driven deduplication in place of string-similarity heuristics.

**Getting started.** Each guide is self-contained — open the directory and follow `guide.ipynb`. All necessary code, data, and evaluation scripts are included to reproduce examples and experiments.
