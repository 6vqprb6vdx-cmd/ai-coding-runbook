---
type: summary
source: 01_Raw/github/anthropics/claude-cookbooks/third_party/ElevenLabs/README.md
source_url: https://github.com/anthropics/claude-cookbooks/blob/main/third_party/ElevenLabs/README.md
title: "Claude Cookbooks — third_party/ElevenLabs README (low-latency voice assistant)"
summarized_at: 2026-05-05
entities_referenced: [Streaming-API]
concepts_referenced: []
---

ElevenLabs <> Claude cookbook for building a low-latency voice assistant by combining ElevenLabs speech-to-text/text-to-speech with Claude's responses, progressively optimizing for real-time performance.

**Included.**

- **Low Latency Voice Assistant Notebook (`low_latency_stt_claude_tts.ipynb`).** Interactive tutorial — using ElevenLabs STT, generating Claude responses and measuring latency, how streaming reduces time-to-first-token, streaming TTS for faster playback, tradeoffs across streaming approaches, and why WebSocket streaming wins on latency-vs-quality.
- **WebSocket Streaming Script (`stream_voice_assistant_websocket.py`).** Production-ready conversational voice assistant with continuous mic input, gapless audio playback, lowest possible latency via WebSocket.

**Setup.** Create venv. Get an ElevenLabs API key (TTS, STT, voices read, models read permissions) and an Anthropic API key. `cp .env.example .env`, set `ELEVENLABS_API_KEY` and `ANTHROPIC_API_KEY`. `pip install -r requirements.txt`.

**Workflow.** Work through the notebook (with performance metrics at each optimization step), then run the production script. Press Enter to start/stop recording; Ctrl+C to exit. The script demonstrates real-time recording with sounddevice, continuous conversation with context retention, WebSocket streaming, and a custom audio queue.

**Troubleshooting.** Audio popping/crackling on the free tier comes from MP3 chunked decoding (FFmpeg sometimes receives incomplete frames); the script skips failed chunks. Eliminate entirely by upgrading to a paid tier and switching to `pcm_44100`. Other guidance covers API-key setup verification, PortAudio/FFmpeg installation per OS (`brew install portaudio ffmpeg`, `apt-get install portaudio19-dev ffmpeg`, manual FFmpeg + PATH on Windows), microphone permissions per OS, and WebSocket connection failures (check internet, firewall on port 443, VPN/proxy, rate limits).

**Project ideas.** Meeting note-taker, language learning tutor, interactive storyteller, hands-free coding assistant, voice-activated smart home, personal voice journal.

**Resources.** ElevenLabs platform, API docs, Voice Library, API Playground, Python SDK.
