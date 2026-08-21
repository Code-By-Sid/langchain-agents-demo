Here is a complete, professional `README.md` tailored specifically for your project. You can copy and paste this directly into your GitHub repository's `README.md` file.

***

```markdown
# 🤖 LangChain Agents with Google Gemini

A simple and practical demonstration of building **tool-calling AI agents** using [LangChain](https://www.langchain.com/) and **Google Gemini**. 

This project shows how to define custom tools, initialize a Gemini-based agent, and execute single or multi-step reasoning tasks.

## ✨ Features

- **Tool Calling**: Agents can autonomously choose and use Python functions.
- **Multi-step Reasoning**: The agent can chain tools together (e.g., multiply, then divide) to solve complex queries.
- **Google Gemini Integration**: Uses `gemini-2.5-flash-lite` via LangChain's `init_chat_model`.

## 📂 Project Structure

```text
├── src/
│   ├── LangchainFrameWork.py   # Basic agent demo with a simulated weather tool
│   └── LangchainTask.py        # Math agent with add, multiply, divide, and square_root tools
├── .env.example                # Template for your environment variables
├── .gitignore
├── requirements.txt
└── README.md
```

## 🛠 Tech Stack

- **Python 3.10+**
- **LangChain** (`langchain`, `langchain-google-genai`)
- **Google Gemini API**

## ⚙️ Installation & Setup

Follow these steps to run the project locally.

### 1. Clone the repository
```bash
git clone https://github.com/<YOUR_USERNAME>/langchain-agents-demo.git
cd langchain-agents-demo
```

### 2. Create a virtual environment
```bash
python -m venv .venv

# Activate on Windows
.venv\Scripts\activate

# Activate on macOS/Linux
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up your API Key
You need a Google Gemini API key to run this code. You can get one for free from [Google AI Studio](https://aistudio.google.com/app/apikey).

Copy the example environment file and add your key:
```bash
cp .env.example .env
```
Open the `.env` file and paste your key:
```env
GOOGLE_API_KEY=your_actual_api_key_here
```

## 🚀 Usage

Run the scripts individually to see the agents in action.

**1. Basic Framework Demo (Weather Tool):**
```bash
python src/LangchainFrameWork.py
```
*Expected Output:* The agent will use the `get_weather` tool to tell you the weather in San Francisco.

**2. Math Agent Demo (Multi-tool reasoning):**
```bash
python src/LangchainTask.py
```
*Expected Output:* The agent will solve three problems of increasing complexity:
- Simple addition (`42 + 58`)
- Sequential tool calling (`15 * 8 / 3`)
- Multi-step planning (calculating the area of a rectangle, then its square root)

## 📝 Code Overview

### Defining Tools
Tools are defined using the `@tool` decorator from `langchain_core.tools`. The docstring is crucial—it tells the AI agent *when* and *how* to use the tool.

```python
from langchain_core.tools import tool
import math

@tool
def square_root(n: float) -> float:
    """Calculate the square root of a number."""
    return math.sqrt(n)
```

### Creating the Agent
The `create_agent` function binds the Gemini model and the tools together.

```python
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model

model = init_chat_model("google_genai:gemini-2.5-flash-lite")
agent = create_agent(model=model, tools=[add, multiply, divide, square_root])
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

### How to use this:
1. Go to your GitHub repository.
2. Click on the `README.md` file.
3. Click the **pencil icon** (Edit this file) in the top right.
4. Delete everything currently in the file.
5. Paste the code block above.
6. Click **Commit changes...** at the top right. 

*(Don't forget to replace `<YOUR_USERNAME>` with your actual GitHub username!)*
