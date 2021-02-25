from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# This needs to be rebuilt in order to import from app.config

SQLALCHEMY_DATABASE_URI = CLUTCH_PBM_URI = 'postgresql+psycopg2://{database_user}:{database_password}@{database_host}:{database_port}/{database_db}?options=-csearch_path%3Dclutch'.format(
    database_user='clutch', database_password='Intenda#01', database_host='clutch-pgr-svc-headless', database_port='5432', database_db='clutch')
    
engine = create_engine(CLUTCH_PBM_URI, convert_unicode=True)

metadata = MetaData(bind=engine)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
#Base = declarative_base()
Base = automap_base()
#Base.metadata.reflect(engine)
Base.prepare(engine, reflect=True)