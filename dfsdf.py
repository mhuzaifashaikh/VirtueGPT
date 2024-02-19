import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key_here'
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY') or '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'
