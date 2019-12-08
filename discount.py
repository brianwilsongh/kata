class Discount:
    
    def __init__(self):
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
        
    def add_weighted(self, id, price, threshold, limit, pct):
        self.weighted[id] = {
            'price': price,
            'threshold': threshold,
            'pct': pct,
            'limit': limit,
            'times_used': 0
        }
    
    def get_markdown(self, id):
        return self.markdowns.get(id)
    
    def get_volume_markdown(self, id):
        return self.volume_markdowns.get(id)
    
    def get_quantified(self, id):
        return self.quantified.get(id)
        
    def get_weighted(self, id):
        return self.weighted.get(id)
    
    def delete_weighted(self, id):
        self.weighted.pop(id)
        
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
    
    def apply_weighted(self, memo, id, price):
        
        for idx, discount in enumerate(memo['active_discounts']):
            if discount['times_used'] >= discount['limit']:
                self.delete_weighted(discount['id'])
                memo['active_discounts'].remove(discount)
            else:
                if price <= discount['price']:
                    multiplier = (100 - discount['pct'])/100
                    price = round(multiplier * price, 2)
                    discount['times_used'] = discount['times_used'] + 1  
        if not memo['items'].get(id):
            memo['items'][id] = 1
        else:
            memo['items'][id] = memo['items'][id] + 1    
        weighted_disc = self.get_weighted(id)
        if weighted_disc and memo['items'][id] == weighted_disc['threshold']:
            weighted_disc['id'] = id
            memo['active_discounts'].append(weighted_disc)
        #still need to sort the active discounts, descending
        return (memo, price)