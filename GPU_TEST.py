import torch

torch.cuda.empty_cache()

print(torch.cuda.is_available())
print(torch.cuda.get_device_name())
print(torch.cuda.memory_summary(device=None, abbreviated=False))
print(torch.cuda.memory_stats())
