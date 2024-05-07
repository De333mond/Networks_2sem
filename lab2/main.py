import math

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

ASDFASDF = 'asdfasdf'

ASDF = 'asdf'
app = FastAPI()

origins = [
    "http://localhost"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Expression(BaseModel):
    operand1: int | None = 0
    operand2: int
    operator: str


class CalculationResponse(BaseModel):
    result: float


@app.post('/calculate')
def calculate(exp: Expression) -> CalculationResponse:
    str_to_func = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        'sin': lambda x, y: math.sin(y),
        'cos': lambda x, y: math.cos(y),
        'tan': lambda x, y: math.tan(y),
        'cot': lambda x, y: 1 / math.tan(y),
        '^': lambda x, y: x ** y,
        'sqrt': lambda x, y: math.sqrt(y),
    }

    if not exp.operand1:
        exp.operand1 = 0

    return CalculationResponse(result=str_to_func[exp.operator](exp.operand1, exp.operand2))
