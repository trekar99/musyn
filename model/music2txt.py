from model.bart import BartCaptionModel
from torch import load
import config

class MusicCapsGenerator(BartCaptionModel):
  def __init__(self, max_length=128):
    super().__init__(max_length)

    self.pretrained_object = load(config.musiccaps_model, map_location='cpu')
    self.state_dict = self.pretrained_object['state_dict']
    self.load_state_dict(self.state_dict)

    self.eval()

# Print model's state_dict
#print("Model's state_dict:")
#for param_tensor in model.state_dict():
#    print(param_tensor, "\t", model.state_dict()[param_tensor].size())
