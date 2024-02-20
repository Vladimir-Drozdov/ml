#инициализация директории - dvc init
#dvc add $filename- добавляем файл для отслеживания
#git add $filename.dvc .gitignore
#git commit -m 'Add new data' - dvc сохраняет мета-информацию о файле с расширением .dvc
#на сайте dvc-есть tutorial, презентацию о dvc сбросят
#pip install urllib3
#python -m pip show urllib3
#dvc add data/data.xml - перед этим надо dvc init --no-scm
#dvc stage add -n prepare -p params -p prepare.seed,prepare.split -d src/prepare.py -d data/data.xml python src/prepare.py data/data.xml
#dvc metrics show или dvc plots show
#dvc stage add -n featurize -p featurize.max_features,featurize.ngrams -d src/featurization.py -d data/prepared  -o data/features python src/featurization.py data/prepared data/features
#dvc stage add -n train -p train.seed,train.n_est,train.min_split -d src/train.py -d data/features -o model.pkl python src/train.py data/features model.pkl
#в dvc решить spaceship titanic

#git clone https://github.com/sdukshis/mlops-dvc-example

