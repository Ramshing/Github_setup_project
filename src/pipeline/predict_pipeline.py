import sys
import os
import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    ## This is the block were prediction going to done by using pickle files
    def __init__(self):        # empty constructor
        pass      

    def predict(self,features):
        # giving the dataframe to predict
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join("artifacts","preprocessor.pkl")
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        except Exception as e:
            raise CustomException(e,sys)


class CustomData:
    ## Handling html input data to back-end process
    ## This class called over app.py to get input values of user
    def __init__(self,gender:str,race_ethnicity:str,parental_level_of_education,lunch:str,test_preparation_course:str,
                 reading_score:int,writing_score:int):
        self.gender=gender
        self.race_ethnicity=race_ethnicity
        self.parental_level_of_education=parental_level_of_education
        self.lunch=lunch
        self.test_preparation_course=test_preparation_course
        self.reading_score=reading_score
        self.writing_score=writing_score

    def get_data_as_dataframe(self):
        ## Converting user entered data into dataframe
        try:
            custom_data_input_dict={
                'gender':[self.gender],
                'race_ethnicity':[self.race_ethnicity],
                'parental_level_of_education':[self.parental_level_of_education],
                'lunch':[self.lunch],
                'test_preparation_course':[self.test_preparation_course],
                'reading_score':[self.reading_score],
                'writing_score':[self.writing_score],
            }

            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            CustomException(e,sys)

    

