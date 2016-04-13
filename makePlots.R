library(readr)
library(ggplot2)
topTags <- read_csv("topTags.csv")
ggplot(topTags, aes(x=Hashtag, y=`Use Count`)) +
  geom_bar(stat="identity", fill="steelblue") +
  theme(axis.text.x = element_text(angle = 90, hjust=1, vjust=0.5))
ggsave("topTags.png")
topURLs <- read_csv("topURLs.csv")
ggplot(topURLs, aes(x=`Base URL`, y=`Use Count`)) +
  geom_bar(stat="identity", fill="steelblue") +
  theme(axis.text.x = element_text(angle = 90, hjust=1, vjust=0.5))
ggsave("topURLs.png")
topURLsExpanded <- read_csv("topURLsExpanded.csv")
ggplot(topURLsExpanded, aes(x=`Base URL`, y=`Use Count`)) +
  geom_bar(stat="identity", fill="steelblue") +
  theme(axis.text.x = element_text(angle = 90, hjust=1, vjust=0.5))
ggsave("topURLsExpanded.png")
