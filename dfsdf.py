import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key_here'
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY') or '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'
