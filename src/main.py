import os
from ai_agents.content_generator import ContentGenerator
from ai_agents.platform_adapter import PlatformAdapter
from utils.helpers import save_post

def main():
    # Initialize AI agents
    content_generator = ContentGenerator()
    platform_adapter = PlatformAdapter()
    
    # Ask the user for the platform and topic
    platform = input("Enter the platform (e.g., Twitter, Instagram): ").strip()
    topic = input("Enter the topic you want to generate a post about: ").strip()
    
    # Generate a post
    generated_post = content_generator.generate_post(platform, topic)
    print(f"\nGenerated Post: {generated_post}")  # Display the generated post
    
    # Adapt the post for the specific platform
    adapted_post = platform_adapter.adapt_post(generated_post, platform)
    print(f"\nAdapted Post for {platform}: {adapted_post}")  # Display the adapted post
    
    # Save the generated post
    save_post(adapted_post, platform)
    print(f"\nPost saved for platform: {platform}")

if __name__ == '__main__':
    main()