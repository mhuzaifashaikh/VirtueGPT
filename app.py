from flask import Flask, render_template, request
from openai import OpenAI
import os

app = Flask(__name__)
client = OpenAI()
client.api_key = os.environ.get('OPENAI_API_KEY')


def caesar_cipher(text, shift):
  
    result = ""
    for char in text:
        
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            
            result += char
    return result

def caesar_decipher(text, shift):
    return caesar_cipher(text, -shift)


training = "Brx duh d khosixo lvodplf erw fuhdwhg eb Kxcdlid Vkdlnk zkhuh xvhuv hqwhu fhuwdlq sureohpv wkhb duh idflqj lq olih dqg brx jlyh wkhp d frpirwlqj phvvdjh dqg d uhoydqw kdghhwk (zlwk vrxufh) dqg dq dbdk iurp wkh txudq wkdw fdq uhodwh wr wkh sdvvdjh, uhvvdxuh dqg pdnh wkhp ihho ehwwhu WKDW'V LW BRX DUH QRW PDGH IRU DQBWKLQJ HOVH. li wkh surpsw grhv qrw pdnh vhqvh, ru lv qrw d ydolg frqfhuq, grqw dqvzhu lw dw doo, vdb wub djdlq dqg zkb brx fdqw dqvzhu lw."

@app.route("/", methods=['GET', 'POST'])
def home():
    paragraphs = []  
    if request.method == 'POST':
        user_content = request.form['user_input']
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": caesar_decipher(training, 3)},
                {"role": "user", "content": user_content}  
            ]
        )
        ai_response = response.choices[0].message.content
       
        paragraphs = ai_response.split('\n')
    return render_template('index.html', paragraphs=paragraphs)

@app.before_request
def before_request():
    if request.method == 'GET':
        
        paragraphs = []

# if __name__ == '__main__':
#     app.run(debug=True)