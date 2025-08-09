.RECIPEPREFIX := >
.PHONY: install run test

install:
>pip install -r requirements.txt

run:
>PYTHONPATH=src uvicorn autocv.main:app --reload

test:
>PYTHONPATH=src pytest
