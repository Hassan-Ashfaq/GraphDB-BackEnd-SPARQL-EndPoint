Mapper  = [
    ["What is the Average Temperature of Ankara in November 2010?", 0],
    ["How many Cities had an Average Temperature Higher than 30°C in August 2010?", 1],
    ["What is the Name of the Continent of a City, which has the Lowest Average Temperature during the Month of January in 2012?", 2],
    ["What is the Name of the Hemishpere of a City, which has the Highest Average Temperature during the Month of May in 2010?", 3],
    ["Which Cities lie in China & its Location?", 4],
    ["Name the City with Highest Average Temperature in Pakistan during 2011?", 5],
    ["List Harbin's Average Temperature from Year 2010 to 2013 for the Month August?", 6]
]

All_Queries = [
"""prefix : <http://www.Climate.com/ClimateOntolog#>
SELECT  ?Temperature
WHERE {
  :Ankara_November_2010 :hasAvgTemperature ?Temperature
}""", 
"""prefix : <http://www.Climate.com/ClimateOntolog#>
SELECT  DISTINCT ?Weather ?Temperature
WHERE {
  ?City :hasWeatherRecord ?Weather.
  ?Weather :hasYear '2010';
     :hasMonth :August;
     :hasAvgTemperature ?Temperature.
    FILTER(?Temperature >= 30)
}""", 
"""prefix : <http://www.Climate.com/ClimateOntolog#>
SELECT  ?City ?Temperature ?Country ?Continent 
WHERE {
  ?City a :City;
     :belongToCountry ?Country;
     :hasWeatherRecord ?w.
  ?w a :WeatherRecord;
     :hasAvgTemperature ?Temperature;
     :hasMonth :January;
     :hasYear '2012'.
  ?Country a :Country;
     :belongToContinent ?Continent.
} ORDER BY ASC(?Temperature) LIMIT 1""",
"""prefix : <http://www.Climate.com/ClimateOntolog#>
SELECT  ?City ?Temperature ?Hemisphere
WHERE {
  ?City a :City;
     :belongToCountry ?Country;
     :hasWeatherRecord ?w.
  ?w a :WeatherRecord;
     :hasAvgTemperature ?Temperature;
     :hasMonth :May;
     :hasYear '2010'.
  ?country a :Country;
     :belongToContinent ?continent.
  ?continent a :Continent;
             :belongToHemisphere ?Hemisphere.
} ORDER BY DESC(?Temperature) LIMIT 1""",
"""PREFIX foaf: <http://xmlns.com/foaf/0.1/>
prefix : <http://www.Climate.com/ClimateOntolog#>
SELECT  ?City ?Name ?Latitude ?Longitude
WHERE {
  ?City a :City;
     :belongToCountry :China;
     :hasLatitude ?Latitude;
     :hasLongitude ?Longitude;
     foaf:name ?Name.
}""","""prefix : <http://www.Climate.com/ClimateOntolog#>
SELECT  DISTINCT ?City ?Temperature
WHERE {
  ?City a :City;
     :belongToCountry :Pakistan;
     :hasWeatherRecord ?w.
  ?w a :WeatherRecord;
     :hasAvgTemperature ?Temperature;
     :hasYear '2011'.
} ORDER BY DESC(?Temperature) LIMIT 1""", 
"""PREFIX foaf: <http://xmlns.com/foaf/0.1/>
prefix : <http://www.Climate.com/ClimateOntolog#>
SELECT ?Name ?Temperature ?Year
WHERE {
  :Harbin a :City;
          foaf:name ?Name;
          :hasWeatherRecord ?w.
  ?w a :WeatherRecord;
     :hasAvgTemperature ?Temperature;
     :hasMonth :August;
     :hasYear ?Year.
}
"""]