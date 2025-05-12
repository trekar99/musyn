title = "Musyn"

web_title = "# Musyn - Music Synesthesia in Real-Time"

description = """
  Musyn: Real-time Music-to-Image Co-creation System
  To use it, simply upload your audio and click 'submit', or click one of the examples to load them. Read more at the links below. 
  """

examples = [
            ["Brasilian Beach, Rio de Janeiro"], 
            ["Gnawa Village, Morocco"],
            ["Cyberpunk, Future"],
            ["Fairy Tales, Forest"]
          ]

css = """ 
      #container{
          margin: 0 auto;
          max-width: 80rem;
      } 
      #intro{
          max-width: 100%;
          text-align: center;
          margin: 0 auto;
      }"""

# Models Path
musiccaps_model = 'model/models/lpmusiccaps.pth'
sdxlturbo_model = 'model/models/sdxlturbo.safetensors'

# Aspect Ratio
width = [512, 1024, 1080, 1920]
height = [512, 1024, 1080, 1920]
