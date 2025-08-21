from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import mysql.connector


db_config = {
    "host" : "localhost",
    "user": "root",
    "password": "12345678",
    "database": "students",
     "port": 3306
}

def __init__db():
    #to create a database of student if there is not an databases.
    connect = mysql.connector.connect(**db_config)
    #connect the sql object
    cursor = connect.cursor()
    #data tables format of student_details\
    cursor.execute('''create table if not exists students_details(
                        student_id int auto_increment primary key,
                        student_name varchar(100) not null,
                        student_number bigint not null,
                        student_email text not null, 
                        student_course text not null
                   
           )
  ''')
    #save connection
    connect.commit()
    # close the database student_details
    connect.close()

class studentAPI (BaseHTTPRequestHandler):

    def send_json_(self, data,status=200):
        # it send the http status code
        self.send_response(status)
        # send a json response code 
        self.send_header("Content-Type", "application/json")
        # end the header 
        self.end_headers()
        # send the json to the body of an content
        self.wfile.write(json.dumps(data).encode())

    def do_GET(self):
        # url path way of students
        if self.path == "/student_details" :
            #connect the student_details database
            Connect = mysql.connector.connect(**db_config)
            cursor = Connect.cursor()
            #its an sql querry to select the table
            cursor.execute("select * from student_details")
            rows = cursor.fetchall()
            #end the table close
            Connect.close()
            # the tables values of set of rows in tuple
            student_details = [{"student_id": r[0],
                                "student_name": r[1], 
                                "student_number": r[2], 
                                "student_email": r[3], 
                                "student_course": r[4]} for r in rows]
            # it can change the tuples to json files
            self.send_json_(student_details)
        else :
            # if it will not found its shows 404
            self.send_json_({"error": "Not found"}, 404)

    def do_POST(self):
        
        #path way
        if self.path == "/student_information" : 
            #splits the URL path into parts.
            length = int(self.headers.get("content-length"))
            #the server how many bytes are in the request body
            body = self.rfile.read(length)
            #store a body of data
            data = json.loads(body)

            connect = mysql.connector.connect(**db_config)
            cursor = connect.cursor()
            # insert the values for post method
            cursor.execute("insert into student_details (student_name, student_number, student_email, student_course) values (%s, %s, %s, %s)",
                           (data['student_name'], data['student_number'],  data['student_email'],  data['student_course']))
            connect.commit()
            connect.close()
            connect.close()
            # added message if the input is valied 
            self.send_json_({"message": "student_details added"}, 201)

        else:
             # if it will not found its shows 404
            self.send_json_({"error": "not found"}, 404)

    def do_PUT(self):
        #income path request of student details
        if self.path.startswith ("/student_update") :  
            # split the way url looks way
            try:
                student_id = int(self.path.split("/")[-1])

            except ValueError:
                return self.send_json_({"error": "Invalid student ID"}, 400)
        
            #splits the URL path into parts.
            length = int(self.headers.get("content-length"))
            #the server how many bytes are in the request body
            body = self.rfile.read(length)
            #store a body of data
            data = json.loads(body)

            
            connect = mysql.connector.connect(**db_config)
            cursor = connect.cursor()

            # insert the values for post method
            cursor.execute("UPDATE student_details SET student_name=%s, student_number=%s, student_email=%s, student_course=%s WHERE id=%s",
                            (data['student_name'], 
                            data['student_number'], 
                            data['student_email'],  
                            data['student_course'], 
                            student_id))
            connect.commit()
            rows_affected = cursor.rowcount
            cursor.close()
            connect.close()
            
            #number of rows affect if 0 means not founded 
            if rows_affected  > 0:
                self.send_json_({"message": "Updated successfully"})
            # if its not founded 404 error
            else:
                self.send_json_({"error": "Not found"}, 404)

        else:
            # if it will not found its shows 404
            self.send_json_({"error": "Not found"}, 404)

    def do_DELETE(self):
        if self.path.startswith("/student_delete/"):
            
            student_id = int(self.path.split("/")[-1])
            connect = mysql.connector.connect(**db_config)
            cursor = connect.cursor()
            cursor.execute("DELETE FROM student_details WHERE id=%s", (student_id,))
            connect.commit()
            rows_affected = cursor.rowcount
            cursor.close()
            connect.close()

            if rows_affected > 0:
                self.send_json_({"message": "Deleted successfully"})
            else:
                self.send_json_({"error": "Not found"}, 404)
        else:
            self.send_json_({"error": "Not found"}, 404)

if __name__ == "__main__":
    __init__db()
    server = HTTPServer(("localhost", 8000), studentAPI)
    print("Server running on http://127.0.0.1:8000")
    server.serve_forever()