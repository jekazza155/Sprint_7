class Endpoints:
    create_courier = "/api/v1/courier"
    login_courier = "/api/v1/courier/login"
    create_order = "/api/v1/orders"
    delete_courier = '/api/v1/courier/'
    get__number_courier_orders = '/api/v1/courier/:id/ordersCount'
    finish_order = '/api/v1/orders/finish/'
    cancel_order = '/api/v1/orders/cancel'
    get_orders_list = '/api/v1/orders'
    accept_order_by_number = '/api/v1/orders/track'
    accept_order = '/api/v1/orders/accept/:id'
