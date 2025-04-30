# Social Media Post Generator

This project is a Social Media Post Generator that utilizes AI agents to create engaging posts tailored for different social media platforms. The application leverages AI to generate content based on specified topics and formats it according to the requirements of each platform.

## Project Structure

```
social-media-post-generator
├── src
│   ├── main.py                # Entry point of the application
│   ├── ai_agents              # Contains AI agent modules
│   │   ├── __init__.py
│   │   ├── content_generator.py # Generates content for social media posts
│   │   └── platform_adapter.py  # Adapts content for specific platforms
│   ├── utils                  # Utility functions
│   │   ├── __init__.py
│   │   └── helpers.py         # Helper functions for loading and saving posts
│   └── data                   # Sample data for testing
│       └── sample_posts.json  # JSON file with sample posts
├── requirements.txt           # Project dependencies
├── .gitignore                 # Files and directories to ignore in Git
└── README.md                  # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd social-media-post-generator
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To generate social media posts, run the main application:

```
python src/main.py
```

You can specify the platform and topic for the post generation. The application will utilize the AI agents to create and format the posts accordingly.

## Example

1. Generate a post for Twitter about "AI in Healthcare":
   ```
   python src/main.py --platform twitter --topic "AI in Healthcare"
   ```

2. The generated post will be formatted to meet Twitter's character limits and style.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.