FROM python:3.10-slim
WORKDIR /smarts
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt -U
COPY . .
CMD python -m pytest -s --alluredir=allure/ /smarts/tests/