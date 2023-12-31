import os

# Name of the repository
repo_name = "architectural_blueprints"

# Directory structure to create
structure = {
    repo_name: [
        "style_guides/README.md",
        "reusable_code/README.md",
        "reusable_code/Python",
        "reusable_code/JavaScript",
        "architectures/README.md",
        "project_templates/README.md",
        "project_templates/python_package",
        "project_templates/web_app",
        "documentation/README.md",
        "LICENSE",
        "README.md"
    ]
}

def create_structure(base, structure):
    """Creates directories and files based on the provided structure."""
    for path in structure:
        dir_path = os.path.join(base, path)

        if os.path.splitext(path)[1]:
            # It's a file
            os.makedirs(os.path.dirname(dir_path), exist_ok=True)
            open(dir_path, 'a').close()
        else:
            # It's a directory
            os.makedirs(dir_path, exist_ok=True)

# Create the repository structure
create_structure(".", structure[repo_name])

# Populate initial files with basic content
with open(f"{repo_name}/README.md", "w") as f:
    f.write(f"# {repo_name}\nThis repository hosts style guides, reusable code, preferred architectures, and other resources.")

with open(f"{repo_name}/LICENSE", "w") as f:
    f.write("MIT License\n[Full license text here]")

# Define and create initial content for other files as needed...

print(f"Directory structure for {repo_name} has been created.")
