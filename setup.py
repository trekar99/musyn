from setuptools import setup

setup(
    name="musyn",
    install_requires=[
        'librosa >= 0.8',
        'torchaudio_augmentations==0.2.1', # for augmentation
        'numpy',
        'pandas',
        'einops',
        'scikit-learn',
        'wandb',
        'jupyter',
        'matplotlib',
        'omegaconf',
        'astropy',
        'transformers==4.26.1',
        'openai',
        'python-dotenv',
        'tqdm',
        'nltk==3.8.1',
        'evaluate==0.4.0',
        'bert_score==0.3.13',
        'rouge_score==0.1.2',
        'gradio',
        'peft==0.10.0',
        'diffusers==0.30'
    ]
)
