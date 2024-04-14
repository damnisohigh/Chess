from fastapi import FastAPI
from fastapi.responses import JSONResponse
from my_chess import GameBoard

app = FastAPI()
board = GameBoard()


@app.get("/positions", response_model=list)
def positions():
    js_data = {}
    for y in range(1, 9):
        for x in range(1, 9):
            piece = board.squares[(x, y)]
            if not piece:
                js_data[f"{x} {y}"] = None    
            else:
                js_data[f"{x} {y}"] = {
                    "color": piece.color,
                    "y": piece.y_coord,
                    "x": piece.x_coord,
                    "name": piece.name,
                }
    return JSONResponse(js_data)


@app.put("/move_to/{fx}/{fy}/{tx}/{ty}")
def move(fx: int, fy: int, tx: int, ty: int):
    board.move((fx, fy), (tx, ty))
    return {"moved": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
