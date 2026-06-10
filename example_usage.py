import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Model ID on Hugging Face
model_id = "N11100/deepseek-r1-python-code-ft"

print(f"Loading model: {model_id}...")
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id, 
    torch_dtype=torch.float16, 
    device_map="auto"
)

# Example prompt
prompt = "Explain how to automate a CI/CD pipeline for a Python project."
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

print("Generating response...")
outputs = model.generate(**inputs, max_new_tokens=150)
print("\nResponse:")
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
