# SIMPLE SPOTIFY UPGRADE API
# Script by @Pured \\ Nulled.to
# Original Key System from https://github.com/xannyyyy/Hwid-Auth-Verify 
# Donate BTC: 1GB4rLLG71eWqAXe6Dj1ZSpZdFwnFcg6VT
import logging, json
import pymysql.cursors

from flask import Flask, render_template, request

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


app = Flask('')

@app.route('/')
def home():
    return ''

@app.route('/upgrade', methods=['GET'])
def test():  
    
    key = request.args.get('key')
    cn =  request.args.get('cn')
    
    
    
    true = {
     'whitelisted': True,
     'status': 200
    }

    false = {
     'whitelisted': False,
     'status': 401
    }

    
    with connection.cursor() as cursor:
        sql = "SELECT * FROM `key` WHERE `key`=%s"
        cursor.execute(sql, (key))
        result = cursor.fetchone()
        print(result)

    result2 = str(result)

    if key not in result2:
      return json.dumps(false), 401
    else:
        with connection.cursor() as cursor:
            sql = "DELETE FROM `key` WHERE `key`=%s"
            cursor.execute(sql, (key))
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `links` WHERE `cn`=%s ORDER BY `id` ASC"
            cursor.execute(sql, (cn))
            resultZ = cursor.fetchone()
            rows = cursor.fetchall()
            for row in rows:
                sql2 = "DELETE FROM `links` WHERE `id`=%s"
                cursor.execute(sql, (row["id"]))


        return (resultZ)


@app.errorhandler(404) 
def not_found(e): 
    return '404 NOT FOUND', 404

if __name__ == '__main__':
    app.run(
      host="localhost", 
      port=8080,
      debug=True
    )
