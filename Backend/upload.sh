cp src/metroDataBase.db metroDataBase.db
rm upload.zip
zip upload.zip lambda_function.py metroDataBase.db  src/aEstrella.py src/metro.py
rm metroDataBase.db
aws --profile personal lambda update-function-code --function-name arn:aws:lambda:eu-west-3:619878177039:function:tokyoAEstrella --zip-file fileb://upload.zip