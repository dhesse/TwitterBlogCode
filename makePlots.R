library(readr)
library(ggplot2)
topTags <- read_csv("topTags.csv")
ggplot(topTags, aes(x=Hashtag, y=`Use Count`)) +
  geom_bar(stat="identity", fill="steelblue") +
  theme(axis.text.x = element_text(angle = 90, hjust=1, vjust=0.5))
ggsave("topTags.png")
