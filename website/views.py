from flask import Blueprint, render_template, request,redirect, url_for
from .models import Incidents_stage1, TEST
from . import db
 

views = Blueprint('views',__name__)

@views.route('/')
def home():
  return render_template("home.html")


@views.route('/incidents')
def incidents():
  test = TEST.query.all()
  return test

@views.route('/all')
def index():
    # Retrieve a list of incidents from the database
    #incidents = db.session.query(Incidents_stage1).all()
    incidents = Incidents_stage1.query.all()
    print('hrehrhehr')
    return incidents
    #return render_template('index.html', incidents=incidents)
@views.route('/test', methods=['GET', 'POST'])
def create_test():
    if request.method == 'POST':
        CHECK = request.form
        print(CHECK)
        NAME = request.form.get('name')
        DESCRIPTION = request.form.get('description')
        #data = request.get_json()        
        print(NAME,'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')

        # Create a new incident based on user input
        new_incident = TEST(
            name=NAME,
            description=DESCRIPTION
            # ... (populate other fields)
        )
        db.session.add(new_incident)
        db.session.commit()
        return render_template("incidents_s1.html")
    return render_template("incidents_s1.html", mimetype="application/json")

@views.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        
        print('hrehrhehrhehrh')
        # Create a new incident based on user input
        new_incident = Incidents_stage1(
            # Extract data from the form fields
            COMPANY_CODE=request.form.get('COMPANY_CODE'),
            I_OPZONE_CODE=request.form.get('I_OPZONE_CODE'),
            I_STATUS=request.form.get('I_STATUS'),
            REGION_CODE=request.form.get('REGION_CODE'),
            SCHEME_CODE=request.form.get('SCHEME_CODE'),
            SEQ=request.form.get('SEQ'),
            YEAR_YR=request.form.get('YEAR_YR')
            # ... (populate other fields)
        )
        db.session.add(new_incident)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create.html')

@views.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    incident = Incidents_stage1.query.get(id)
    if request.method == 'POST':
        # Update the incident based on user input
        incident.COMPANY_CODE = request.form.get('COMPANY_CODE')
        incident.I_OPZONE_CODE = request.form.get('I_OPZONE_CODE')
        # ... (update other fields)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', incident=incident)

@views.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    incident = Incidents_stage1.query.get(id)
    db.session.delete(incident)
    db.session.commit()
    return redirect(url_for('index'))
