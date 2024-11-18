**A GPT-4V Level MLLM for Single Image, Multi Image and Video on Your Phone**

**Attention**  
This is a customized repo with some adjustements to work in Windows Enviroment.  
**Attention**  

I've made the following changes:

- Update requirements to work seamlessly
- Add `main.py` which is basically the example code but with some bugfixes (including an OCR example in `assets`)
- Added `flash_attn_whl` which contains a build wheel (splitted with tar) for flash_attn installation (which takes > 4 hours of compiling)

## Troubleshooting

### Problem: flash_attn is needed  
Solution: Install flash_attn, but newest version  

### Problem: flash_attn needs pytorch with cuda  
Solution: If you also don't like conda, first, get rid of conda and use venv with:  
`python -m pip uninstall torch`  
`python -m pip cache purge`  
`python -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124`  
Note: This is for CUDA compiler driver 12.4. Adjust to your system wide cuda. Check with `nvcc --version`  

### Problem: Unrecognized configuration class  to build an AutoTokenizer  
Solution: Add huggingface token to tokenizer  

### Problem: "'MiniCPMVTokenizerFast' object has no attribute 'image_processor'"  
Solution: Use AutoProcessor.from_pretrained() and the model itself. Maybe not the optimal performance solution.  
