Title: Weather Station
Date: 2020-07-18 16:00
Modified: 2020-07-25 19:30
Tags: Raspberry Pi, Python, weather station

# As a studied atmospheric scientist it is almost a duty to operate a personal weather station [(PWS)](https://www.wunderground.com/dashboard/pws/IPATSC2/).

Here you can see the outside sensors.
![Photo](/images/weather_station/IMG_20200705_154307_resize.jpg)

It is a Renkfore radio weather station ["WH2315"](https://www.amazon.de/Renkforce-WH2315-Funk-WETTERSTATION/dp/B01N4DK6TG#ace-g6772571139).
The station has a radio connection to a basis station and this is connected to a Raspberry Pi.
The data is than hosted via [weex](http://www.weewx.com/) to [Wunderground](https://www.wunderground.com/).

Below is a picture of the basis station.
![Photo](/images/weather_station/IMG_20200726_172233_resize.jpg)

Here you can see a sample screenshot of my PWS taken from Wunderground suitable to the photo above. 
![Photo](/images/weather_station/renkforce_weather_history_ipatsc2_Screenshot from 2020-07-27 21-01-11.png)

## Technical Data:
|                       |                       | Range                  | Resolution                                                                 | Accuracy                                                          |
|-----------------------|-----------------------|------------------------|----------------------------------------------------------------------------|-------------------------------------------------------------------|
| Basis Station sensors |                       |                        |                                                                            |                                                                   |
|                       | Temperature           | -9.9 °C - +60 °C       | 0.1%                                                                       | +-1 °C                                                            |
|                       | Relative humidity     | 1% - 99%               | 1%                                                                         | +-5%                                                              |
|                       | Barometric pressure   | 300 - 1100 hPa         | 0.1%                                                                       | +-3 hPa in the area of 700 - 1100 hPa                             |
| Outside sensors       |                       |                        |                                                                            |                                                                   |
|                       | Temperature           | -40 °C - +60 °C        | 0.1 °C                                                                     | +-1 °C                                                            |
|                       | Relative humidity     | 1% - 99%               | 1%                                                                         | +-5%                                                              |
|                       | Rain volume           | 0 - 9999 mm            | 0.3 mm (at rain volume of < 1000 mm) 1 mm (at rain volume of >= 1000 mm)   | +-10%                                                             |
|                       | Wind speed            | 0 - 50 m/s             | -                                                                          | +- 1 m/s  (at wind speed < 5 m/s) +- 10% (at wind speed >= 5 m/s) |
|                       | Illumination strength | 0 - 300000 lux         | -                                                                          | +- 15%                                                            |
|                       | UV-index              | 0 - 15 (0 - 20000 W/m² | -                                                                          | -                                                                 |

Finally a link to [live data of my PWS](https://www.wunderground.com/dashboard/pws/IPATSC2/).

### Will be be continued...


