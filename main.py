from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector
app = FastAPI()

# Database connection parameters
db_config = {
    'host': '43.202.62.169',
    'user': 'gopher',
    'password': 'leon#cto',
    'database': 'tax_checker'
}

# Define the Pydantic model for request data validation
class Item(BaseModel):
    name: str
    contact: str  # Change 'mobile' to 'contact' to match your HTML form
    content: str
    created_at: str

# Function to insert data into the database
def db_insert(item: Item):
    # Connect to the database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Prepare the SQL insert statement
    insert_query = """
    INSERT INTO tax_checker (name, contact, story, created_at) 
    VALUES (%s, %s, %s, %s)
    """
    values_to_insert = (item.name, item.contact, item.content, item.created_at)  # Use the correct field names

    # Execute the insert statement
    cursor.execute(insert_query, values_to_insert)
    conn.commit()  # Commit the transaction

    # Close the connection
    cursor.close()
    conn.close()

cnt = 0

@app.get("/get_cnt")
async def get_cnt():
    return {"cnt": cnt}
@app.post("/update_cnt/{increment}")
async def update_cnt(increment: int):
    global cnt
    cnt += increment
    print(f"Current cnt value: {cnt}")
    return {"cnt": cnt}
@app.post("/reset_cnt")
async def reset_cnt():
    global cnt
    cnt = 0
    return {"cnt": cnt}


from fastapi.responses import FileResponse

@app.get("/")
async def root():
    return FileResponse('index.html')

@app.get("/Q1")
async def root():
    return FileResponse('Q1.html')

@app.get("/Q2")
async def root():
    return FileResponse('Q2.html')
@app.get("/Q3")
async def root():
    return FileResponse('Q3.html')
@app.get("/Q4")
async def root():
    return FileResponse('Q4.html')
@app.get("/Q5")
async def root():
    return FileResponse('Q5.html')

@app.get("/INFO")
async def root():
    return FileResponse('INFO.html')
@app.get("/RE1")
async def root():
    return FileResponse('RE1.html')
@app.get("/RE2")
async def root():
    return FileResponse('RE2.html')
@app.get("/RE3")
async def root():
    return FileResponse('RE3.html')
@app.get("/RE4")
async def root():
    return FileResponse('RE4.html')
@app.get("/RE5")
async def root():
    return FileResponse('RE5.html')

@app.get("/agree")
async def root():
    return FileResponse('agree.html')
@app.get("/insert")
async def root():
    return FileResponse('insert.html')
@app.get("/thanks")
async def root():
    return FileResponse('thanks.html')

@app.get("/ad#ministra#tor")
async def root():
    return FileResponse('thanks.html')


# POST
from pydantic import BaseModel

@app.post("/send")
async def send(item: Item):
    # Insert the data into the database
    db_insert(item)
    return {"message": "Data inserted successfully"}