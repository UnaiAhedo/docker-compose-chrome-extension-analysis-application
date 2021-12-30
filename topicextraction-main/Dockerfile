FROM rstudio/plumber
MAINTAINER Docker User <docker@user.org>

RUN apt-get update --allow-releaseinfo-change && apt-get install -y libz-dev
RUN R -e "install.packages(c('tidyverse','dplyr','udpipe','jsonlite'), \
repos = 'http://cran.us.r-project.org')"
RUN R -e "udpipe::udpipe_download_model('english')"

COPY ./getTopics.R /plumber.R

CMD ["/plumber.R"]
