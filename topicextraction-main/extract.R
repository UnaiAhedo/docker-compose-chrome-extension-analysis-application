library(itunesr)

reviews1 <- getReviews("297606951", "us", 1)

reviews2 <- getReviews("297606951", "us", 2)

reviews <- rbind(reviews1, reviews2)

head(reviews)
##                                    Title
## 1      Fine Anything Easy, Good Policies
## 2                       Customer support
## 3 Uh oh, something went wrong on our end
## 4                        Connection Lost
## 5             Add this app to the I-Pads
## 6                            Wish lists!
##                                        Author_URL           Author_Name
## 1 https://itunes.apple.com/us/reviews/id899889795    KeithAppProgrammer
## 2 https://itunes.apple.com/us/reviews/id978296731             Stormdoll
## 3  https://itunes.apple.com/us/reviews/id33953389             Joker1138
## 4   https://itunes.apple.com/us/reviews/id8865955       Loquacious lair
## 5  https://itunes.apple.com/us/reviews/id43459956               MattC4U
## 6 https://itunes.apple.com/us/reviews/id389452759 Best update ever12345
##   App_Version Rating
## 1     13.15.0      5
## 2     13.15.0      5
## 3     13.15.0      1
## 4     13.15.0      2
## 5     13.15.0      1
## 6     13.15.0      1
##                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      Review
## 1                                                                                                                                                                                                                                                                                                                       We’ve been quite blessed to work with Amazon. Searching for odd items, the App also has some compatibility safeguards. If I need to return something, it really couldn’t be easier.
## 2 I love not having to call if there is an issue. The mobile app has great automated features to reach someone and when there is a problem it’s resolved quickly and in the manner I request instead of just a refund . - meaning I was able to get half of my order refunded and the other half mailed again as my first package was listed lost. The items I needed more quickly than could arrive were swiftly refunded and the other items mailed again without a problem this time - super convenient!
## 3                                                                                                                                                                                                                                                                                                                                                               Constantly getting the above error message combined with random pictures of dogs. Hasn’t been fixed for a couple weeks. Pretty frustrating.
## 4                                                                                                                                                                                                                                                                                                                                                                       The app is constantly crashing and telling me that the network connection has been lost even if I have full access to WiFi or data.
## 5                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     This makes me so mad.
## 6                                                                                                                                                                                                                                     What did you do Amazon? Changing the way we saved wish list items was a horrible idea. Whoever came up with this heart update instead of holding and dropping needs to be demoted immediately. Please fix this. We also need Amazon smile ability in the app as well.
##                  Date
## 1 2019-08-21 13:54:37
## 2 2019-08-21 11:39:40
## 3 2019-08-21 10:21:20
## 4 2019-08-21 07:11:33
## 5 2019-08-21 05:25:44
## 6 2019-08-21 05:20:25