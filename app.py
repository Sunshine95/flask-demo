from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    status = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<Item %r>' % self.id

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        item_content = request.form['content']
        new_item = Item(content=item_content)

        try:
            db.session.add(new_item)
            db.session.commit()
            return redirect('/')
        except Exception as inst:            
            return 'Error: Failed to add Item'
    else:
        items = Item.query.order_by(Item.status).all()
        return render_template('index.html', items=items)

@app.route('/delete/<int:id>')
def delete(id):
    item_to_delete = Item.query.get_or_404(id)

    try:
        db.session.delete(item_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'Error: Failed to delete Item'

@app.route('/update/<int:id>')
def update(id):
    item_to_update = Item.query.get_or_404(id)
    new_status = (item_to_update.status + 1) % 3
    item_to_update.status = new_status

    try:
        db.session.commit()
        return redirect('/')
    except Exception as inst:
        print(inst.args)
        print(inst)
        return 'Error: Failed to update Item status'

if __name__ == "__main__":
    app.run(debug=True)

