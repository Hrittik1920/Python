import pandas
from seaborn import load_dataset
df = load_dataset('penguins')
df['bill_length_cm'] = [ i/100 for i in df['bill_length_mm'] ]
df['bill_depth_cm'] = [ i/100 for i in df['bill_depth_mm'] ]
df['flipper_length_cm'] = [ i/100 for i in
df['flipper_length_mm'] ]
df['bmi'] = [
(df['body_mass_g'][i]/1000)/(df['bill_depth_cm'][i]*df['bill_depth_cm'][i]) for i in range(len(df['bill_depth_cm']))]
print(df.head())