class InvoiceItem:
    def __init__(self,id,desc,qty,unitPrice):
        self.id = str(id)
        self.desc = str(desc)
        self.qty = int(qty)
        self.unitPrice = float(unitPrice)

    def getID(self):
        return self.id

    def getDesc(self):
        return self.desc

    def getQty (self):
        return self.qty

    def setQty (self, amt):
        self.qty = amt

    def getUnitPrice(self):
        return self.unitPrice

    def setUnitPrice(self, amt):
        self.unitPrice = amt

    def getTotal(self):
        return self.unitPrice*self.qty

    def toString(self):
        return "InvoiceItem[id= {0}, desc= {1}, qty= {2}, unitPrice= {3}]".format(self.id,self.desc,self.qty,self.unitPrice)

