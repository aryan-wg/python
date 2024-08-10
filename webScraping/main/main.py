import re
from bs4 import BeautifulSoup

ITEM_HTML = '''<html><head></head><body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
            </div>
                <p class="star-rating Three">
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                </p>
            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
            <div class="product_price">
        <p class="price_color" item_name = "this is the item name" >$51.77</p>
<p class="instock availability">
    <i class="icon-ok"></i>

        In stock

</p>
    <form>
        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
    </form>
            </div>
    </article>
</li>

</body></html>
'''


soup = BeautifulSoup(ITEM_HTML, 'html.parser')

def get_price ():
    locator = "article p.price_color" # tag (space) tag_inside .class_of_tag #id_of_that_tag
    item = soup.select_one(locator)
    price = item.string
    reg_ex = '$([0-9]+\.[0-9]+)'
    print(re.search('\$([0-9]+\.[0-9]+)',price)) # regex to match
    print(item.string)#gives the internal string
    print(item.contents)# gives the content inside the tags as an array
    print(item.attrs["item_name"]) #attributes

get_price()