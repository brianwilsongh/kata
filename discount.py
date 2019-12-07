class Discount:
    
    def __init__(self):
        print("init discounts")
        self.markdowns = {}
        
    def add_markdown(self, id, pct):
        self.markdowns[id] = pct
    
    def get_markdown(self, id):
        return self.markdowns.get(id)
        
    def apply_markdown_price(self, id, price):
        this_markdown = self.get_markdown(id)
        if this_markdown:
            multiplier = (100 - self.get_markdown(id))/100
            return round(multiplier * price, 2)
        else:
            return price