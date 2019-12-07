class Discount:
    
    def __init__(self):
        print("init discounts")
        self.markdowns = {}
        
    def add_markdown(self, id, pct):
        self.markdowns[id] = pct