import datetime
from flask_appbuilder import Model
from flask import Markup
from sqlalchemy import Column, Date, ForeignKey, Integer, String, Table, Text, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base

#metadata = MetaData()
#Base = declarative_base(metadata=metadata)
#from app.db import Base, metadata
from . import db
metadata = MetaData(bind=db.engine)
#db.Model.metadata.reflect(bind=db.engine,schema='clutch')
Base = automap_base()
Base.prepare(db.engine, reflect=True)

#class Person(Model):
##    __bind_key__ = 'person'
#    __table__ = Table('person',
#                      metadata,
##                      Column('id', Integer, primary_key=True),
#                      extend_existing=True,
#                      autoload=True)
#    def __repr__(self):
#        return str(self.id)
#        
        
class JobTitle(Model):
#    __bind_key__ = 'person'
    __table__ = Table('job_title',
                      metadata,
#                      Column('id', Integer, primary_key=True),
                      extend_existing=True,
                      autoload=True)
    def __repr__(self):
        return str(self.description)
        
class Language(Model):
#    __bind_key__ = 'person'
    __table__ = Table('language',
                      metadata,
#                      Column('id', Integer, primary_key=True),
                      extend_existing=True,
                      autoload=True)
    def __repr__(self):
        return str(self.description)
    
    
class Suffix(Model):
#    __bind_key__ = 'person'
    __table__ = Table('suffix',
                      metadata,
#                      Column('id', Integer, primary_key=True),
                      extend_existing=True,
                      autoload=True)
    def __repr__(self):
        return str(self.description)
        
        
class IdentityType(Model):
#    __bind_key__ = 'person'
    __table__ = Table('identity_type',
                      metadata,
#                      Column('id', Integer, primary_key=True),
                      extend_existing=True,
                      autoload=True)
    def __repr__(self):
        return str(self.description)
        
        
        
class MaritalStatus(Model):
#    __bind_key__ = 'person'
    __table__ = Table('marital_status',
                      metadata,
#                      Column('id', Integer, primary_key=True),
                      extend_existing=True,
                      autoload=True)
    def __repr__(self):
        return str(self.description)
        
        
class Title(Model):
#    __bind_key__ = 'person'
    __table__ = Table('title',
                      metadata,
#                      Column('id', Integer, primary_key=True),
                      extend_existing=True,
                      autoload=True)
    def __repr__(self):
        return str(self.description)
        
        
class PersonNote(Model):
#    __bind_key__ = 'person'
    __table__ = Table('person_note',
                      metadata,
#                      Column('id', Integer, primary_key=True),
                      extend_existing=True,
                      autoload=True)
    def __repr__(self):
        return str(self.note_text)
        
        
class Sex(Model):
#    __bind_key__ = 'person'
    __table__ = Table('sex',
                      metadata,
#                      Column('id', Integer, primary_key=True),
                      extend_existing=True,
                      autoload=True)
    def __repr__(self):
        return str(self.description)
        
        
class Race(Model):
#    __bind_key__ = 'person'
    __table__ = Table('race',
                      metadata,
#                      Column('id', Integer, primary_key=True),
                      extend_existing=True,
                      autoload=True)
    def __repr__(self):
        return str(self.description)
        
        
class Ethnicity(Model):
#    __bind_key__ = 'person'
    __table__ = Table('ethnicity',
                      metadata,
#                      Column('id', Integer, primary_key=True),
                      extend_existing=True,
                      autoload=True)
    def __repr__(self):
        return str(self.description)
        
        
class PersonNotification(Model):
#    __bind_key__ = 'person'
    __table__ = Table('person_notification',
                      metadata,
#                      Column('id', Integer, primary_key=True),
                      extend_existing=True,
                      autoload=True)
    def __repr__(self):
        return str(self.id)
        
        
class NotificationType(Model):
#    __bind_key__ = 'person'
    __table__ = Table('notification_type',
                      metadata,
#                      Column('id', Integer, primary_key=True),
                      extend_existing=True,
                      autoload=True)
    def __repr__(self):
        return str(self.description)
        
        
class PersonHash(Model):
#    __bind_key__ = 'person'
    __table__ = Table('person_hash',
                      metadata,
#                      Column('id', Integer, primary_key=True),
                      extend_existing=True,
                      autoload=True)
    def __repr__(self):
        return str(self.id)
        
        
class ClutchMember(Model):
#    __bind_key__ = 'person'
    __table__ = Table('clutch_member',
                      metadata,
#                      Column('id', Integer, primary_key=True),
#                      Column('person_id'),
#                      Column('fraxses_user_code', 
#                      Column('member_code', 
#                      Column('dependancy_member_code', 
#                      Column('clutch_member_type_id', 
#                      Column('clutch_member_relationship_type_id', 
#                      Column('start_date', 'end_date', 
#                      Column('clutch_member_status_id', 
#                      Column('terms_accept_date', 
#                      Column('phone_verification', 
#                      Column('email_verification', 
#                      Column('receive_push_notifications', 
#                      Column('receive_sms_notifications', 
#                      Column('receive_email_notifications', 
#                      Column('total_points', 
#                      Column('total_spend'
                      extend_existing=True,
                      autoload=True)
    def __repr__(self):
        return str(self.person_id)
        
        
class ClutchMemberType(Model):
#    __bind_key__ = 'person'
    __table__ = Table('clutch_member_type',
                      metadata,
#                      Column('id', Integer, primary_key=True),
                      extend_existing=True,
                      autoload=True)
    def __repr__(self):
        return str(self.description)
        
        
class ClutchMemberStatus(Model):
#    __bind_key__ = 'person'
    __table__ = Table('clutch_member_status',
                      metadata,
#                      Column('id', Integer, primary_key=True),
                      extend_existing=True,
                      autoload=True)
    def __repr__(self):
        return str(self.description)
        
        
class ClutchMemberRelationshipType(Model):
#    __bind_key__ = 'person'
    __table__ = Table('clutch_member_relationship_type',
                      metadata,
#                      Column('id', Integer, primary_key=True),
                      extend_existing=True,
                      autoload=True)
    def __repr__(self):
        return str(self.description)
        
        
class Address(Model):
#    __bind_key__ = 'person'
    __table__ = Table('address',
                      metadata,
#                      Column('id', Integer, primary_key=True),
                      extend_existing=True,
                      autoload=True)
    def __repr__(self):
        return Markup(self.address_line1 + ' ' + self.unit_number + ' ' + str(self.city_id) + ', ' + str(self.state))
        
        
class State(Model):
#    __bind_key__ = 'person'
    __table__ = Table('state',
                      metadata,
#                      Column('id', Integer, primary_key=True),
                      extend_existing=True,
                      autoload=True)
    def __repr__(self):
        return str(self.name)
        
        
class City(Model):
#    __bind_key__ = 'person'
    __table__ = Table('city',
                      metadata,
#                      Column('id', Integer, primary_key=True),
                      extend_existing=True,
                      autoload=True)
    def __repr__(self):
        return str(self.name)
        
        
class Country(Model):
#    __bind_key__ = 'person'
    __table__ = Table('country',
                      metadata,
#                      Column('id', Integer, primary_key=True),
                      extend_existing=True,
                      autoload=True)
    def __repr__(self):
        return str(self.country)
        
        
class CountyFips(Model):
#    __bind_key__ = 'person'
    __table__ = Table('county_fips',
                      metadata,
#                      Column('id', Integer, primary_key=True),
                      extend_existing=True,
                      autoload=True)
    def __repr__(self):
        return str(self.place_name)
        
        
class PersonAddress(Model):
#    __bind_key__ = 'person'
    __table__ = Table('person_address',
                      metadata,
#                      Column('id', Integer, primary_key=True),
                      extend_existing=True,
                      autoload=True)
    def __repr__(self):
        return str(self.address_id)
        
        
class AddressType(Model):
#    __bind_key__ = 'person'
    __table__ = Table('address_type',
                      metadata,
#                      Column('id', Integer, primary_key=True),
                      extend_existing=True,
                      autoload=True)
    def __repr__(self):
        return str(self.description)
        
        
class PharmacyAddress(Model):
#    __bind_key__ = 'person'
    __table__ = Table('pharmacy_address',
                      metadata,
#                      Column('id', Integer, primary_key=True),
                      extend_existing=True,
                      autoload=True)
    def __repr__(self):
        return str(self.address_id)
        
        
#class Prescription(Model):
##    __bind_key__ = 'person'
#    __table__ = Table('prescription',
#                      metadata,
##                      Column('id', Integer, primary_key=True),
#                      extend_existing=True,
#                      autoload=True)
#    def __repr__(self):
#        return str(self.id)
#        
        
class PrescriptionStatus(Model):
#    __bind_key__ = 'person'
    __table__ = Table('prescription_status',
                      metadata,
#                      Column('id', Integer, primary_key=True),
                      extend_existing=True,
                      autoload=True)
    def __repr__(self):
        return str(self.description)
        
        
class PrescriptionPharmacyPrices(Model):
#    __bind_key__ = 'person'
    __table__ = Table('prescription_pharmacy_prices',
                      metadata,
#                      Column('id', Integer, primary_key=True),
                      extend_existing=True,
                      autoload=True)
    def __repr__(self):
        return str(self.price)
        
        
class ApiPricesChangeHealth(Model):
#    __bind_key__ = 'person'
    __table__ = Table('api_prices_change_health',
                      metadata,
#                      Column('id', Integer, primary_key=True),
                      extend_existing=True,
                      autoload=True)
    def __repr__(self):
        return str(self.prescription_id)
        
class UnitOfMeasure(Model):
#    __bind_key__ = 'person'
    __table__ = Table('unit_of_measure',
                      metadata,
#                      Column('id', Integer, primary_key=True),
                      extend_existing=True,
                      autoload=True)
    def __repr__(self):
        return str(self.description)
        
        
class Drug(Model):
#    __bind_key__ = 'person'
    __table__ = Table('drug',
                      metadata,
#                      Column('id', Integer, primary_key=True),
                      extend_existing=True,
                      autoload=True)
    def __repr__(self):
        return str(self.drug_name)
        
        
#class PharmacyDrug(Model):
#    __bind_key__ = 'person'
#    __table__ = Table('pharmacy_drug',
#                      metadata,
#                      Column('id', Integer, primary_key=True),
#                      extend_existing=True,
#                      autoload=True)
#    def __repr__(self):
#        return str(self.id)
        
        
#class OrphanedPrescription(Model):
##    __bind_key__ = 'person'
#    __table__ = Table('orphaned_prescription',
#                      metadata,
##                      Column('id', Integer, primary_key=True),
#                      extend_existing=True,
#                      autoload=True)
#    def __repr__(self):
#        return str(self.id)
        
#class Prescriber(Model):
##    __bind_key__ = 'person'
#    __table__ = Table('prescriber',
#                      metadata,
##                      Column('id', Integer, primary_key=True),
#                      extend_existing=True,
#                      autoload=True)
#    def __repr__(self):
#        return str(self.id)
#        
        
class Pharmacy(Model):
#    __bind_key__ = 'person'
    __table__ = Table('pharmacy',
                      metadata,
#                      Column('id', Integer, primary_key=True),
                      extend_existing=True,
                      autoload=True)
    def __repr__(self):
        return str(self.name)
        
        
class PharmacyGroup(Model):
#    __bind_key__ = 'person'
    __table__ = Table('pharmacy_group',
                      metadata,
#                      Column('id', Integer, primary_key=True),
                      extend_existing=True,
                      autoload=True)
    def __repr__(self):
        return str(self.group_name)
        
        
class PharmacyMember(Model):
#    __bind_key__ = 'person'
    __table__ = Table('pharmacy_member',
                      metadata,
#                      Column('id', Integer, primary_key=True),
                      extend_existing=True,
                      autoload=True)
    def __repr__(self):
        return str(self.person_id)
        
        
class NfiItg(Model):
#    __bind_key__ = 'person'
    __table__ = Table('nfi_itg',
                      metadata,
#                      Column('id', Integer, primary_key=True),
                      extend_existing=True,
                      autoload=True)
    def __repr__(self):
        return str(self.id)
        
class NfiItgTrgReq(Model):
#    __bind_key__ = 'person'
    __table__ = Table('nfi_itg_trg_req',
                      metadata,
#                      Column('id', Integer, primary_key=True),
                      extend_existing=True,
                      autoload=True)
    def __repr__(self):
        return str(self.id)
        
           
        
class Person(Model):
#    __bind_key__ = 'person'
    __table__ = Table('person',
                      metadata,
                      Column('id', Integer, primary_key=True, autoincrement=True),
                      Column('title_id', Integer, ForeignKey('title.id')),
                      Column('sex_id', Integer, ForeignKey('sex.id')),
                      Column('suffix_id', Integer, ForeignKey('suffix.id')),
                      Column('race_id', Integer, ForeignKey('race.id')),
                      Column('ethnicity_id', Integer, ForeignKey('ethnicity.id')),
                      Column('marital_status_id', Integer, ForeignKey('marital_status.id')),
                      Column('identity_type_id', Integer, ForeignKey('identity_type.id')),
                      Column('job_title_id', Integer, ForeignKey('job_title.id')),
                      Column('language_id', Integer, ForeignKey('language.id')),
#                      Column('person_address_id', Integer, ForeignKey('person_address.id')),
                      extend_existing=True,
                      autoload=True)
    title = relationship("Title", primaryjoin='Person.title_id==Title.id', backref="person")                  
    sex = relationship("Sex", primaryjoin='Person.sex_id==Sex.id', backref="person")
    suffix = relationship("Suffix", primaryjoin='Person.suffix_id==Suffix.id', backref="person")
    race = relationship("Race", primaryjoin='Person.race_id==Race.id', backref="person")
    ethnicity = relationship("Ethnicity", primaryjoin='Person.ethnicity_id==Ethnicity.id', backref="person")
    marital_status = relationship("MaritalStatus", primaryjoin='Person.marital_status_id==MaritalStatus.id', backref="person")
    identity_type = relationship("IdentityType", primaryjoin='Person.identity_type_id==IdentityType.id', backref="person")
    job_title = relationship("JobTitle", primaryjoin='Person.job_title_id==JobTitle.id', backref="person")
    language = relationship("Language", primaryjoin='Person.language_id==Language.id', backref="person")
    person_address = relationship("PersonAddress", primaryjoin='Person.id==PersonAddress.person_id', backref="person")
                      
    def __repr__(self):
        return Markup(self.first_name + ' ' + self.last_name + ' ' + str(self.date_of_birth))
        
        
class Prescriber(Model):
#    __bind_key__ = 'person'
    __table__ = Table('prescriber',
                      metadata,
                      Column('id', Integer, primary_key=True),
                      Column('person_id', Integer, ForeignKey('person.id')),
                      extend_existing=True,
                      autoload=True)
    person = relationship("Person", primaryjoin='Prescriber.person_id==Person.id', backref="prescriber")
    
    def __repr__(self):
        return str(self.state_license_number)
        

        
class Prescription(Model):
#    __bind_key__ = 'person'
    __table__ = Table('prescription',
                      metadata,
                      Column('id', Integer, primary_key=True),
                      Column('prescriber_id', Integer, ForeignKey('prescriber.id')),
                      Column('drug_id', Integer, ForeignKey('drug.id')),
                      Column('person_id', Integer, ForeignKey('person.id')),  
                      Column('prescription_status_id', Integer, ForeignKey('prescription_status.id')),
                      Column('quantity_unit_of_measure_id', Integer, ForeignKey('unit_of_measure.id')),
                      extend_existing=True,
                      autoload=True)
    prescriber = relationship("Prescriber", primaryjoin='Prescription.prescriber_id==Prescriber.id', backref="prescription")
    drug = relationship("Drug", primaryjoin='Prescription.drug_id==Drug.id', backref="prescription")
    person = relationship("Person", primaryjoin='Prescription.person_id==Person.id', backref="prescription")                      
    prescription_status = relationship("PrescriptionStatus", primaryjoin='Prescription.prescription_status_id==PrescriptionStatus.id', backref="prescription")
    unit_of_measure = relationship("UnitOfMeasure", primaryjoin='Prescription.quantity_unit_of_measure_id==UnitOfMeasure.id', backref="prescription")
    prescription_pharmacy_prices = relationship("PrescriptionPharmacyPrices", primaryjoin='Prescription.id==PrescriptionPharmacyPrices.prescription_id', backref="prescription")
    
    def __repr__(self):
        return str(self.id)
      
      
class OrphanedPrescription(Model):
#    __bind_key__ = 'person'
    __table__ = Table('orphaned_prescription',
                      metadata,
                      Column('id', Integer, primary_key=True),
                      Column('prescriber_id', Integer, ForeignKey('prescriber.id')),
                      Column('drug_id', Integer, ForeignKey('drug.id')),
                      extend_existing=True,
                      autoload=True)
    prescriber = relationship("Prescriber", primaryjoin='OrphanedPrescription.prescriber_id==Prescriber.id', backref="orphaned_prescription")
    drug = relationship("Drug", primaryjoin='OrphanedPrescription.drug_id==Drug.id', backref="orphaned_prescription")
    
    def __repr__(self):
        return str(self.id)
        
