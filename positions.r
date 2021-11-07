data <- read.csv("positions.csv", sep=";", colClasses=c("ID"="character"))
print(data)

library("ggplot2")
theme_set(theme_bw())
library("sf")

library(geojsonio)
gj <- geojson_read("geojson/ProvinciasArgentina.geojson", what = "sp")
library(broom)
tidied_gj <- tidy(gj)

library(dplyr)
tidied_gj = tidied_gj %>%
    left_join(. , data, by=c("id"="ID"))

bronze <- "#cd7f32"
silver <- "#C0C0C0"
gold <- "#d4af37"

library(viridis)

ggplot() +
    geom_polygon(data = tidied_gj, aes( x = long, y = lat, group = group, fill=Posicion), color="white") +
    scale_fill_viridis(breaks=c(1, 2, 3)) +
    theme_void() +
    coord_map()

