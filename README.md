# Ai-agent

## Setup

1. Open PowerShell in `c:\Users\metan\Ai-agent`
2. Create a virtual environment:
   ```powershell
   python -m venv venv
   ```
3. Activate it in PowerShell:
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```
4. Install dependencies:
   ```powershell
   python -m pip install -r requirements.txt
   ```
5. Create a `.env` file with your OpenAI key:
   ```text
   OPENAI_API_KEY=your_key_here
   ```
6. Run the app:
   ```powershell
   python .\main.py
   ```

Gemini (Google) usage:

- To use Google Gemini instead of OpenAI, set `GEMINI_API_KEY` in your `.env` with an API key that has access to the Generative API.
- The script will prefer `GEMINI_API_KEY` over `OPENAI_API_KEY` when both are present.
- Example `.env`:
   ```text
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

Note: This script calls the Google Generative REST endpoint for `text-bison-001` by default, and it retries `v1beta2` if needed. If you get a 404 error, your key may not be authorized for this model or the Generative API.

CLI usage:

- Send a custom prompt on the command line:

   ```powershell
   python .\main.py "Summarize Python decorators"
   ```

- To choose a Gemini model, set `GEMINI_MODEL` in `.env` (for example `chat-bison-001` to use a chat-capable model).

## Notes

- Use `Activate.ps1` in PowerShell, not `activate`.
- If PowerShell blocks execution, run once:
  ```powershell
  Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
  ```
- Never commit your real `.env` secrets into source control.
