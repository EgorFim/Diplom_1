class TestBun:

    def test_bun_get_name(self,bun):
        assert bun.name == 'булка'

    def test_bun_get_price(self,bun):
        assert bun.price == 200