files=$(cat ../working_on_links.txt)

for file in $files
do
  # echo "------ $file ->"
  DIR=$(dirname $file)
  FILE=${file##*/}
  # echo DIR=$DIR
  # echo FILE=$FILE
  # ls -l $DIR/$FILE.md

  # grep "Daniel Han's Technical Notes" $DIR/$FILE.md
  title=$(grep "Daniel Han's Technical Notes" $DIR/$FILE.md | sed -e 's/.*\[\(.*\)\].*/\1/g')
  file=$DIR/$FILE.md
  echo "- [${title}](./${file})"
done
