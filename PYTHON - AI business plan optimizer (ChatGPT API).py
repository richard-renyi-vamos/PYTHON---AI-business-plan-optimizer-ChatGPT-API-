import openai

def optimize_business_plan(api_key, business_plan_text):
    """Sends the business plan to ChatGPT and retrieves optimization recommendations."""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert business consultant. Provide actionable recommendations to optimize the given business plan."},
            {"role": "user", "content": business_plan_text}
        ]
    )
    return response["choices"][0]["message"]["content"]

def main():
    api_key = "your_openai_api_key_here"
    openai.api_key = api_key
    
    print("Enter your business plan (or provide a file path):")
    input_option = input("Type 'text' to enter manually or 'file' to upload a document: ").strip().lower()
    
    if input_option == 'file':
        file_path = input("Enter the file path: ").strip()
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                business_plan_text = file.read()
        except Exception as e:
            print(f"Error reading file: {e}")
            return
    else:
        print("Enter your business plan (press Enter twice when done):")
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
        business_plan_text = "\n".join(lines)
    
    print("Analyzing and optimizing your business plan...\n")
    recommendations = optimize_business_plan(api_key, business_plan_text)
    print("Optimization Recommendations:")
    print(recommendations)

if __name__ == "__main__":
    main()
