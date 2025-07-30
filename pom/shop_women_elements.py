class ShopWomen:

    def __init__(self, page):
        celebrating_beauty_header = page.get_by_role("paragraph").filter(has_text="Celebrating Beauty and Style")