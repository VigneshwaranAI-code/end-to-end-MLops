import os 
import pandas as pd 
import joblib
from  sklearn.model_selection import RandomizedSearchCV
import lightgbm as lgb
from lightgbm import LGBMClassifier
from sklearn.metrics import accuracy_score , precision_score , recall_score, f1_score
from src.logger import get_logger
from src.Custom_exception import CustomException
from config.paths_config import *
from config.Model_para import *
from utils.common_function import read_yaml , load_data
from scipy.stats import randint
import mlflow


logger =get_logger(__name__)

class ModelTraining:
    def __init__(self,train_path,test_path,model_output_path):
        self.train_path = train_path
        self.test_path =test_path
        self.model_output_path = model_output_path
        self.params_dist =   LIGHTGM_MODEL
        self.random_search_params = RANDOM_SEARCH_PARAMS


    def load_and_split_data(self):
        try:
            logger.info(f'loading data from {self.train_path}')
            train_df = load_data(self.train_path)

            logger.info(f'Loading data from {self.train_path}')
            test_df = load_data(self.test_path)

            x_train = train_df.drop(columns=["booking_status"])
            y_train = train_df["booking_status"]

            x_test = test_df.drop(columns=["booking_status"])
            y_test = test_df["booking_status"]


            logger.info("Data Splitted succefully for model training")
            return x_train , y_train , x_test ,y_test
        except Exception as e:
            logger.error(f'Error while loading data {e}')
            raise CustomException("Failed to load data",e)

    def train_lgbm(self,X_train,y_train):
        try:
            logger.info("Intializing our model")

            lgbm_model = lgb.LGBMClassifier(random_state=self.random_search_params["random_state"])
            logger.info("starting our HYpermeter")

            random_search = RandomizedSearchCV(
                estimator=lgbm_model,
                param_distributions=self.params_dist,
                n_iter=self.random_search_params["n_iter"],
                cv=self.random_search_params["cv"],
                n_jobs=self.random_search_params["n_jobs"],
                verbose=self.random_search_params["verbose"],
                random_state=self.random_search_params["random_state"],
                scoring=self.random_search_params["scoring"]
            )

            logger.info("staring hyper parameter tuning ")
            random_search.fit(X_train,y_train)

            logger.info("Hyperparameter tuning complete ")

            best_params = random_search.best_params_
            best_lgbm_model = random_search.best_estimator_

            logger.info(f'Best parametes are : {best_params}')

            return  best_lgbm_model
        except Exception as e:
            logger.error(f'Error while training data {e}')
            raise CustomException("Failed to training data",e)

    def evaluate_model(self,model, X_test , y_test):
        try:
            logger.info("Evaluating our model")
            
            y_pred = model.predict(X_test)

            accuracy = accuracy_score(y_test,y_pred)
            precision = precision_score(y_test,y_pred)
            recall = recall_score(y_test,y_pred)
            f1= f1_score(y_test,y_pred)

            logger.info(f'Accuracy score ;{accuracy}')
            logger.info(f'precision score :{precision}')
            logger.info(f'recall score {recall}')
            logger.info(f'F1 score:{f1}')

            return {
                "accuracy":accuracy,
                "precision":precision,
                "recall":recall,
                "f1":f1
            }

        except Exception as e:
            logger.error(f'Error while evaluation model {e}')
            raise CustomException("Failed to evaluate data",e)

    def save_model(self,model):
        try:
            os.makedirs(os.path.dirname(self.model_output_path),exist_ok=True)
            logger.info("saving the model")
            joblib.dump(model,self.model_output_path)
            logger.info(f'Model saved to {self.model_output_path}')
        except Exception as e:
            logger.error(f'Error while evaluation model {e}')
            raise CustomException("Failed to evaluate data",e)
    def run(self):
        try:
            mlflow.set_experiment("Hotel Booking Prediction")
            with mlflow.start_run():
                logger.info("starting our model training pipeline")
                
                logger.info("starting our MLflow experimentation")

                logger.info("logging the training and testing datset to MLflow")
                mlflow.log_artifact(self.train_path , artifact_path="datasets")
                mlflow.log_artifact(self.test_path, artifact_path="datasets")

                X_train,y_train , X_test,y_test = self.load_and_split_data()
                best_lgbm_model = self.train_lgbm(X_train,y_train)
                model_metrics=self.evaluate_model(best_lgbm_model,X_test ,y_test)
                self.save_model(best_lgbm_model)

                logger.info("logging the model into MLflow")
                "mlflow.log_artifact(self.model_output_path)"

                mlflow.set_experiment("Hotel Booking Prediction")

                mlflow.sklearn.log_model(best_lgbm_model, "model",registered_model_name="HotelBookingModel")
                mlflow.log_params(best_lgbm_model.get_params())
                mlflow.log_metrics(model_metrics)

                """


                import mlflow.sklearn
                mlflow.sklearn.log_model(best_lgbm_model, "model")
                
                
                """

                logger.info("model Training sucessfully completed")

        except Exception as e:
            logger.error(f'Error while training pipeline model {e}')
            raise CustomException("Failed to training pipeline data",e)
        

if __name__=="__main__":
    trainer = ModelTraining(PROCESSED_TRAIN_DATA,PROCESSED_TEST_DATA,MODEL_OUTPUT_PATH)
    trainer.run()




