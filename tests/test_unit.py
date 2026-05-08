from payment.main import Order

def test_order_total_calculation():

    order = Order(
        product_id="1",
        price=100,
        fee=20,
        total=120,
        quantity=1,
        status="pending"
    )

    assert order.total == 120
    assert order.fee == 20
    assert order.status == "pending"