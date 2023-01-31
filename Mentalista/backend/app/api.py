from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from . import schemas

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

questions = [
    schemas.Quiz(
        title="Qual é a capital do Brasil?", 
        options=[ "Belo Horizonte", "Rio de Janeiro", "São Paulo", "Brasília" ],
        answer=3
        ),
    schemas.Quiz(
        title="Qual é a cor do cavalo branco de Napoleão?", 
        options=[ "Branco", "Preto", "Marrom", "Cinza" ],
        answer=3
        ),
    # Adicionar mais perguntas aqui
]

fake_user = schemas.User(email='joao.bobo@bobo.com', password='123456', username='joao.bobo', fullname='joao bobo da silva')

@app.get("/")
def read_root():
    """ The base route from the API """
    
    return {"message": "Bem-vindo ao Quiz API"}

@app.get("/question/{question_id}")
def read_question(question_id: int):
    """ handdle with get requests from route 'question', return all details from a question. """
    
    question = questions[question_id]
    if question:
        return question
    return {"message": "Pergunta não encontrada"}

@app.get("/questions")
def read_questions(skip: int = 0, limit: int = 100):
    """ handdle with get requests from route 'questions', return a list of questions. """
    
    return questions[skip : skip + limit]

@app.get("/answer/{question_id}")
def read_answer(question_id: int, answer: int):
    """ handdle with get requests from route 'answer', return a message saying that the answer is correct or not. """
    
    question = questions[question_id]
    if question:
        if answer == question.answer:
            return {"message": "Vocé acertou."}
        return {"message" : "Você errou."}
    return {"message": "Pergunta não encontrada."}

@app.post("/question")
def creat_quiz(question: schemas.Quiz):
    """ handdle with post requests from route 'question', return a message saying that the question was created or not. """
    questions.append(question)
    return {"message": "Pergunta criada com sucesso."}