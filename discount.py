class Discount:
    
    def __init__(self):
        print("init discounts")
        self.markdowns = {}
        self.volume_markdowns = {}
        self.quantified = {}
        self.weighted = {}
        
    def add_markdown(self, id, pct):
        self.markdowns[id] = pct
    
    def add_volume_markdown(self, id, threshold, pct):
        self.volume_markdowns[id] = {
            'pct': pct,
            'threshold': threshold
        }
    
    def add_quantified(self, id, quant, price, limit=None):
        self.quantified[id] = {
            'quant': quant,
            'price': price,
            'limit': limit
        } 
        
    def add_weighted(self, id, threshold, limit):
        self.weighted[id] = {
            'threshold': threshold,
            'limit': limit
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
        disc_limit = trans_quant + 1
        if this_quant:
            if this_quant.get('limit'):
                disc_limit = this_quant['limit']
            disc_applications = 0
            while trans_quant >= this_quant['quant'] and disc_applications < disc_limit:
                trans_quant -= this_quant['quant']
                disc_applications += 1
            return (this_quant['price'] * disc_applications, trans_quant)
        return None