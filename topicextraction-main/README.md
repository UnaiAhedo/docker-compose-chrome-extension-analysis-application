# Topic Extraction

# Run
`docker build --progress=plain -t extract-topics .`


# Build

`docker run --rm -p 8000:8000 extract-topics`

In case of needing to change the R script to execute, try this:

`docker run --rm -p 8000:8000 -v `pwd`/yourScript.R:/plumber.R extract-topics`

# Download sample.json file:
(this is just a file to use as an example)
https://www.dropbox.com/s/hojydjpqorhot3l/salida2.json?dl=1 

This salida2.json file has been obtained using the puppeteer script to extract comments from the chrome store in json format, running a command like this one: 

`$ node extractComments.js --extensionId=mmeijimgabbpbgpdklnllpncmdofkcpn > salida2.json`

# Usage: How to call the API endpoint

`$ curl --data @salida2.json http://127.0.0.1:8000/topics `

Output sample:

`$ curl --data @salida2.json http://127.0.0.1:8000/topics`


```[{"keyword":"user friendly larger time screen capture","ngram":6,"freq":1,"rake":21.0195},{"keyword":"default local save folder","ngram":4,"freq":1,"rake":8.6667},{"keyword":"occasional user such","ngram":3,"freq":1,"rake":7.5},{"keyword":"default save folder","ngram":3,"freq":1,"rake":6.6667},{"keyword":"big red flag","ngram":3,"freq":1,"rake":6},{"keyword":"chrome web store","ngram":3,"freq":1,"rake":6},{"keyword":"demo web design","ngram":3,"freq":1,"rake":6},{"keyword":"such reasonable price","ngram":3,"freq":1,"rake":6},{"keyword":"own overlay commentary","ngram":3,"freq":1,"rake":5.5},{"keyword":"version produce gif","ngram":3,"freq":1,"rake":5.25}]%```

# Usage: Define the number of topics to return using a queryString

`$  curl -s  --data @salida2.json http://127.0.0.1:8000/topics?items=15 | jq '.|length'`

```15```


