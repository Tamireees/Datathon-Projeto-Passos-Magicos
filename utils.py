from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder, OrdinalEncoder
from imblearn.over_sampling import SMOTE
from sklearn.pipeline import Pipeline
import pandas as pd

class DropFeatures(BaseEstimator, TransformerMixin):
    def __init__(self, feature_to_drop=['NOME']):             
        self.feature_to_drop = feature_to_drop
        
    def fit(self, df):                                              
        return self                                                 
                                                                    
    
    def transform(self, df):                                    
        if (set(self.feature_to_drop).issubset(df.columns)):        
            df.drop(self.feature_to_drop, axis=1, inplace= True)       
                                                                    #
            return df
        else:
            print('Uma ou mais features não estão no DataFrame')
            return df
        
class MinMax(BaseEstimator,TransformerMixin):
    def __init__(self,min_max_scaler  = ['PONTO_VIRADA_2020', 'PONTO_VIRADA_2021','PONTO_VIRADA_2022' ]):
        self.min_max_scaler = min_max_scaler 
    def fit(self,df):
        return self
    def transform(self,df):
        if (set(self.min_max_scaler ).issubset(df.columns)):
            min_max_enc = MinMaxScaler()
            df[self.min_max_scaler] = min_max_enc.fit_transform(df[self.min_max_scaler ])
            return df
        else:
            print('Uma ou mais features não estão no DataFrame')
            return df
        
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import OneHotEncoder
import pandas as pd

class OneHotEncodingNames(BaseEstimator,TransformerMixin):
    def __init__(self,OneHotEncoding = ['dimensao_psicopedagogica', 'dimensao_academica', 'dimensao_psicossocial', 'PEDRA_2020', 'PEDRA_2021', 'PEDRA_2022']):                                      
                                                                           
        self.OneHotEncoding = OneHotEncoding

    def fit(self,df):
        return self

    def transform(self,df):
        if (set(self.OneHotEncoding).issubset(df.columns)):
            # função para one-hot-encoding das features
            def one_hot_enc(df,OneHotEncoding):
                one_hot_enc = OneHotEncoder()
                one_hot_enc.fit(df[OneHotEncoding])
                # obtendo o resultado dos nomes das colunas
                feature_names = one_hot_enc.get_feature_names_out(OneHotEncoding)
                # mudando o array do one hot encoding para um dataframe com os nomes das colunas
                df = pd.DataFrame(one_hot_enc.transform(df[self.OneHotEncoding]).toarray(),
                                  columns= feature_names,index=df.index)
                return df

            # função para concatenar as features com aquelas que não passaram pelo one-hot-encoding
            def concat_with_rest(df,one_hot_enc_df,OneHotEncoding):              
                # get the rest of the features
                outras_features = [feature for feature in df.columns if feature not in OneHotEncoding]
                # concaternar o restante das features com as features que passaram pelo one-hot-encoding
                df_concat = pd.concat([one_hot_enc_df, df[outras_features]],axis=1)
                return df_concat

            # one hot encoded dataframe
            df_OneHotEncoding = one_hot_enc(df,self.OneHotEncoding)

            # retorna o dataframe concatenado
            df_full = concat_with_rest(df, df_OneHotEncoding,self.OneHotEncoding)
            return df_full

        else:
            print('Uma ou mais features não estão no DataFrame')
            return df
        
class OrdinalFeature(BaseEstimator,TransformerMixin):
    def __init__(self,ordinal_feature = ['FASE_2020', 'FASE_2021', 'FASE_2022']):
        self.ordinal_feature = ordinal_feature
    def fit(self,df):
        return self
    def transform(self,df):
        if (set(self.ordinal_feature ).issubset(df.columns)):
            ordinal_encoder = OrdinalEncoder()
            df[self.ordinal_feature] = ordinal_encoder.fit_transform(df[self.ordinal_feature])
            return df
        else:
            print('Uma ou mais features não estão no DataFrame')
            return df
        
from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd

class EnsureColumnsTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, expected_columns=None):
        self.expected_columns = expected_columns if expected_columns else []

    def fit(self, X, y=None):
        return self  # Nenhum ajuste necessário

    def transform(self, X):
        X = X.copy()
        # Adiciona as colunas ausentes com valor 0
        for col in self.expected_columns:
            if col not in X.columns:
                X[col] = 0
        # Ordena as colunas para manter a mesma ordem que foi usada no treino
        X = X[self.expected_columns]
        return X

        
class Oversample(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    
    def fit(self, df, y=None):
        # Não faz nada no fit, mas é necessário para usar no pipeline
        return self
    
    def transform(self, df):
        if 'ATIVO' in df.columns:
            # Aplica SMOTE usando 'ATIVO' como target
            oversample = SMOTE(sampling_strategy='minority')
            
            # Separa X e y
            X = df.loc[:, df.columns != 'ATIVO']
            y = df['ATIVO']
            
            # Aplica o SMOTE para balanceamento
            X_bal, y_bal = oversample.fit_resample(X, y)
            
            # Combina as variáveis X e y balanceadas em um único DataFrame
            df_bal = pd.DataFrame(X_bal, columns=X.columns)  # Usando as colunas originais de X
            df_bal['ATIVO'] = y_bal  # Adiciona a coluna de ATIVO
            
            return df_bal
        else:
            print("O target 'ATIVO' não está no DataFrame")
            return df

colunas_treinadas = ['dimensao_psicopedagogica_abaixo da media',
                    'dimensao_psicopedagogica_excelente',
                    'dimensao_academica_abaixo da media', 'dimensao_academica_excelente',
                    'dimensao_psicossocial_abaixo da media',
                    'dimensao_psicossocial_excelente', 'PEDRA_2020_Ametista',
                    'PEDRA_2020_Quartzo', 'PEDRA_2020_Topázio', 'PEDRA_2020_Ágata',
                    'PEDRA_2021_Ametista', 'PEDRA_2021_Quartzo', 'PEDRA_2021_Topázio',
                    'PEDRA_2021_Ágata', 'PEDRA_2022_Ametista', 'PEDRA_2022_Quartzo',
                    'PEDRA_2022_Topázio', 'PEDRA_2022_Ágata', 'FASE_2020', 'FASE_2021',
                    'FASE_2022', 'PONTO_VIRADA_2020', 'PONTO_VIRADA_2021',
                    'PONTO_VIRADA_2022', 'ANO_INGRESSO']

def novo_pipeline(df):
    # Definir o pipeline com os transformadores
    pipeline = Pipeline([
        ('feature_dropper', DropFeatures()),                                # Remove features desnecessárias
        ('OneHotEncoding', OneHotEncodingNames()),                          # Codificação OneHot para variáveis categóricas
        ('ensure_columns', EnsureColumnsTransformer(colunas_treinadas)),    # Garante colunas
        ('ordinal_feature', OrdinalFeature()),                              # Codificação ordinal para variáveis ordinais
        ('min_max_scaler', MinMax()),                                       # Normalização dos dados
        ('oversample', Oversample())                                        # Superamostragem para balancear as classes
    ])
    
    try:
        # Aplicar o pipeline de transformação e retornar o resultado
        df_pipeline = pipeline.fit_transform(df)
        return df_pipeline
    except Exception as e:
        print(f"Erro ao aplicar o pipeline: {e}")
        return None