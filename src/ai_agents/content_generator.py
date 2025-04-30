import ollama

class ContentGenerator:
    def generate_post(self, platform, topic):
        # Define the prompt for Ollama
        prompt = f"Generate a social media post for {platform} about {topic}."
        print(f"Prompt sent to Ollama: {prompt}")  # Debugging: Show the prompt
        
        # Use Ollama to generate the post
        try:
            response = ollama.generate(
                model="llama2",  # Specify the model you want to use (e.g., llama2)
                prompt=prompt
            )
            
            # Debugging: Print the raw response
            print("Raw response from Ollama:")
            for chunk in response:
                print(chunk)
            
            # Extract the generated text from the response
            generated_text = ""
            for chunk in response:
                if isinstance(chunk, tuple) and chunk[0] == "response":
                    generated_text += chunk[1]
            
            # Return the generated text
            return generated_text.strip()
        
        except Exception as e:
            print(f"An error occurred while generating the post: {e}")
            return "Error: Unable to generate post."