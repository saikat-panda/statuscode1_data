import os

def generate(repo_url, root_dir):
    links = {}
    
    for subdir, _, files in os.walk(root_dir):
        class_name = os.path.basename(subdir)
        links[class_name] = []
        
        for file in files:
            if file.endswith(('.png', '.jpg', '.jpeg', '.gif')):
                file_path = os.path.relpath(os.path.join(subdir, file), root_dir)
                github_link = f"{repo_url}/blob/main/{file_path}"
                github_link.replace('\\', '/')
                links[class_name].append(github_link)
    
    return links

# Replace with your GitHub repository URL
repo_url = "https://github.com/saikat-panda/statuscode1_data.git"
# Root directory containing your dataset
root_dir = "/dataset/"

links = generate(repo_url, root_dir)

# Printing the links class-wise
for class_name, urls in links.items():
    print(f"Class: {class_name}")
    for url in urls:
        print(url)
    print("\n")

