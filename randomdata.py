import sqlite3
from random import randint
from random import choice


def date():
    randyear=randint(0,22)
    if randyear<10:
        return f'{randint(1, 12)}/{randint(1, 31)}/0{randint(0, 9)}'
    else:
        return f'{randint(1,12)}/{randint(1,31)}/{randint(10,22)}'

def state():
    states = ['Lagos', 'FCT(ABUJA)', 'Anambra', 'Ogun', 'Rivers', 'Delta']
    # states=['Ekiti', 'Enugu', 'Gombe', 'Imo', 'Jigawa', 'Kaduna', 'Kano']
    return states[randint(0,5)]

def address():
    places=('somewhere','someplace','test','sample address','magboro','under the skies','just a place','under the canopy','nigeria','airport')
    return choice(places)

def email():
    emails = [
        'egbudomraphael@gmail.com',
        'major@gmail.com',
        'minor@gmail.com',
        'test'
    ]
    return choice(emails)

def crime():
    crimes = [
        'Aggravated Assault', 'Aiding and Abetting', 'Arson',
        'Assault / Battery', 'Attempted murder', 'Bribery', 'Burglary', 'Child Abuse',
        'Child Pornography', 'Computer Crime', 'Conspiracy', 'Credit / Debit Card Fraud', 'Criminal Contempt of Court',
        'Cyberbullying', 'Domestic Violence', 'Disorderly Conduct', 'Disturbing the Peace', 'Drug Possession',
        'Drug Trafficking', 'Drug Manufacturing', 'Extortion', 'Forgery', 'Fraud', 'Harassment',
        'Homicide', 'Identity Theft', 'Indecent Exposure', 'Insurance Fraud', 'Kidnapping', 'Manslaughter',
        'Money Laundering', 'Murder',
        'Perjury', 'Probation Violation', 'Prostitution', 'Public Intoxication', 'Pyramid Schemes', 'Rape', 'Robbery',
        'Racketeering / RICO', 'Securities Fraud', 'Sexual Assault', 'Shoplifting', 'Solicitation', 'Stalking',
        'Statutory Rape', 'Theft', 'Vandalism', 'Wire Fraud'
    ]
    return choice(crimes)

def description():
    from random import randint
    names = ["We", "I", "They", "He", "She", "Jack", "Jim"]
    verbs = ["was", "is", "are", "were"]
    nouns = ["commiting a crime", "watching a crime", "reporting crime", "dancing with the devil", "speaking to a thief"]
    while True:
        return names[randint(0, len(names) - 1)] + " " + verbs[randint(0, len(verbs) - 1)] + " " + nouns[
            randint(0, len(nouns) - 1)]
        break

def status():
    s=['PENDING','INVESTIGATING','CONCLUDED']
    return choice(s)

def evidence():
    pics=['statistical (1).png','statistical.png','barChart.png','chart.png','admin.png','history.png','submit.png',
          'startup.png','helping-hand.png','inspection.png']
    with open(choice(pics), 'rb') as f:
        m = f.read()
    return m

conn = sqlite3.connect("user_data2.db")
cursor = conn.cursor()
for i in range(28):
    stmt = "INSERT INTO crime_data(date,state,address,crime,description,email,evidence,status) VALUES(?, ?, ?, ?, ?, ?, ?, ?)"
    entries = [(date(),state(),address(),crime(),description(),email(),evidence(),status())]
    cursor.executemany(stmt, entries)
conn.commit()
conn.close()