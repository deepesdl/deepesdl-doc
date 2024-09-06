## ddp_init

```python
def ddp_init() -> None 
```

### Description
`ddp_init` initializes the distributed process group for GPU-based distributed training using NCCL (NVIDIA Collective Communications Library). 
It configures the environment to ensure each process operates on its designated GPU.


### Parameters
- (`None`): This method has no input parameters.

### Returns
- `None`: The function does not return any value. It initializes the distributed training process

### Example

```python
ddp_init()  # Initialize distributed environment
model = MyModel()
trainer = Trainer(model=model, ...)
trainer.train()  # Manage distributed training
```

### Notes
- **NCCL Backend**: Optimizes GPU communication in multi-GPU settings, enhancing the speed and efficiency of model training.
- **Environment Configuration**: Automatically sets the CUDA device to the local rank provided by the environment, aligning the process-to-GPU mapping.
- **Usage Scenario**: This function should be called at the beginning of your script to set up the necessary environment for distributed training.
