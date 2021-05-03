from flask import Flask, redirect, render_template, url_for, flash
from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
import urllib
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField


params = urllib.parse.quote_plus("DRIVER= {ODBC Driver 17 for SQL Server};SERVER={63.33.44.172};DATABASE={glue};UID={heida};PWD={Krullusnura.NOX}")

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
db = SQLAlchemy(app)


class MetaTable(db.Model):

    project = db.Column(db.String(800))
    start = db.Column(db.String(800))
    end = db.Column(db.String(32))
    nox_technology = db.Column(db.String(32))
    investigators = db.Column(db.String(32))
    locations = db.Column(db.Integer)
    purpose = db.Column(db.String(800))
    contact = db.Column(db.String(800))
    bill_to_client = db.Column(db.String(800))
    ship_to_address = db.Column(db.String(800))
    transport_cost_to_site = db.Column(db.String(800))
    required_shipment_arrival_date = db.Column(db.String(800))
    investigator_name = db.Column(db.String(800))
    investigator_email_and_phone_number = db.Column(db.String(800))
    contacts_for_RMA_support= db.Column(db.String(800))
    priority_of_RMA_replacements = db.Column(db.String(800))
    number_of_studies = db.Column(db.String(800))
    duration_of_study_end_date_of_contract = db.Column(db.String(800))
    payment_terms = db.Column(db.String(800))
    data_access = db.Column(db.String(5))
    price_list_for_damaged_units = db.Column(db.String(800))
    full_BOM_quantities = db.Column(db.String(800))
    firmware_versions = db.Column(db.String(800))
    noxturnal_version = db.Column(db.String(800))
    payment_type = db.Column(db.String(800))
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)

    def __init__(self, project, start, end, nox_technology, investigators, locations, purpose, contact, bill_to_client, ship_to_address, transport_cost_to_site, required_shipment_arrival_date, investigator_name, investigator_email_and_phone_number, contacts_for_RMA_support, priority_of_RMA_replacements, number_of_studies, duration_of_study_end_date_of_contract, payment_terms, data_access, price_list_for_damaged_units, full_BOM_quantities, firmware_versions, noxturnal_version, payment_type):
        self.project = project
        self.start = start
        self.end = end
        self.nox_technology = nox_technology
        self.investigators = investigators
        self.locations = locations
        self.purpose = purpose
        self.contact = contact
        self.bill_to_client = bill_to_client
        self.ship_to_address = ship_to_address
        self.transport_cost_to_site = transport_cost_to_site
        self.required_shipment_arrival_date = required_shipment_arrival_date
        self.investigator_name= investigator_name
        self.investigator_email_and_phone_number= investigator_email_and_phone_number
        self.contacts_for_RMA_support = contacts_for_RMA_support
        self.priority_of_RMA_replacements = priority_of_RMA_replacements
        self.number_of_studies= number_of_studies
        self.duration_of_study_end_date_of_contract = duration_of_study_end_date_of_contract
        self.payment_terms= payment_terms
        self.data_access = data_access
        self.price_list_for_damaged_units= price_list_for_damaged_units
        self.full_BOM_quantities= full_BOM_quantities
        self.firmware_versions = firmware_versions
        self.noxturnal_version= noxturnal_version
        self.payment_type= payment_type
        #self.id= id



class ReusableForm(Form):
    project = TextField('Project:', validators=[validators.DataRequired()])
    start =  TextField('start')
    end = TextField('end')
    nox_technology = TextField('nox_technology')
    investigators = TextField('investigators')
    locations = TextField('locations')
    purpose = TextField('purpose')
    contact = TextField('contact')
    bill_to_client = TextField('bill-to-client')
    ship_to_address = TextField('ship-to-address')
    transport_cost_to_site = TextField('transport_cost_to_site')
    required_shipment_arrival_date = TextField('required_shipment_arrival_date')
    investigator_name= TextField('investigator_name')
    investigator_email_and_phone_number= TextField('investigator_email_and_phone_number')
    contacts_for_RMA_support= TextField('contacts_for_RMA_support')
    priority_of_RMA_replacements= TextField('priority_of_RMA_replacements')
    number_of_studies= TextField('number_of_studies')
    duration_of_study_end_date_of_contract = TextField('duration_of_study-end_date_of_contract')
    payment_terms= TextField('payment_terms')
    data_access = TextField('data_access')
    price_list_for_damaged_units= TextField('price_list_for_damaged_units')
    full_BOM_quantities= TextField('full_BOM_quantities')
    firmware_versions = TextField('firmware_versions')
    noxturnal_version= TextField('noxturnal_version')
    payment_type= TextField('payment_type')
    #id= TextField('id')

    @app.route("/metaTable", methods=['GET', 'POST'])
    def hello():
        form = ReusableForm(request.form)

        if request.method == 'POST': 
            project = request.form['project']
            start = request.form['start']
            end = request.form['end']
            nox_technology = request.form['nox_technology']
            investigators = request.form['investigators']
            locations= request.form['locations']
            purpose= request.form['purpose']
            contact = request.form['contact']
            bill_to_client = request.form['bill-to-client']
            ship_to_address = request.form['ship-to-address']
            transport_cost_to_site = request.form['transport_cost_to_site']
            required_shipment_arrival_date = request.form['required_shipment_arrival_date']
            investigator_name= request.form['investigator_name']
            investigator_email_and_phone_number= request.form['investigator_email_and_phone_number']
            contacts_for_RMA_support= request.form['contacts_for_RMA_support']
            priority_of_RMA_replacements= request.form['priority_of_RMA_replacements']      
            number_of_studies= request.form['number_of_studies']
            duration_of_study_end_date_of_contract = request.form['duration_of_study-end_date_of_contract']
            payment_terms= request.form['payment_terms']
            data_access = request.form['data_access']
            price_list_for_damaged_units= request.form['price_list_for_damaged_units']
            full_BOM_quantities= request.form['full_BOM_quantities']
            firmware_versions = request.form['firmware_versions']
            noxturnal_version= request.form['noxturnal_version']
            payment_type= request.form['payment_type']

        if form.validate(): 
            metaTable = MetaTable(project, start, end, nox_technology, investigators, locations, purpose, contact, bill_to_client, ship_to_address, transport_cost_to_site, required_shipment_arrival_date, investigator_name, investigator_email_and_phone_number, contacts_for_RMA_support, priority_of_RMA_replacements, number_of_studies, duration_of_study_end_date_of_contract, payment_terms, data_access, price_list_for_damaged_units, full_BOM_quantities, firmware_versions, noxturnal_version, payment_type)
            db.session.add(metaTable)
            db.session.commit()
            db.session.close()
            flash('Takk fyrir '+ project + ' skráð')
        else:
            flash('Error: Uppfyllir ekki skilyrði ')
            db.session.rollback()

            db.session.close()
        return render_template('main_page.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)