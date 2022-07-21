### TEVdata.py ###
# This file contains helpful classes and data used by the dashboard

# Imports
import numpy
import pandas as pd

# Metadata constants
METASET = 'datasets/metadata/'
AWS_BUCKET = 'https://gbads-metadata.s3.ca-central-1.amazonaws.com/'

METADATA_SOURCES = {
    'FAOSTAT QCL':{
        'METADATA': METASET+'FAOSTAT_QCL.csv',
        'DOWNLOAD': AWS_BUCKET+'20220613_FAOSTAT_QCL.json',
        'PROVENANCE': METASET+'FAOSTAT_QCL_PROVENANCE.txt',
    },
    'FAO FISHSTAT J':{
        'METADATA': METASET+'20220719_FAO_FISHSTATJ.csv',
        'DOWNLOAD': AWS_BUCKET+'20220613_FAOSTAT_QCL.json',
        # 'DOWNLOAD': AWS_BUCKET+'20220719_FAO_FISHSTATJ.json',
        'PROVENANCE': METASET+'FAO_FISHSTATJ_PROVENANCE.txt',
    },
}
METADATA_OTHER = {
    'GLOSSARY':{
        'CSV': METASET+'MetadataGlossary.csv',
    },
}

# TEVdata object
# Used to store data and return manipulated data
class TEVdata():
    def __init__(self, datasource,iso3codes):
        self.ds = datasource
        codes = pd.read_csv(iso3codes)

        # Retrieve and clean data
        self.df = pd.read_csv(self.ds)
        self.df['iso3_code'] = self.df['iso3_code'].str.upper()
        
        # Adding ISO3 column, and converting iso3_code to 'country menu names'
        self.df['ISO3'] = self.df['iso3_code']
        self.df['iso3_code'] = self.df['ISO3'].replace(dict(zip(codes['ISO3'], codes['Menu Name'])))

        self.df.rename(columns={
            'year':'Year',
            'iso3_code':'Country',
            'category':'Species',
            'value':'Value', 
            'type':'Type', 
            'unit':'Currency',
        }, inplace=True)

        self.countries = sorted(self.df['Country'].unique())
        self.types = self.df['Type'].unique()
        self.types = numpy.delete(self.types, numpy.where(self.types == 'Crops'))
        self.species = self.df['Species'].unique()
        self.max_year = int(self.df['Year'].max())
        self.min_year = int(self.df['Year'].min())
    
    def filter_country(self, code, df):
        if code is None or len(code) == 0:
            return df
        if isinstance(code,list):
            return df[df['Country'].isin(code)]
        return df[df['Country']==code]
    
    def filter_type(self, type, df):
        if type is None:
            return df
        return df[df['Type']==type]
    
    def filter_species(self, spec, df):
        if spec is None:
            return df
        return df[df['Species']==spec]
    
    def filter_year(self, year, df):
        if year is None:
            return df
        year = int(year)
        return df[df['Year']==year]
