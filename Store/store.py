from bottle import route, run, template, static_file, get, post, delete, request
from sys import argv
import json
import pymysql

connection = pymysql.connect(host = 'localhost', 
user = 'root', 
password = '##', #insert your password 
db = 'store',
charset = 'utf8', 
cursorclass = pymysql.cursors.DictCursor)

@get("/admin")
def admin_portal():
	return template("pages/admin.html")

@get("/")
def index():
    return template("index.html")


#create categories
@post("/category")
def create_category(name):
    new_cat = request.POST.get("name")

    if new_cat = " ":
        return json.dumps({"STATUS":"ERROR", "MSG":"Bad request", "CAT_ID":None, "CODE":400})

    try:
        with connection.cursor() as cursor:
            sql = "SELECT name FROM category"
            cursor.execute(sql)
            categories= cursor.fetchall()

            for cat in categories:
                if new_cat == cat[""]:
                    return json.dumps({"STATUS":"ERROR", "MSG":"category already exists", "CAT_ID":None, "CODE":200})
                
            sql = ("INSERT INTO category VALUES(id, %s)") #add values
            data_add = new_cat
            cursor.execute(sql, data_add)
            new_cat_id = cursor.lastrowid
            connection.commit()
            return json.dumps({"STATUS":"SUCCESS", "MSG":"category created successfully", "CAT_ID":new_cat_id, "CODE":201})

    except:
        return json.dumps({"STATUS":"ERROR", "MSG":"Internal error", "CAT_ID":None, "CODE":500})


#delete categories
@route("/category/<catId>", method='DELETE')
def delete_category(catId):
    try:
        with connection.cursor() as cursor:
            sql = ('DELETE FROM category WHERE id = {}'.format(catId))
            cursor.execute(sql)
            connection.commit()
            return json.dumps({'STATUS':'SUCCESS', 'MSG': 'The category was deleted successfully'})
    
    except:
        return json.dumps({'STATUS':'ERROR', 'MSG': "Internal error"})


#get categorirs 

@get("/categories")
def load_categories():
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM category"
            cursor.execute(sql)
            result = cursor.fetchall()
            return json.dumps({'STATUS' : 'SUCCESS', 'CATEGORIES':result})
    except:
        return json.dumps({'STATUS' : 'ERROR', 'MSG': "Internal error"})


@route('/product/<pid>', method='DELETE')
def delete_product(pid):
    try:
        with connection.cursor() as cursor:
            sql = ('DELETE FROM products WHERE id = {}'.format(pid))
            cursor.execute(sql)
            connection.commit()
            return json.dumps({'STATUS':'SUCCES', 'MSG':'The product was deleted successfully'})
    except:
        return json.dumps({'STATUS' : 'ERROR', 'MSG': "Internal error"})

@get("/products")
def load_products():
    try:
        with connection.cursor() as cursor:
            sql = ('SELECT category, description, price, title, favorite, img_url, id FROM products ')
            cursor.execute(sql)
            result = cursor.fetchall()
            return json.dumps({'STATUS':'SUCCESS','PRODUCTS': result})
    except:
        return json.dumps({'STATUS' : 'ERROR', 'MSG': "Internal error"})


@get("/product/<pid>")
def load_products(pid):
    try:
        with connection.cursor() as cursor:
            sql = ('SELECT category, description, price, title, favorite, img_url, id FROM products')
            cursor.execute(sql)
            result = cursor.fetchall()
            return json.dumps({'STATUS':'SUCCESS','PRODUCTS': result})
    except:
        return json.dumps({'STATUS' : 'ERROR', 'MSG': "Internal error"})



@get('/category/<id>/products')
def list_products_cat(id):
    try:
        with connection.cursor() as cursor:
            sql = ('SELECT category, description, price, title, favorite, img_url, id FROM products WHERE category = {} ORDER BY favorite DESC, creation_date ASC'.format(id) )
            cursor.execute(sql)
            result = cursor.fetchall()
            return json.dumps({'STATUS':'SUCCESS','PRODUCTS': result})
    except:
        return json.dumps({'STATUS':'ERROR', 'MSG': "Internal error"})


@post("/product")
def add_product():

    cat_id = request.POST.get('id')
    category = request.POST.get('category')
    title = request.POST.get('title')
    description = request.POST.get('desc')
    price = request.POST.get('price')
    favorite = request.POST.get('favorite')
    if favorite == None:
        n_fav = 0
    else:
        n_fav = 1
    img_url = request.POST.get('img_url')
    if cat_id != '':
        try:
            with connection.cursor() as cursor:
                sql = ('UPDATE products SET category=%s, title=%s, description=%s, price=%s, favorite=%s, img_url=%s WHERE id=%s')
                data = (category,str(title),str(description),price,n_fav,str(img_url), id)
                cursor.execute(sql, data)
                connection.commit()
                return json.dumps({'STATUS':'SUCCESS', 'MSG':'The product was added/updated successfully'})
        except:
            return json.dumps({'STATUS':'ERROR', 'MSG':"error in the updating"})
    else:
        try:
            with connection.cursor() as cursor:
                sql = 'INSERT INTO products VALUES(id,%s,%s,%s,%s,%s,%s,now())'
                data = (category,title,description,price,n_fav,img_url)
                cursor.execute(sql, data)
                connection.commit()
        except:
            return json.dumps({'STATUS':'ERROR', 'MSG':"error in the values adding"})





@get('/js/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='js')


@get('/css/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='css')


@get('/images/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='images')


run(host='0.0.0.0', port=argv[1])
