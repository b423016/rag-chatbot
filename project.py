import os

def create_project_structure():
    # Define the base directory
    base_dir = "rag_chatbot_project"
    
    # Define the directory structure
    directories = [
        "data",
        "app",
        "responses"
    ]
    
    # Define files to create
    files = {
        "data/sample_data.csv": "",
        "app/__init__.py": "",
        "app/data_loader.py": "",
        "app/rag_pipeline.py": "",
        "app/chatbot.py": "",
        "app/streamlit_app.py": "",
        "requirements.txt": "",
        ".env": "",
        "README.md": "# RAG Chatbot Project\n\nA chatbot implementation using Retrieval Augmented Generation.",
        "responses/chatbot_responses.txt": ""
    }
    
    # Create base directory
    os.makedirs(base_dir, exist_ok=True)
    
    # Create directories
    for dir_name in directories:
        dir_path = os.path.join(base_dir, dir_name)
        os.makedirs(dir_path, exist_ok=True)
        print(f"Created directory: {dir_path}")
    
    # Create files
    for file_path, content in files.items():
        full_path = os.path.join(base_dir, file_path)
        with open(full_path, 'w') as f:
            f.write(content)
        print(f"Created file: {full_path}")

if __name__ == "__main__":
    create_project_structure()