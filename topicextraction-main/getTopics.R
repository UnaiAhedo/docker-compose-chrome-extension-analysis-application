library(plumber)
library(tidyverse)
library("udpipe")
library(jsonlite)



#* parse JSON
#* @param req  the request object
#* @get /topics
#* @post /topics
function(req) {
  
  # http://127.0.0.1:8000/topics?items=30 (argsQuery)
  numItems <- as.numeric( if(length(req$argsQuery)==0) 10 else req$argsQuery )
  
  js <- as.data.frame(lapply(jsonlite::fromJSON(req$postBody), unlist))
  
  Sys.setlocale("LC_TIME","C")
  js$dateNum <- as.POSIXct(
    lubridate::with_tz(
      strptime(js$date,format='%b %d, %Y')))
  
  names(js)
  js$stars <- as.numeric(js$stars)
  
  
  # install.packages("udpipe")
  # en <- udpipe::udpipe_download_model("english")
  
  model <- udpipe_load_model("english-ewt-ud-2.5-191206.udpipe")
  doc <- udpipe::udpipe_annotate(model, js$text)
  
  # names(as.data.frame(doc))
  doc_df <- as.data.frame(doc)
  
  topics <- keywords_rake(x = doc_df , term = "lemma", group = "doc_id",
                          relevant = doc_df$upos %in%  c("NOUN", "ADJ"), ngram_max=10, n_min=1)
  
  
  # remove spam and french topics
  # topics <- head(topics %>% slice(-c(1,2,3,4,10)))
  
  return(head(topics,numItems))
  
  # write.table(result, file="testing_v3_xyz.csv", sep=",", row.names=FALSE, col.names=TRUE, append = T)
  
  # return(names(result))
}