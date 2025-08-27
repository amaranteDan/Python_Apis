from services.car_api import CarApi

car_api = CarApi()


carros = car_api.get_cars()
print(f'Tdos os carros: {carros}')

new_car_data = {
    "marca": "Fiat",
    "modelo": "Marea",
    "ano": 1999,
    "combustivel": "Gasolina",
    "portas": 4,
    "preco": 90000
}
new_car = car_api.create_car(new_car_data)
print(f'Novo carro criado: {new_car}')

car = car_api.get_car_by_id(new_car['id'])
print(f'Carro buscado por ID: {car}')

updated_car_data = {
    "marca": "Fiat",
    "modelo": "Marea Turbo",
    "ano": 2001,
    "combustivel": "Gasolina",
    "portas": 4,
    "preco": 95000
}
updated_car = car_api.update_car(new_car['id'], updated_car_data)
print(f'Carro atualizado: {updated_car}')   

deleted_car = car_api.delete_car(new_car['id'])
print(f'Carro deletado: {deleted_car}')     
