from fastapi import FastAPI


app = FastAPI()

origins = ["http://localhost:3000"]  # React app running on port 3000

@app.get("/")
def root():
    """
    Main entry point of the API.

    Returns a simple JSON with a friendly message.
    """
    return {"message": "Hello World"}