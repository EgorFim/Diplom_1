class TestBun:

    def test_bun_get_name(self,bun):
        assert bun.get_name() == 'булка'

    def test_bun_get_price(self,bun):
        assert bun.get_price() == 200