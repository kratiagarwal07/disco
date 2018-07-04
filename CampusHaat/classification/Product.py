
class Product:
    Product_list = []
    def __init__(self,ProductTitle,ProductId,ProductParent):
        self.ProductTitle=ProductTitle
        self.ProductId=ProductId
        self.__class__.Product_list.append(self)


    def ProductTitle(self):
        return self.ProductTitle
    def ProductId(self):
        return self.ProductId
    def ProductParent(self):
        return self.ProductParent
    def setProductTitle(self,title):
         self.ProductTitle=title
    def setProductId(self,id):
         self.ProductId=id
    def setProductParent(self,parent):
         self.ProductParent=parent



#print('Product Title is %s and Product Id is %s and Product Parent is %s'%(c.ProductTitle,c.ProductId,c.ProductParent))
#for prod in Product.Product_list:
    #print(prod.ProductTitle)
   # print(cat.CategoryId)