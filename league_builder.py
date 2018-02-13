import csv

with open('soccer_players.csv', 'a') as csvfile:
    fieldnames = ['Name','Height','Experience','Guardian Name']
    teachwriter = csv.DictWriter(csvfile,fieldnames=fieldnames)

    teachwriter.writeheader()
    teachwriter.writerow({
        'Name': 'Jonny',
        'Height': 67,
        'Experience': 'YES',
        'Guardian Name': 'Jesse Ventura'
    })