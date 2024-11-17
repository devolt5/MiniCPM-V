import torch

print(torch.__version__)                     # Expected to show 2.1.2 or similar
print(torch.cuda.is_available())             # Should return True if CUDA is properly configured