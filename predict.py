# 인코더 정의
from category_encoders import OrdinalEncoder
from sklearn.preprocessing import LabelEncoder
from imblearn.over_sampling import SMOTE
from lightgbm import LGBMClassifier
import joblib
import pandas as pd


df = pd.read_pickle("./fitness_export.pkl")
target = 'exercises'
X = df.drop(columns=['id','barriers','motivation','exercises'])
y = df[target]

# smote오버샘플링을 위한 전처리
encoder = OrdinalEncoder()
le = LabelEncoder()
smote = SMOTE(random_state=0)

X_encoded = encoder.fit_transform(X)
le.fit(y)
y_encoded= le.transform(y)

X_over, y_over = smote.fit_resample(X_encoded, y_encoded)

model = LGBMClassifier(random_state=2
            , n_jobs=-1
            , learning_rate=0.2
            , boost_from_average=False
            )
model.fit(X_over, y_over);

joblib.dump(model, './fitness_model.pkl')
joblib.dump(encoder, './fitness_encoder.pkl')
joblib.dump(le, './fitness_Label.pkl')
