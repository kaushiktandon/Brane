import csv
import pandas as pd

def main():
	elsevier_file = 'covid1.csv'
	wos_file = 'COVID-19.csv'

	output_file = 'COVID_COMBINED.csv'

	wos_data = pd.read_csv(wos_file).fillna('')
	else_data = pd.read_csv(elsevier_file).fillna('')
	print(len(wos_data), len(else_data))
	num_deleted = 0
	wos_data['RO'] = ''
	wos_data['URL'] = ''
	wos_data['URL2'] =''
	titles = wos_data['TI'].unique()
	to_delete = []
	for rowidx in range(0, len(else_data)):
		if rowidx % 500 == 0:
			print(rowidx, len(else_data))
		else_row = else_data.iloc[rowidx,:]
		else_ti = else_row['TI']
		if else_ti in titles:
			wos_data.loc[wos_data['TI'] == else_ti,'RO'] = else_row['RO']
			wos_data.loc[wos_data['TI'] == else_ti,'URL'] = else_row['URL']
			wos_data.loc[wos_data['TI'] == else_ti,'URL2'] = else_row['URL2']
			# else_data.drop(rowidx, inplace=True)
			num_deleted = num_deleted + 1
			to_delete.append(rowidx)

	else_data.drop(to_delete, inplace=True)

	else_data['PT'] = 'J'
	else_data['AU'] = ''
	else_data['BA'] = ''
	else_data['BE'] = ''
	else_data['GP'] = ''
	else_data['BF'] = ''
	else_data['CA'] = ''
	else_data['SE'] = ''
	else_data['BS'] = ''
	else_data['LA'] = 'English'
	else_data['DT'] = ''
	else_data['CT'] = ''
	else_data['CY'] = ''
	else_data['CL'] = ''
	else_data['SP'] = ''
	else_data['HO'] = ''
	else_data['ID'] = ''
	else_data['C1'] = ''
	else_data['RP'] = ''
	else_data['EM'] = ''
	else_data['RI'] = ''
	else_data['OI'] = ''
	else_data['FU'] = ''
	else_data['FX'] = ''
	else_data['CR'] = ''
	else_data['TC'] = ''
	else_data['Z9'] = ''
	else_data['U1'] = ''
	else_data['U2'] = ''
	else_data['PU'] = ''
	else_data['PI'] = ''
	else_data['PA'] = ''
	else_data['SN'] = ''
	else_data['EI'] = ''
	else_data['BN'] = ''
	else_data['J9'] = ''
	else_data['JI'] = ''
	else_data['PD'] = ''
	else_data['PN'] = ''
	else_data['SU'] = ''
	else_data['SI'] = ''
	else_data['MA'] = ''
	else_data['AR'] = ''
	else_data['D2'] = ''
	else_data['EA'] = ''
	else_data['PG'] = ''
	else_data['WC'] = ''
	else_data['SC'] = ''
	else_data['GA'] = ''
	else_data['UT'] = ''
	else_data['PM'] = ''
	else_data['HC'] = ''
	else_data['HP'] = ''
	else_data['DA'] = ''

	print(len(wos_data), len(else_data), "deleted=", num_deleted)
	new_data = pd.concat([wos_data, else_data], sort=False)
	print(len(new_data))
	with open(output_file, 'w+', encoding='utf8') as csvfile1:
		writer1 = csv.writer(csvfile1,lineterminator = '\n')
		writer1.writerow(['PT','AU','BA','BE','GP','AF','BF','CA','TI','SO','SE','BS','LA','DT','CT','CY','CL','SP','HO','DE','ID','AB','C1','RP','EM','RI','OI','FU','FX','CR','NR','TC','Z9','U1','U2','PU','PI','PA','SN','EI','BN','J9','JI','PD','PY','VL','IS','PN','SU','SI','MA','BP','EP','AR','DI','D2','EA','PG','WC','SC','GA','UT','PM','OA','HC','HP','DA','URL','RO','URL2'])
		for rowidx in range(len(new_data)):
			row = new_data.iloc[rowidx,:]
			writer1.writerow([row['PT'], row['AU'], row['BA'], row['BE'], row['GP'], row['AF'], row['BF'], row['CA'], row['TI'], row['SO'], row['SE'], row['BS'], row['LA'], row['DT'], row['CT'], row['CY'], row['CL'], row['SP'], row['HO'], row['DE'], row['ID'], row['AB'], row['C1'], row['RP'], row['EM'], row['RI'], row['OI'], row['FU'], row['FX'], row['CR'], row['NR'], row['TC'], row['Z9'], row['U1'], row['U2'], row['PU'], row['PI'], row['PA'], row['SN'], row['EI'], row['BN'], row['J9'], row['JI'], row['PD'], row['PY'], row['VL'], row['IS'], row['PN'], row['SU'], row['SI'], row['MA'], row['BP'], row['EP'], row['AR'], row['DI'], row['D2'], row['EA'], row['PG'], row['WC'], row['SC'], row['GA'], row['UT'], row['PM'], row['OA'], row['HC'], row['HP'], row['DA'], row['URL'], row['RO'], row['URL2']])

if __name__ == '__main__':
	main()