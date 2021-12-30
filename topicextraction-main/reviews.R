getReviews <- function(app_id,country,page_num){
  
  
  
  #building_url
  
  
  json_url <- paste0('https://itunes.apple.com/',
                     country,
                     '/rss/customerreviews/page=',
                     page_num,
                     '/id=',
                     app_id,
                     '/sortby=mostrecent/',
                     'json')
  
  xml_url <- paste0('https://itunes.apple.com/',
                    country,
                    '/rss/customerreviews/page=',
                    page_num,
                    '/id=',
                    app_id,
                    '/sortby=mostrecent/',
                    'xml')
  
  
  js <- jsonlite::fromJSON(json_url)
  
  reviews <- cbind(Title = js$feed$entry$title$label,
                   Author_URL = js$feed$entry$author$uri,
                   Author_Name = js$feed$entry$author$name,
                   App_Version = js$feed$entry$`im:version`$label,
                   Rating = js$feed$entry$`im:rating`$label,
                   Review = js$feed$entry$content$label)
  
  # remove first line
  reviews <- reviews[-1,]
  
  names(reviews) <- c('Title','Author_URL','Author_Name','App_Version','Rating','Review')
  
  #reading xml for date
  
  
  
  xml_n <- xml2::read_xml(xml_url)
  
  
  entries <- xml2::xml_children(xml_n)[xml2::xml_name(xml2::xml_children(xml_n))=='entry']
  
  entries <- entries[-1]
  
  #extrcting date from entries
  
  date <- xml2::xml_text(
    xml2::xml_children(entries))[xml2::xml_name(xml2::xml_children(entries))=='updated']
  
  # POSIXct conversion to make it work with dplyr
  
  reviews$Date <- as.POSIXct(
    lubridate::with_tz(
      strptime(date,format='%Y-%m-%dT%H:%M:%S',tz='America/Los_Angeles'),
      tzone='Europe/London'))
  
  #re-arraning column order
  
  #reviews <- reviews[,c(7,4,5,1,6,3,2)]
  
  #to fix the rownumber/rownames issue
  
  # Formatting
  
  reviews$Title <- as.character(reviews$Title)
  
  reviews$Review <- as.character(reviews$Review)
  
  rownames(reviews) <- NULL
  
  return(reviews)
  
}

reviews1 <- getReviews("297606951", "us", 1)


# install.packages("curl")
# install.packages("xml2")
# install.packages("lubridate")

str(reviews1)


reviews_neg <- reviews1[ reviews1$Rating %in% c ('1','2'),]

reviews1$Rating 


# install.packages("udpipe")
library("udpipe")
# en <- udpipe::udpipe_download_model("english")

model <- udpipe_load_model("english-ewt-ud-2.5-191206.udpipe")
doc <- udpipe::udpipe_annotate(model, reviews$Review)

names(as.data.frame(doc))


doc_df <- as.data.frame(doc)

topics <- keywords_rake(x = doc_df , term = "lemma", group = "doc_id",
                        relevant = doc_df$upos %in%  c("NOUN", "ADJ"))
head(topics)

#install.packages("tidyverse")
library(tidyverse)

topics %>% 
  head() %>% 
  ggplot() + geom_bar(aes ( x = keyword, y = rake) , stat="identity", fill="#ff2211") +
  theme_minimal() + 
  labs( title = "Top Topics of Negative Customer Reviews",
        subtitle = "subtitle",
        caption = "caption")

