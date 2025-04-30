from diffusers import StableDiffusionXLPipeline, AutoencoderKL
from huggingface_hub import snapshot_download
from torch import float16, manual_seed

# TODO download
#from diffusers import AutoencoderKL
'''vae = AutoencoderKL.from_pretrained(
  'madebyollin/sdxl-vae-fp16-fix',
  use_safetensors=True,
  torch_dtype=torch.float16,
).to('cuda')'''

class ImageGenerator():
  def __init__(self):
    self.model_config_path = self.get_model_config()

    self.pipeline = StableDiffusionXLPipeline.from_single_file("model/models/sdxlturbo.safetensors",
                                                      config=self.model_config_path,
                                                      local_files_only=True,
                                                      revision="fp16",
                                                      variant="fp16",
                                                      torch_dtype=float16)
    self.pipeline.set_progress_bar_config(disable=True)

  def get_model_config(self):
    return snapshot_download(
      repo_id="stabilityai/sdxl-turbo",
      allow_patterns=["*.json", "**/*.json", "*.txt", "**/*.txt"],
     local_dir="model/models/config"
    )

  def image_generator(self, prompt, seed = 123123123, inference=""):
    generator =  manual_seed(seed)
    return self.pipeline(prompt=prompt + inference,
                num_inference_steps=1,
                guidance_scale=0.0,
                generator=generator
                ).images[0]

  '''pipeline = StableDiffusionXLPipeline.from_single_file("model/models/sdxlturbo.safetensors",
                                                      config=my_local_config_path,
                                                      local_files_only=True,
                                                      revision="fp16",
                                                      variant="fp16",
                                                      torch_dtype=torch.float16)'''
