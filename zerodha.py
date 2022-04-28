from jugaad_trader import Zerodha

kite = Zerodha()
 
# Set access token loads the stored session.
# Name chosen to keep it compatible with kiteconnect.
kite.set_access_token()

# Get profile
profile = kite.profile()

# Finally placing an order

for i in range(100):
    order_id = kite.place_order(variety=kite.VARIETY_REGULAR,
                                tradingsymbol="",
                                exchange=kite.EXCHANGE_BSE,
                                transaction_type=kite.TRANSACTION_TYPE_BUY,
                                quantity=20,
                                order_type=kite.ORDER_TYPE_LIMIT,
                                price=0.02,
                                product=kite.PRODUCT_CNC,
                                validity=kite.VALIDITY_DAY)

    order_id = kite.place_order(variety=kite.VARIETY_REGULAR,
                                tradingsymbol="",
                                exchange=kite.EXCHANGE_BSE,
                                transaction_type=kite.TRANSACTION_TYPE_BUY,
                                quantity=20,
                                order_type=kite.ORDER_TYPE_LIMIT,
                                price=0.02,
                                product=kite.PRODUCT_CNC,
                                validity=kite.VALIDITY_DAY)
    order_id = kite.place_order(variety=kite.VARIETY_REGULAR,
                                tradingsymbol="",
                                exchange=kite.EXCHANGE_BSE,
                                transaction_type=kite.TRANSACTION_TYPE_BUY,
                                quantity=20,
                                order_type=kite.ORDER_TYPE_LIMIT,
                                price=0.02,
                                product=kite.PRODUCT_CNC,
                                validity=kite.VALIDITY_DAY)
    order_id = kite.place_order(variety=kite.VARIETY_REGULAR,
                                tradingsymbol="",
                                exchange=kite.EXCHANGE_BSE,
                                transaction_type=kite.TRANSACTION_TYPE_BUY,
                                quantity=20,
                                order_type=kite.ORDER_TYPE_LIMIT,
                                price=0.02,
                                product=kite.PRODUCT_CNC,
                                validity=kite.VALIDITY_DAY)
    order_id = kite.place_order(variety=kite.VARIETY_REGULAR,
                                tradingsymbol="",
                                exchange=kite.EXCHANGE_BSE,
                                transaction_type=kite.TRANSACTION_TYPE_BUY,
                                quantity=20,
                                order_type=kite.ORDER_TYPE_LIMIT,
                                price=0.1,
                                product=kite.PRODUCT_CNC,
                                validity=kite.VALIDITY_DAY)
    order_id = kite.place_order(variety=kite.VARIETY_REGULAR,
                                tradingsymbol="",
                                exchange=kite.EXCHANGE_BSE,
                                transaction_type=kite.TRANSACTION_TYPE_BUY,
                                quantity=20,
                                order_type=kite.ORDER_TYPE_LIMIT,
                                price=0.03,
                                product=kite.PRODUCT_CNC,
                                validity=kite.VALIDITY_DAY)
    order_id = kite.place_order(variety=kite.VARIETY_REGULAR,
                                tradingsymbol="",
                                exchange=kite.EXCHANGE_BSE,
                                transaction_type=kite.TRANSACTION_TYPE_BUY,
                                quantity=20,
                                order_type=kite.ORDER_TYPE_LIMIT,
                                price=0.03,
                                product=kite.PRODUCT_CNC,
                                validity=kite.VALIDITY_DAY)
    order_id = kite.place_order(variety=kite.VARIETY_REGULAR,
                                tradingsymbol="",
                                exchange=kite.EXCHANGE_BSE,
                                transaction_type=kite.TRANSACTION_TYPE_BUY,
                                quantity=20,
                                order_type=kite.ORDER_TYPE_LIMIT,
                                price=0.02,
                                product=kite.PRODUCT_CNC,
                                validity=kite.VALIDITY_DAY)
    order_id = kite.place_order(variety=kite.VARIETY_REGULAR,
                                tradingsymbol="",
                                exchange=kite.EXCHANGE_BSE,
                                transaction_type=kite.TRANSACTION_TYPE_BUY,
                                quantity=20,
                                order_type=kite.ORDER_TYPE_LIMIT,
                                price=0.02,
                                product=kite.PRODUCT_CNC,
                                validity=kite.VALIDITY_DAY)
# Fetch all orders
kite.orders()
