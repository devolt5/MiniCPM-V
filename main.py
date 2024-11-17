import torch
from PIL import Image
from transformers import AutoModel, AutoTokenizer, AutoProcessor

torch.manual_seed(0)

hf_user_token = 'YOUR_TOKEN'

model = AutoModel.from_pretrained('openbmb/MiniCPM-V-2_6', trust_remote_code=True,
    attn_implementation='sdpa', torch_dtype=torch.bfloat16, token=hf_user_token) # sdpa or flash_attention_2, no eager
model = model.eval().cuda()
tokenizer = AutoTokenizer.from_pretrained('openbmb/MiniCPM-V-2_6', trust_remote_code=True, token=hf_user_token)
processor = AutoProcessor.from_pretrained('openbmb/MiniCPM-V-2_6', trust_remote_code=True, token=hf_user_token)

image = Image.open('./assets/transkribus.png').convert('RGB')

# First round chat 
question = "This image shows a paragraph. Tell me the text."
msgs = [{'role': 'user', 'content': [image, question]}]

answer = model.chat(
    processor=processor,
    image=None,
    msgs=msgs,
    tokenizer=tokenizer
)
print(answer)

# Second round chat 
# pass history context of multi-turn conversation
#msgs.append({"role": "assistant", "content": [answer]})
#msgs.append({"role": "user", "content": ["Introduce something about Airbus A380."]})

#answer = model.chat(
#    image=None,
#    msgs=msgs,
#    tokenizer=tokenizer
#)
#print(answer)