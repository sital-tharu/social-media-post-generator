# import json

# def load_sample_posts(file_path):
#     # Open the file with UTF-8 encoding
#     with open(file_path, 'r', encoding='utf-8') as file:
#         return json.load(file)
    
 
# def save_post(post, platform):
#     # Dynamically create the filename based on the platform
#     file_name = f"{platform}_post.txt"
#     with open(file_name, 'w', encoding='utf-8') as file:
#         # Add a title and format the post with line breaks
#         file.write(f"--- {platform.capitalize()} Post ---\n\n")
#         file.write(post.strip() + "\n\n")
#         file.write("Follow us for more updates! 🚀 #InstaAI\n")

# filepath: d:\project_2.1\social-media-post-generator\src\utils\helpers.py

def save_post(post, platform):
    # Dynamically create the filename based on the platform
    file_name = f"{platform}_post.txt"
    with open(file_name, 'w', encoding='utf-8') as file:
        # Add a title and format the post with line breaks
        file.write(f"--- {platform.capitalize()} Post ---\n\n")
        file.write(post.strip() + "\n\n")
        file.write("Follow us for more updates! 🚀 #InstaAI\n")