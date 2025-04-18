## agent.py Features

- 💬 **Natural Language Querying**: Ask questions like “How many females survived?” or “What’s the average fare paid by third-class passengers?” — and get meaningful responses.
- 🧠 **Dual LLM Support**: Utilizes `Mistral-7B-Instruct-v0.3` (via HuggingFace) — one model specialized for SQL generation, another for natural response generation.
- 🗃️ **Auto SQL Generation**: Converts questions into SQLite queries only when relevant to the data.
- 📊 **Smart Graphs**: Automatically detects graph-worthy queries and generates visual insights.
- 🛑 **Noise Filtering**: Ignores unrelated/generic questions like “how are you?” with a `[nthg]` response.

---

## 🧩 Table Schema

The assistant works on a Titanic dataset with the following `Observation` table schema:

| Column       | Type    | Description                                            |
|--------------|---------|--------------------------------------------------------|
| `age`        | REAL    | Age of the passenger                                   |
| `pclass`     | INT     | Passenger class (1st, 2nd, 3rd)                        |
| `sibsp`      | INT     | Number of siblings/spouses aboard                      |
| `parch`      | INT     | Number of parents/children aboard                      |
| `sex_id`     | TEXT    | Gender (1 = male, 0 = female)                         |
| `fare`       | REAL    | Ticket fare in dollars                                 |
| `adult_male` | INT     | Adult male flag (1 = yes, 0 = no)                      |
| `alone`      | INT     | Alone flag (1 = alone, 0 = not alone)                  |
| `embarked_id`| INT     | Port of embarkation (-1 = Unknown, 0 = Cherbourg/Southampton, 1 = Queenstown) |
| `survived`   | INT     | Survival status (1 = survived, 0 = not survived)       |

---

## 🧠 How It Works

1. **Query Understanding**:
   - Text input is parsed using a HuggingFace-hosted Mistral LLM.
   - If relevant, an SQL query is generated.
   - Otherwise, returns `[nthg]` for generic prompts.

2. **Data Processing**:
   - SQL query is run against the local Titanic database.
   - If applicable, a graph type is predicted and generated from the data.

3. **Response Generation**:
   - Final answer is composed using both the data and a natural language model — without exposing backend operations like SQL or graph creation.

---

## 📁 Key Components

- `query.py`: Executes SQLite queries.
- `query_fixer.py`: Formats SQL for cleaner execution.
- `graph.py`: Detects graph intent & renders visualizations.
- `main.py`: Core orchestration script for LLMs and logic.
- HuggingFace Models: Mistral 7B for both query generation and response crafting.

---

## 🔐 API Token

Set your HuggingFace API token via:

```python
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "your_hf_token_here"
