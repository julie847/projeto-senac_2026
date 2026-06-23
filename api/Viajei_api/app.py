ttp import HTTPSstatus 

astapi import FastAPI   

ast_zero.schemas import message 

app = FastAPI()

@app.get ('/', status_code=HTTPSstatus.OK response_model=message)

def read_root():
    return {'message': 'Olá mundo !'}
            