"""
write a function called linear_search_product that takes the list of products and a target product
name as input. the function should perform a linear search too find the target product in the list and
return a list of indices of call occurrences of the product if found ,or na empty list if the product is not 
found.
"""


def                 linearSearchProduct      (productList,targetProduct):
   indices=[]

   for index,product in      numerate(productlist) :
     if product== targetproduct:
       indices.append(index)

     return indices


    # example usage:
   products =["shoes","boot",          "loafer","shoes","sandal","shoes"]
   target="shoes"
   target2='apple'
   result=                              linearSearchProduct(products,        target)
   print (result)