
URLS=$(cat $1)
DEST_DIR="/Volumes/case-sensitive/git/tech-notes/src"

ROOT_URL=https://sites.google.com/site/xiangyangsite/home/technical-tips/

for URL in $URLS
do
  echo "====== $URL ->"
  RELATIVE_PATH=${URL#$ROOT_URL}
  echo RELATIVE_PATH=$RELATIVE_PATH
  DIR=$(dirname ${RELATIVE_PATH})
  echo DIR=$DIR
  mkdir -p $DEST_DIR/$DIR
  FILE_NAME=${RELATIVE_PATH##*/}
  echo FILE_NAME=$FILE_NAME

  mercury-parser $URL | ./reader.py  -f md - > $DEST_DIR/$DIR/$FILE_NAME.md
done
