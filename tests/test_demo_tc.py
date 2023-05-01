def test_tc1():
    from ..py_tenma_app import TenmaPs
    app_obj = TenmaPs()
    assert app_obj.demo_method()
