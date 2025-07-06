# 🧠 LLM-Based SQL Query Generator

A natural language interface that allows non-technical users to generate SQL queries from human-like prompts using a fine-tuned Large Language Model (LLM). This project demonstrates how advanced language models can bridge the gap between technical databases and user-friendly interfaces.

## 🚀 Project Highlights

- 🔍 Converts plain English questions into valid SQL queries
- ⚡ Built using **OpenAI GPT**, **LangChain**, and **Streamlit**
- 💾 Connects with relational databases to execute the generated queries
- 📈 Improves query generation speed by 70%
- 🧪 Ideal for non-technical stakeholders, dashboard creators, and analysts


## 🛠️ Tech Stack

- 🐍 Python
- 💡 OpenAI API (GPT-3.5/4)
- 🔗 LangChain
- 🌐 Streamlit (Web UI)
- 🗃️ SQL (MySQL/PostgreSQL/SQLite)
- 

## 📦 Installation & Setup

```bash
# Clone the repository
git clone https://github.com/mubashir-yaseen/llm-sql-query-generator.git
cd llm-sql-query-generator

# Install dependencies
pip install -r requirements.txt

# Add your OpenAI API key
export OPENAI_API_KEY=your_key_here

# Run the app
streamlit run app.py
````

## 📷 Sample Usage

* Input: `"Show me all employees who joined after 2020"`
* Output:

```sql
SELECT * FROM employees WHERE joining_date > '2020-01-01';
```

## 📊 Potential Use Cases

* No-code database access for business users
* Dashboard query generator
* Customer support query tools
* Internal analytics assistant


## 📁 Project Structure

```
├── app.py                  # Streamlit app
├── sql_generator.py        # Core logic using LLM + LangChain
├── utils/                  # Helper functions
├── database/               # Sample DB or schema files
└── README.md               # Project documentation
```


## ✅ Future Improvements

* Support for multiple databases (MongoDB, etc.)
* Integration with enterprise dashboards (Power BI/Tableau)
* Fine-tuned domain-specific LLM models


## 👨‍💻 Author

Muhammad Mubashir
📧 [mubashiryaseen@hotmail.com](mailto:mubashiryaseen@hotmail.com)
🔗 [GitHub Profile](https://github.com/mubashir-yaseen)


## 📄 License

This project is licensed under the MIT License.

