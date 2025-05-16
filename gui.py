from flask import Flask, render_template, request
from kotprog import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')
        extensions = request.form.get('extensions')
        from_path = request.form.get('from')
        to_path = request.form.get('to')

        print("Kezdő dátum:", start_date)
        print("Végdátum:", end_date)
        print("Kiterjesztések:", extensions)
        print("Letöltések mappa:", from_path)
        print("Cél mappa:", to_path)

        start_datee = None
        if start_date !='':
            split_start_date = start_date.split('-')
            if len(split_start_date)>0:
                start_datee=Date(int(split_start_date[0]), int(split_start_date[1]), int(split_start_date[2]))
        end_datee = None
        if end_date !='':
            split_end_date = end_date.split('-')
            if len(split_end_date)>0:
                end_datee=Date(int(split_end_date[0]), int(split_end_date[1]), int(split_end_date[2]))
        split_extensions = extensions.split(',')
        for i in range(len(split_extensions)):
            split_extensions[i]=split_extensions[i].strip()
        print("----------------------------", split_extensions)

        list_downloads(from_path, start_datee, end_datee)
        folder_maker(to_path, split_extensions)
        files_copy(files, to_path, from_path, split_extensions)

        return f"<p>Adatok megérkeztek!</p><a href='/'>Vissza</a>"

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)