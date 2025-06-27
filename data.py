import generators


class Url:
    MAIN_URL = 'https://qa-scooter.praktikum-services.ru/' # Main url Yandex Scooter
    CREATE_COURIER = 'api/v1/courier' # Courier account creation handle
    COURIER_LOGIN = 'api/v1/courier/login' # Courier login handle
    COURIER_DELETE = 'api/v1/courier' # Courier Delete handle
    CREATE_ORDER = 'api/v1/orders' # Courier creation handle
    ORDER_CANCEL = 'api/v1/orders/cancel?track=' # Get order list handle
    TRACK_ORDER = 'api/v1/orders/track?t=' # Track order handle

class DataForOrder:
    order_data = {
        "firstName": "Nadezhda",
        "LastName": "Planidina",
        "address": "Vosstaniya 17",
        "metroStation": 3,
        "phone": "+79165558825",
        "rentTime": 3,
        "deliveryTime": "2024-11-03",
        "comment": "Call me before deliver"
    }
    scooter_color = [['BLACK'], ['GREY'], (['BLACK'], ['GREY']), ['']]


class DataForRegistration:
    reg_data = [
        {'login': generators.login_generator(), 'password': generators.password_generator(), 'first_name': generators.name_generator()}
    ]

class ResponseBody:
    COURIER_CREATION_SUCCESS = {'ok': True}
    COURIER_NAME_ALREADY_EXIST = {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}
    COURIER_REGISTRATION_NOT_ENOUGH_DATA = {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}
    COURIER_ACCOUNT_NOT_FOUND = {'code': 404, 'message': 'Учетная запись не найдена'}
    COURIER_LOGIN_NOT_ENOUGH_DATA = {'code': 400, 'message': 'Недостаточно данных для входа'}

class Flags:
    SUCCESSFUL_ORDER_CREATION = 'track' #Successful order creation flag
    SUCCESSFUL_GET_ORDER_LIST = 'orders'
