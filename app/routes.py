from flask import request, redirect, render_template, flash, url_for
from . import db
from .models import URL
from flask import current_app as app

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['original_url']

        existing_url = URL.query.filter_by(original_url=original_url).first()
        if existing_url:
            short_url = request.host_url + existing_url.short_id 
            return render_template('index.html', short_url=short_url)

        short_id = URL.generate_short_id()
        while URL.query.filter_by(short_id=short_id).first():
            short_id = URL.generate_short_id()
        
        new_url = URL(original_url=original_url, short_id=short_id)
        db.session.add(new_url)
        db.session.commit()

        short_url = request.host_url + short_id
        return render_template('index.html',short_url=short_url)
    
    return render_template('index.html')

@app.route('/<short_id>')
def redirect_url(short_id):
    link = URL.query.filter_by(short_id=short_id).first_or_404()
    return redirect(link.original_url)

        