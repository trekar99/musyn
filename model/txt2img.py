from diffusers import StableDiffusionXLPipeline, AutoencoderTiny
from huggingface_hub import snapshot_download
from torch import float16#, manual_seed
#from random import randint

class ImageGenerator():
  def __init__(self):
    self.model_config_path = self.get_model_config()

    self.vae = AutoencoderTiny.from_pretrained(
                                      'madebyollin/taesdxl',
                                      use_safetensors=True,
                                      torch_dtype=float16,
                                    )
    
    self.pipeline = StableDiffusionXLPipeline.from_single_file("model/models/sdxlturbo.safetensors",
                                                      config=self.model_config_path,
                                                      local_files_only=True,
                                                      revision="fp16",
                                                      variant="fp16",
                                                      torch_dtype=float16,
                                                      vae=self.vae
                                                      )
    
    self.pipeline.set_progress_bar_config(disable=True)

  def get_model_config(self):
    return snapshot_download(
      repo_id="stabilityai/sdxl-turbo",
      allow_patterns=["*.json", "**/*.json", "*.txt", "**/*.txt"],
     local_dir="model/models/config"
    )

  def image_generator(self, prompt, inference="", width=512, height=512):
    #generator = manual_seed(randint(0, 9007199254740991))
    return self.pipeline(prompt=prompt + inference,
                num_inference_steps=1,
                guidance_scale=0.0,
                width=width,
                heigth=heigth
                ).images[0]

  '''pipeline = StableDiffusionXLPipeline.from_single_file("model/models/sdxlturbo.safetensors",
                                                      config=my_local_config_path,
                                                      local_files_only=True,
                                                      revision="fp16",
                                                      variant="fp16",
                                                      torch_dtype=torch.float16)'''
