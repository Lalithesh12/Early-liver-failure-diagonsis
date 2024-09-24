from csv_shuffler import csv_shuffler

shuffler = csv_shuffler.ShuffleCSV(input_file='D:\College\8th semester\project\implementation\dataset\liver_patient2.csv',header=True, batch_size=584)
shuffler.shuffle_csv()
