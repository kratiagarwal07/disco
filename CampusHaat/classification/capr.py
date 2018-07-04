class BaseResponse:

    def __init__(self, StatusCode,Message):
        self.StatusCode=StatusCode
        self.Message=Message


    def StatusCode(self):
        return self.StatusCode

    def Message(self):
        return self.Message
e=BaseResponse(10,'Hello')
array3={"message":e.Message,"statuscode":e.StatusCode}
#print(array3)

class Category:
    Category_list = []

    def __init__(self, CategoryName, CategoryId):
        self.CategoryName = CategoryName
        self.CategoryId = CategoryId
        self.__class__.Category_list.append(self)




    def CategoryName(self):
        return self.CategoryName
    def CategoryId(self):
        return self.CategoryId

d = Category('bike', 90)
d1 = Category('bike', 900)
d3=Category('motor',98)


#print('Category name is %s and CategoryId is %s' %(d.CategoryName, d.CategoryId))
array1 = {"CategoryId": d.CategoryId,"CategoryName":d.CategoryName}
Categoryarray={"category":array1}
#print(Categoryarray)

class Product:
    Product_list = []
    def __init__(self,ProductTitle,ProductId,ProductParent):
        self.ProductTitle=ProductTitle
        self.ProductId=ProductId
        self.ProductParent=ProductParent
        self.__class__.Product_list.append(self)


    def ProductTitle(self):
        return self.ProductTitle
    def ProductId(self):
        return self.ProductId
    def ProductParent(self):
        return self.ProductParent
    def setProductTitle(title):
         self.ProductTitle=title
    def setProductId(id):
         self.ProductId=id
    def setProductParent(parent):
         self.ProductParent=parent

'''
textdetection=class_testing.textDetection
c = Product(textdetection.title,textdetection.result_id,'cycle')
c1=Product('pp',00,'py')
products=[]

#c = Product('ladybi',1,'cyc')
#print('Product Title is %s and Product Id is %s and Product Parent is %s'%(c.ProductTitle,c.ProductId,c.ProductParent))
#array1={"CategoryId":[d.CategoryId],"CategoryName":[d.CategoryName]}
prodarray2 = {"ProductId": c.ProductId,"ProductTitle":c.ProductTitle,"ParentProduct":c.ProductParent}
prodarray3 = {"ProductId": c1.ProductId,"ProductTitle":c1.ProductTitle,"ParentProduct":c1.ProductParent}
products.append(prodarray2)
products.append(prodarray3)
#print(product)

#print(prodarray2)
#Productarray={"product":prodarray2}
Productarray={"product":products}
productlist=[]
productlist.append(prodarray2)
productlist.append(prodarray3)
#Categoryarray={"category":array1,"product":productlist}
#productlist.append(Categoryarray)
#productlist.append(Productarray)
#productlist.append(products)
#print(productlist)

#Categoryarray={"category":array1,"product":productlist}
#finalarray={"baseresponse": array3,"productlist":productlist}
#productList={"category":Categoryarray}
productList={"category": array1,"products":productlist}

#productList={"category":array1,"product":productList}
#finalarray={"baseresponse": array3,"productlist":[productList]}
#print(productList)


#print(Productarray)
print(finalarray)
'''
