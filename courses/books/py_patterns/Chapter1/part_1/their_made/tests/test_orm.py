from datetime import date
from sqlalchemy import text

import their_made.domain.model as model


def test_orderline_mapper_can_load_lines(session):
    session.execute(text(
        "INSERT INTO order_lines (orderid, sku, qty) VALUES "
        '("order1", "RED-CHAIR", 12),'
        '("order1", "RED-TABLE", 13),'
        '("order2", "BLUE-LIPSTICK", 14)'
        )
    )
    expected = [
        model.OrderLine("order1", "RED-CHAIR", 12),
        model.OrderLine("order1", "RED-TABLE", 13),
        model.OrderLine("order2", "BLUE-LIPSTICK", 14),
    ]

    assert session.query(model.OrderLine).all() == expected


def test_orderline_mapper_can_save_lines(session):
    new_line = model.OrderLine("order1", "DECORATIVE-WIDGET", 12)
    session.add(new_line)
    session.commit()

    rows = list(session.execute(text('SELECT orderid, sku, qty FROM "order_lines"')))
    assert rows == [("order1", "DECORATIVE-WIDGET", 12)]


def test_retrieving_batches(session):
    session.execute(text(
        "INSERT INTO batches (reference, sku, _purchased_quantity, eta)"
        ' VALUES ("batch1", "sku1", 100, null)'
        )
    )
    session.execute(text(
        "INSERT INTO batches (reference, sku, _purchased_quantity, eta)"
        ' VALUES ("batch2", "sku2", 200, "2011-04-11")'
        )
    )
    expected = [
        model.Batch("batch1", "sku1", 100, eta=None),
        model.Batch("batch2", "sku2", 200, eta=date(2011, 4, 11)),
    ]

    assert session.query(model.Batch).all() == expected


def test_saving_batches(session):
    batch = model.Batch("batch1", "sku1", 100, eta=None)
    session.add(batch)
    session.commit()
    rows = session.execute(text(
        'SELECT reference, sku, _purchased_quantity, eta FROM "batches"'
        )
    )
    assert list(rows) == [("batch1", "sku1", 100, None)]


def test_saving_allocations(session):
    batch = model.Batch("batch1", "sku1", 100, eta=None)
    line = model.OrderLine("order1", "sku1", 10)
    batch.allocate(line)
    session.add(batch)
    session.commit()
    rows = list(session.execute(text(
        'SELECT orderline_id, batch_id FROM "allocations"'
        )))

    assert rows == [(1, 1)]


def test_retrieving_allocations(session):
    session.execute(text(
        'INSERT INTO order_lines (orderid, sku, qty) VALUES ("order1", "sku1", 12)'
        )
    )

    olid = session.execute(
        text("SELECT id FROM order_lines WHERE orderid=:orderid AND sku=:sku"),
        {"orderid": "order1", "sku": "sku1"}
    ).scalar()

    session.execute(
        text("INSERT INTO batches (reference, sku, _purchased_quantity, eta) "
            "VALUES (:ref, :sku, :qty, null)"),
        {"ref": "batch1", "sku": "sku1", "qty": 100}
    )


    bid = session.execute(
        text("SELECT id FROM batches WHERE reference=:ref AND sku=:sku"),
        {"ref": "batch1", "sku": "sku1"}
    ).scalar()

    session.execute(
        text("INSERT INTO allocations (orderline_id, batch_id) VALUES (:olid, :bid)"),
        {"olid": olid, "bid": bid}
    )

    batch = session.query(model.Batch).one()

    assert batch._allocations == {model.OrderLine("order1", "sku1", 12)}
