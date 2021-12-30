# library
require(magrittr)
# require(httr)
require(jsonlite)

## transform wide to long and long to wide format
#' @post /widelong
#' @get /widelong
function(req) {

  
  # post body
  body <- jsonlite::fromJSON(req$postBody)
  
  .data <- body$.data
  .trans <- body$.trans
  
  # wide or long transformation
  if(.trans == 'l' || .trans == 'long') {
    return(.data)
  } else {
    print('Please specify the transformation')
  }
}