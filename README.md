# Alter-Ego

🦸 **Alter-Ego** is a conversational playground for interacting with a variety of AI-powered personas, each with their own unique style, expertise, and personality. Choose your alter-ego and chat with them in your terminal!

## Features

- Multiple distinct AI personas ("egos"), including:
  - Captain Mainwaring (Dad's Army)
  - Dante Alighieri (in terza rima)
  - Aeneas (Virgil's Aeneid)
  - Odysseus (Homeric epic)
  - Sarcastic MondayGPT
  - Aviation expert
  - Bleak "Doom" AI
  - British writing assistant ("Clerk")
- Each ego has a custom prompt and conversation style.
- Conversation history is preserved within each session for context-aware responses.
- Easily extensible: add your own egos by creating new Python files in the `egos/` directory.

## Requirements

- Python 3.11+
- See [requirements.txt](requirements.txt) for dependencies.

## Setup

1. **Clone the repository:**
   ```sh
   git clone https://github.com/Leofric99/alter-ego.git
   ```
**Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Run Alter-Ego:**
    ```sh
    python3 -m egos
    ```

## Usage

- Follow the on-screen prompts to select an ego and start chatting.
- To add a new ego, create a Python file in the `egos/` directory and define its persona and prompt logic.