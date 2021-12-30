#install.packages("tidyverse")
library("tidyverse")
library("udpipe")

json_url<- "/opt/extractComments/salida2.json"

js <- jsonlite::fromJSON(json_url)

class(js)
names(js)

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
head(topics,10)

# remove spam and french topics
# topics <- head(topics %>% slice(-c(1,2,3,4,10)))

# Save to text
# write.table(js$text, file = "comments.txt", sep = " ",row.names = FALSE)



topics %>% 
  head() %>% 
  ggplot() + geom_bar(aes ( x = keyword, y = rake) , stat="identity") +
  theme_minimal() + 
  theme(axis.text.x = element_text(angle = 40, hjust=1.00, vjust = 1.0)) +
  labs( title = "Top Topics of Reviews",
        subtitle = "Extension: Screencastify Site",
        caption = "") 
# -> p

# png("fig1.png",width = 800, height = 800, units = "px")
# print(p)
# dev.off()

