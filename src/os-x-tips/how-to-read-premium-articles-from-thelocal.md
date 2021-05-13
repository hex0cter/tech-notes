# How to read articles from thelocal

The script below will do the trick:

```
#!/bin/bash

URL=$1
OUTPUT=/tmp/thelocal-$$.html
curl --silent "$URL" --output $OUTPUT
sed -i -e 's,/userdata,http://www.thelocal.se/userdata,g' $OUTPUT
sed -i -e 's,/assets,http://www.thelocal.se/assets,g' $OUTPUT
echo "Saved into $OUTPUT"
open $OUTPUT
```
