from flask import Flask
import sys
from insurance.logger import logging
from insurance.exception import InsuranceException

app=Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
        project_name = InsuranceException(e, sys)
        logging.info(project_name.error_message)
        logging.info("We are testing logging module")
    return "CI CD pipeline has been established."

if __name__=="__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
