########################### INPUT
import pandas as pd
data = pd.read_csv('benchmarks/homo_dump/sample_50/data_NOsmi_50.csv',
                   sep = None,
                   skiprows = 0,
                   header = 0)
target = pd.read_csv('benchmarks/homo_dump/sample_50/homo_50.csv',
                     sep = None,
                     skiprows = 0,
                     header = None)
###########################

########################### OUTPUT
from cheml import initialization
output_directory, log_file, error_file = initialization.output(output_directory = 'ChemML.out',
                                                               logfile = 'log.txt',
                                                               errorfile = 'error.txt')
###########################

########################### MISSING_VALUES
from cheml import preprocessing
missval = preprocessing.missing_values(strategy = 'mean',
                                       string_as_null = True,
                                       inf_as_null = True,
                                       missing_values = False)
data = missval.fit(data)
target = missval.fit(target)
from sklearn.preprocessing import Imputer
imp = Imputer(strategy = 'mean',
              missing_values = 'NaN',
              axis = 0,
              verbose = 0,
              copy = True)
df_columns = data.columns 
data = imp.fit_transform(data)
data = pd.DataFrame(data,columns=df_columns)
df_columns = target.columns 
target = imp.fit_transform(target)
target = pd.DataFrame(target,columns=df_columns)
###########################

