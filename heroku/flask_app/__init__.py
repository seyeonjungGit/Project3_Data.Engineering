# 실행방법 : $ FLASK_APP=flask_app flask run
# $ pip freeze > requirements.txt
# 웹 주소 : https://fitness6302.herokuapp.com/ | 깃 저장소 : https://git.heroku.com/fitness6302.git
# https://fitness220407.herokuapp.com/ | https://git.heroku.com/fitness220407.git
import os
import pandas as pd

from flask import Flask, render_template, request, jsonify
import joblib

model = joblib.load('flask_app/fitness_model.pkl')
le = joblib.load('flask_app/fitness_Label.pkl')
encoder = joblib.load('flask_app/fitness_encoder.pkl')

def create_app():

    app = Flask(__name__)

    # 라우팅 정보 작성
    @app.route('/', methods=['GET','POST'])
    def make_prediction():
        if request.method == 'GET':
            return render_template('index.html')
        if request.method == 'POST':

            # 벨류값 가져오기.
            Gender = request.form.get('recommend_fitness')
            Age = request.form.get('age')
            Exercise_importance = request.form.get('exercise_importance', type=int, default=None)
            Fitness_level = request.form.get('fitness_level')
            Regularity = request.form.get('regularity')
            Do_you = request.form.get('do_you')
            Time = request.form.get('time')
            Time_spent = request.form.get('time_spent')
            Balanced_diet = request.form.get('balanced_diet')
            Health_level = request.form.get('health_level', type=int, default=None)
            Recommend_fitness = request.form.get('recommend_fitness')
            Equipment = request.form.get('equipment')
            Prevents_balanced = request.form.get('prevents_balanced')

            final_features = pd.DataFrame({"gender":[Gender], "age":[Age], "exercise_importance":[Exercise_importance], "fitness_level":[Fitness_level]
                    , "regularity":[Regularity],"do_you" : [Do_you], "time":[Time],"time_spent":[Time_spent],"balanced_diet":[Balanced_diet]
                    , "health_level":[Health_level],"recommend_fitness":[Recommend_fitness],"equipment":[Equipment],"prevents_balanced":[Prevents_balanced]})
            
            X_pred = encoder.transform(final_features) 
            fitt = le.inverse_transform(model.predict(X_pred))[0]

            return render_template('index.html', fitt = fitt)

    return app

if __name__ == "__main__":
  app = create_app()
  app.run(debug=True)




# <reference>
# flask에서 커스텀 모듈 불러올 때 주의사항 : https://stackoverflow.com/questions/65853229/flask-run-giving-me-modulenotfounderror
# https://www.nextree.co.kr/p8428/
# streamlit : https://zzsza.github.io/mlops/2021/02/07/python-streamlit-dashboard/
# https://livere.com/ : 강력한 댓글달기 툴.
# 플라스크 이용법: https://hleecaster.com/flask-introduction/
