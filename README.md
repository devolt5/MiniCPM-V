<div align="center">

<img src="./assets/minicpmv.png" width="300em" ></img> 

**A GPT-4V Level MLLM for Single Image, Multi Image and Video on Your Phone**

  <strong>[中文](./README_zh.md) |
  English</strong>

Join our <a href="docs/wechat.md" target="_blank"> 💬 WeChat</a> | View  MiniCPM-V <a href="docs/best_practice_summary.md" target="_blank"> 📖 best practices</a>


**Attention** This is a customized repo with some adjustements to work in Windows Enviroment.

I've made the following changes:

- Update requirements to work seamlessly
- Add `main.py` which is basically the example code but with some bugfixes (including an OCR example in `assets`)
- Added `flash_attn_whl` which contains a build wheel for flash_attn which took > 4 hours of compiling

## Troubleshooting

Problem: flash_attn is needed
Solution: Install flash_attn, but newest version

---

Problem: flash_attn needs pytorch with cuda
Solution: If you also don't like conda, first, get rid of conda and use venv with:
`python -m pip uninstall torch`
`python -m pip cache purge`
`python -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124`
Note: This is for CUDA compiler driver 12.4. Adjust to your system wide cuda. Check with `nvcc --version`

---

Problem: Unrecognized configuration class  to build an AutoTokenizer
Solution: Add huggingface token to tokenizer

---

Problem: "'MiniCPMVTokenizerFast' object has no attribute 'image_processor'"
Solution: Use AutoProcessor.from_pretrained() and the model itself. Maybe not the optimal performance solution.

<p align="center">
  MiniCPM-V 2.6 <a href="https://huggingface.co/openbmb/MiniCPM-V-2_6">🤗</a> <a href="http://120.92.209.146:8887/">🤖</a> | MiniCPM-Llama3-V 2.5  <a href="https://huggingface.co/openbmb/MiniCPM-Llama3-V-2_5/">🤗</a> <a href="https://huggingface.co/spaces/openbmb/MiniCPM-Llama3-V-2_5">🤖</a> |
  <a href=https://arxiv.org/abs/2408.01800>MiniCPM-Llama3-V 2.5 Technical Report</a> 
</p>

</div>


**MiniCPM-V** is a series of end-side multimodal LLMs (MLLMs) designed for vision-language understanding. The models take image, video and text as inputs and provide high-quality text outputs. Since February 2024, we have released 5 versions of the model, aiming to achieve **strong performance and efficient deployment**. The most notable models in this series currently include:

- **MiniCPM-V 2.6**: 🔥🔥🔥 The latest and most capable model in the MiniCPM-V series. With a total of 8B parameters, the model **surpasses GPT-4V in single image, multi-image and video understanding**. It outperforms **GPT-4o mini, Gemini 1.5 Pro and Claude 3.5 Sonnet** in single image understanding, and advances MiniCPM-Llama3-V 2.5's features such as strong OCR capability, trustworthy behavior, multilingual support, and end-side deployment. Due to its superior token density, MiniCPM-V 2.6 can for the first time support real-time video understanding on end-side devices such as iPad.

- **MiniCPM-V 2.0**: The lightest model in the MiniCPM-V series. With 2B parameters, it surpasses larger models such as Yi-VL 34B, CogVLM-Chat 17B, and Qwen-VL-Chat 10B in overall performance. It can accept image inputs of any aspect ratio and up to 1.8 million pixels (e.g., 1344x1344), achieving comparable performance with Gemini Pro in understanding scene-text and matches GPT-4V in low hallucination rates.

