class PlatformAdapter:
    def adapt_post(self, post, platform):
        if platform == 'Twitter':
            # Ensure the post is within Twitter's 280-character limit
            return post[:280]
        elif platform == 'Instagram':
            # Add Instagram-specific formatting (e.g., line breaks, hashtags)
            return post + "\n\nFollow us for more updates! 🚀 #InstaAI"
        else:
            return post