library(plumber)

# widelong_api <- plumber::plumb("./widelongwide.R")
topics_api <- plumber::plumb("./getTopics.R")
topics_api$run(host = '127.0.0.1', port = 8000)