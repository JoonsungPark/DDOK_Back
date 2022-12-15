from flask import Flask, request, redirect
from pymongo import MongoClient

app = Flask(__name__) 


@app.route('/') # 생성한 객체의 route 설정 = URL 설정
def index(): # 함수 생성
	return 'Hello World!'



#if __name__ == '__main__': # 실행한 서버가 현재 동작되는 유일한 서버
app.run() # run() 함수로 어플리케이션을 로컬 서버로 실행(기본 포트 5000)