import google.generativeai as genai

# Configure with your API key
genai.configure(api_key='AIzaSyCzFUOILnmTKtaaieVYjilZDCJKYrnmh5s') # <-- USE YOUR REAL KEY

# List all available models
print("Available models for your API key:")
for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        print(f"- {model.name}")