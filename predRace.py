from ethnicolr import census_ln, pred_census_ln
import pandas as pd
import numpy as np

paperdf = pd.read_csv('paper1.csv')
authordf = pd.read_csv('author1.csv')
matchdf = pd.read_csv('matching1.csv')
print(authordf)
rdf2000 = census_ln(authordf, 'lname', 2000)
rdf2000['year'] = 2000
rdf2010 = census_ln(authordf, 'lname', 2010)
rdf2010['year'] = 2010
rdf = pd.concat([rdf2000, rdf2010])
rdf.head(20)
