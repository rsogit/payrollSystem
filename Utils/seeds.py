import json

data = {'employees': []}
data['employees'].append({
    'id_number': 1,
    'name': 'Raul Oliveira',
    'address': 'Alguma rua da pajucara',
    'type': 'Horista',
    'salary': 45
})
data['employees'].append({
    'id_number': 2,
    'name': 'Relu Cintos',
    'address': 'Abbey st.',
    'type': 'Assalariado',
    'salary': 4500
})
data['employees'].append({
    'id_number': 3,
    'name': 'Bono Vox',
    'address': 'Lá pras Europa',
    'type': 'Comissionado',
    'salary': 4500,
    'percentage': 15
})
data['employees'].append({
    'id_number': 4,
    'name': 'Pelé dos Santos',
    'address': 'Vila belmiro',
    'type': 'Horista',
    'salary': 45
})
data['employees'].append({
    'id_number': 5,
    'name': 'Silvio Luiz',
    'address': 'Sede da Sportv',
    'type': 'Assalariado',
    'salary': 4500
})
data['employees'].append({
    'id_number': 6,
    'name': 'Cesar Menotti',
    'address': 'Minas gerais',
    'type': 'Comissionado',
    'salary': 4500,
    'percentage': 15
})
data['employees'].append({
    'id_number': 7,
    'name': 'Homer Simpsom',
    'address': 'Springfield',
    'type': 'Horista',
    'salary': 45
})
data['employees'].append({
    'id_number': 8,
    'name': 'Alicia Keys',
    'address': 'New York',
    'type': 'Assalariado',
    'salary': 4500
})
data['employees'].append({
    'id_number': 9,
    'name': 'Dante Alighieri',
    'address': 'Inferno',
    'type': 'Comissionado',
    'salary': 4500,
    'percentage': 15
})

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)


