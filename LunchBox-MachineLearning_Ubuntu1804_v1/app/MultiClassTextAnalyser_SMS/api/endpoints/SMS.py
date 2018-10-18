from textblob import TextBlob
import sklearn
import numpy as np
from sklearn.externals import joblib
from ...main import app, request
import sys
from os.path import dirname
sys.path.append(dirname(__file__))

from split_into_lemmas import split_into_lemmas

#filename = '/data/sms_spam_detector.pkl'
#svm_detector_reloaded=joblib.load(filename);
filename = '../../../../data/sms_spam_detector.pkl'
svm_detector_reloaded=joblib.load(filename);
test1=split_into_lemmas("I am ok")
print(test1)
test="Amazon Shopping: Amazon Shopping: Arriving early: Thought Block Unruled Notebook (Size 5\" * 7\") (Pack of 3) will be delivered today by AmzAgent(1234567890).";
result= str( svm_detector_reloaded.predict([test])[0]);
print ((test)+':  '+ result)


@app.route('/SMS/')
def SMS_detect():
    SMS=request.args.get('SMS')
    if(SMS==None or SMS==''):
        SMS="test";
    test=[SMS]
    message=  ( svm_detector_reloaded.predict(test)[0])
    return SMS+"    "+message;
