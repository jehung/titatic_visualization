import csv

file = 'titanic_data.csv'

def read_data(file):
    dir = 'C:\\Users\\Jenny\\Documents\\Mathfreak_Data\\School\\Data_Analysis_ND\\Project6\\'
    
    with open('titanic_final.csv', 'wb') as f_out:
        out_colnames = ['Outcome', 'Passenger Class', 'Sex', 'Age', 'Embarked']

        writer = csv.DictWriter(f_out, fieldnames = out_colnames)
        writer.writeheader()
        
        with open(dir+file, 'r') as f_in:
            reader = csv.DictReader(f_in)
        
            for row in reader:
                new_point = {}
                if row['Survived'] == '1':
                    new_point['Outcome'] = 'Survived'
                else:
                    new_point['Outcome'] = 'Perished'
                    
                if row['Pclass'] == '1':
                    new_point['Passenger Class'] = 'Class 1'
                elif row['Pclass'] == '2':
                    new_point['Passenger Class'] = 'Class 2'
                else:
                    new_point['Passenger Class'] = 'Class 3'
    

                if row['Sex'] == 'male':
                    new_point['Sex'] = 'Male'
                else:
                    new_point['Sex'] = 'Female'


                if row['Age'] == '':
                    new_point['Age'] = 'Unknown'
                elif float(row['Age']) < 12:
                    new_point['Age'] = 'Age < 12'
                elif float(row['Age']) >= 12 and float(row['Age']) < 30:
                    new_point['Age'] = 'Age 12 - 29'
                elif float(row['Age']) >= 30 and float(row['Age']) < 50:
                    new_point['Age'] = 'Age 30 - 49'
                elif float(row['Age']) >= 50:
                    new_point['Age'] = 'Age > 50'

                    
                if row['Embarked'] == 'C':
                    new_point['Embarked'] = 'Cherbourg'
                elif row['Embarked'] == 'Q':
                    new_point['Embarked'] = 'Queenstown'
                else:
                    new_point['Embarked'] = 'Southampton'
                    
                writer.writerow(new_point)
        
read_data(file)