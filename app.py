from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def translate():
    if request.method == 'POST':
        source_text = request.form['source_text']
        source_lang = request.form['source_lang']
        target_lang = request.form['target_lang']
        
        translation = get_translation(source_text, source_lang, target_lang)
        
        return render_template('index.html', translation=translation)
    
    return render_template('index.html')

def get_translation(text, source_lang, target_lang):
    url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl={source_lang}&tl={target_lang}&dt=t&q={text}"
    response = requests.get(url)
    translation = response.json()[0][0][0]
    return translation

if __name__ == '__main__':
    app.run(debug=True)
