from flask import Flask, render_template, request
from openai import OpenAI
import os

app = Flask(__name__)
client = OpenAI()
client.api_key = os.environ.get('OPENAI_API_KEY')

@app.route("/", methods=['GET', 'POST'])
def home():
    paragraphs = []  # Initialize paragraphs as an empty list
    if request.method == 'POST':
        user_content = request.form['user_input']
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful islamic bot created by Huzaifa Shaikh where users\
                  enter certain problems they are facing in life and you give them a comfoting message and a relvant \
                 hadeeth (with source) and an ayah from the quran that can relate to the passage, ressaure and make \
                 them feel better THAT'S IT YOU ARE NOT MADE FOR ANYTHING ELSE. if the prompt does not make sense, or \
                 is not a valid concern, dont asnwer it at all and give an appropriate response and say try again.\
                 "},
                {"role": "user", "content": user_content}  
            ]
        )
        ai_response = response.choices[0].message.content
        # Split the AI response into paragraphs
        paragraphs = ai_response.split('\n')
    return render_template('index.html', paragraphs=paragraphs)

# if __name__ == '__main__':
#     app.run(debug=True)