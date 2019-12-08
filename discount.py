class Discount:
    
    def __init__(self):
        print("init discounts")
        self.markdowns = {}
        self.volume_markdowns = {}
        self.quantified = {}
        
    def add_markdown(self, id, pct):
        self.markdowns[id] = pct
    
    def add_volume_markdown(self, id, threshold, pct):
        self.volume_markdowns[id] = {
            'pct': pct,
            'threshold': threshold
        }
    
    def add_quantified(self, id, quant, price):
        self.quantified[id] = {
            'quant': quant,
            'price': price
        } 
    
    def get_markdown(self, id):
        return self.markdowns.get(id)
    
    def get_volume_markdown(self, id):
        return self.volume_markdowns.get(id)
    
    def get_quantified(self, id):
        return self.quantified.get(id)
        
    def apply_markdown_price(self, id, price):
        this_markdown = self.get_markdown(id)
        if this_markdown:
            multiplier = (100 - this_markdown)/100
            return round(multiplier * price, 2)
        return price
    
    def apply_volume_markdown_price(self, id, price):
        this_vol_markdown = self.get_volume_markdown(id)
        if this_vol_markdown:
            current_threshold = this_vol_markdown['threshold']
            if current_threshold >= 1:
                this_vol_markdown['threshold'] = current_threshold - 1
            else:
                multiplier = (100 - this_vol_markdown['pct'])/100
                return round(multiplier * price, 2)
        return price
    
    def apply_quantified(self, id, trans_quant):
        this_quant = self.get_quantified(id)
        if this_quant:
            if trans_quant >= this_quant['quant']:
                new_quant = trans_quant - this_quant['quant']
                return (this_quant['price'], new_quant)
        return None