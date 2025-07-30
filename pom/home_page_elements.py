class HomePage:

    def __init__(self, page):
        self.celebrate_header = page.get_by_role("paragraph").filter(has_text="Celebrating Beauty and Style")
        self.celebrate_body = page.get_by_role("paragraph").filter(has_text="playwright-practice was")